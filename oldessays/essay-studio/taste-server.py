#!/usr/bin/env python3
"""Local review server: rank thumbnail candidates per essay, save feedback,
and search the image catalog informed by your taste profile.

Endpoints:
  GET  /                     review page
  GET  /img/<file>           candidate image
  GET  /api/bundle           full bundle
  GET  /api/state            bundle + current feedback
  POST /api/feedback         save ranking/rejections for an essay
  GET  /api/search?q=...     search images, ranked by taste profile
  GET  /api/profile          current taste profile
"""
import json, os, sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs, unquote

ESSAYS = Path("/root/projects/ochema2/essays")
BUNDLE = ESSAYS / "review-bundle.json"
FEEDBACK = ESSAYS / "thumbnail-feedback.json"
PROFILE = ESSAYS / "taste-profile.json"
IMG_DIR = ESSAYS / "review-images"

sys.path.insert(0, str(ESSAYS))
from match_thumbnails import build_catalog, norm, WEIGHTS


def load(path, default):
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return default


FEEDBACK = load.__code__  # noqa — see load_state below


def load_state():
    bundle = load(BUNDLE, {})
    feedback = load(FEEDBACK, {})
    return bundle, feedback


def save_feedback(feedback):
    FEEDBACK.write_text(json.dumps(feedback, indent=2))


PAGE = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Thumbnail taste review</title>
<style>
body{font-family:system-ui,sans-serif;background:#141414;color:#e8e8e8;margin:0;padding:20px}
#meta{max-width:900px;margin:0 auto 16px}
h1{font-size:20px;margin:0 0 4px}
#meta .sub{color:#999;font-size:13px}
#card{max-width:900px;margin:0 auto;background:#1e1e1e;border:1px solid #333;border-radius:10px;padding:18px}
h2{font-size:16px;margin:0 0 6px}
.kws{color:#9a9a9a;font-size:12px;margin-bottom:14px}
#grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.cand{background:#2a2a2a;border:2px solid #3a3a3a;border-radius:8px;overflow:hidden;cursor:grab;position:relative}
.cand img{width:100%;height:150px;object-fit:cover;display:block}
.cand .info{padding:6px 8px;font-size:11px}
.cand .info .src{color:#7fd6a0}
.cand .info .img{color:#999;word-break:break-all}
.cand .rank{position:absolute;top:6px;left:6px;background:rgba(0,0,0,.75);border-radius:6px;padding:2px 8px;font-weight:bold;font-size:13px}
.cand .btn{position:absolute;top:6px;right:6px;background:rgba(0,0,0,.75);border:none;border-radius:6px;padding:4px 10px;color:#fff;cursor:pointer;font-size:12px}
.cand.ranked{border-color:#ffd166}
.cand.rejected{opacity:.45;border-color:#c0392b}
.cand.rejected::after{content:"REJECTED";position:absolute;top:6px;left:6px;background:#c0392b;border-radius:6px;padding:2px 8px;font-size:11px;font-weight:bold}
#nav{display:flex;gap:8px;margin-top:16px;align-items:center}
button{background:#3a5a8a;border:none;color:#fff;padding:8px 14px;border-radius:6px;cursor:pointer;font-size:13px}
button.primary{background:#2e7d4f}
button:hover{filter:brightness(1.15)}
#prog{color:#bbb;font-size:13px;margin-left:auto}
</style></head><body>
<div id="meta">
<h1>Thumbnail taste review</h1>
<div class="sub" id="sub"></div>
</div>
<div id="card">
<h2 id="title"></h2>
<div class="kws" id="kws"></div>
<div id="grid"></div>
<div id="nav">
  <button onclick="prev()">Prev</button>
  <button onclick="save(false)">Save</button>
  <button class="primary" onclick="save(true)">Save &amp; Next</button>
  <span id="prog"></span>
</div>
</div>
<script>
let bundle={}, state={}, feedback={}, order=[], idx=0, ranks={}, rejected={};
const sortRank=()=>[...document.querySelectorAll('.cand')].sort((a,b)=>{
  const ra=+a.dataset.r||1e9, rb=+b.dataset.r||1e9; return ra-rb;
}).forEach((el,i)=>{el.style.order=i});
function render(){
  const key=order[idx], e=bundle[key];
  document.getElementById('title').textContent=e.title;
  document.getElementById('kws').textContent='KEYWORDS: '+(e.keywords||[]).join(' · ');
  document.getElementById('prog').textContent=`${idx+1} / ${order.length}`;
  const grid=document.getElementById('grid'); grid.innerHTML='';
  ranks=state.feedback[key]?.ranking||{}; rejected=state.feedback[key]?.rejected||{};
  e.candidates.forEach((c,i)=>{
    const d=document.createElement('div'); d.className='cand';
    d.dataset.key=key; d.dataset.i=i;
    const r=ranks[c.image];
    if(r){d.classList.add('ranked'); d.dataset.r=r;}
    if(rejected[c.image])d.classList.add('rejected');
    d.innerHTML=`<img src="/img/${c.file}" loading="lazy">
      <span class="rank">${r?('# '+r):'—'}</span>
      <button class="btn" onclick="event.stopPropagation();rej(${i})">✕</button>
      <div class="info"><div class="src">${c.source}</div><div class="img">${c.image}</div>
      <div>${c.title}</div></div>`;
    d.onclick=()=>setRank(i);
    grid.appendChild(d);
  });
  render();
}
function setRank(i){
  const key=order[idx], img=bundle[key].candidates[i].image;
  const cur=ranks[img]; const n=Object.keys(ranks).length;
  if(cur===undefined){ranks[img]=n+1;}
  else{ranks[img]=undefined;delete ranks[img];}
  document.querySelectorAll('.cand').forEach((el,ii)=>{
    const im=bundle[key].candidates[ii].image;
    const rr=ranks[im];
    el.classList.toggle('ranked',!!rr); el.dataset.r=rr;
    el.querySelector('.rank').textContent=rr?('# '+rr):'—';
  });
  sortRank();
}
function rej(i){
  const key=order[idx], img=bundle[key].candidates[i].image;
  rejected[img]=!rejected[img];
  document.querySelectorAll('.cand')[i].classList.toggle('rejected',rejected[img]);
}
function save(next){
  const key=order[idx], e=bundle[key];
  const ranking={};
  // normalize: ranked get 1..k in current DOM order
  const els=[...document.querySelectorAll('.cand')].filter(el=>el.dataset.r)
    .sort((a,b)=>+a.dataset.r-+b.dataset.r);
  els.forEach((el,k)=>{ranking[bundle[key].candidates[+el.dataset.i].image]=k+1;});
  feedback[key]={ranking, rejected:{...rejected}, ts:Date.now()};
  state.feedback=feedback;
  fetch('/api/feedback',{method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify(feedback)}).then(()=>{
    if(next)go(idx+1);
  });
}
function go(n){if(n<order.length){idx=n;render();}window.scrollTo(0,0);}
function prev(){if(idx>0){idx--;render();}}
async function init(){
  state=await (await fetch('/api/state')).json();
  bundle=state.bundle; feedback=state.feedback||{};
  order=Object.keys(bundle);
  document.getElementById('sub').textContent=`${order.length} essays · ${Object.keys(feedback).length} reviewed · click a card to rank (click order = rank), ✕ to reject`;
  render();
}
init();
</script></body></html>
"""


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, body, ctype="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        u = urlparse(self.path)
        p = u.path
        if p == "/":
            self._send(200, PAGE.encode(), "text/html")
        elif p.startswith("/img/"):
            fname = unquote(p[len("/img/"):])
            fp = IMG_DIR / os.path.basename(fname)
            if not fp.exists():
                self._send(404, b"not found")
                return
            data = fp.read_bytes()
            self._send(200, data, "image/jpeg")
        elif p == "/api/bundle":
            bundle = load(BUNDLE, {})
            self._send(200, json.dumps(bundle).encode())
        elif p == "/api/state":
            bundle, feedback = load_state()
            self._send(200, json.dumps({"bundle": bundle, "feedback": feedback}).encode())
        elif p == "/api/profile":
            profile = load(PROFILE, {})
            self._send(200, json.dumps(profile).encode())
        elif p == "/api/search":
            q = parse_qs(u.query).get("q", [""])[0]
            profile = load(PROFILE, {})
            res = search(q, profile)
            self._send(200, json.dumps(res, indent=2).encode())
        else:
            self._send(404, b"not found")

    def do_POST(self):
        u = urlparse(self.path)
        if u.path == "/api/feedback":
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            FEEDBACK.write_text(json.dumps(body, indent=2))
            self._send(200, json.dumps({"ok": True}).encode())
        else:
            self._send(404, b"not found")


def search(q, profile):
    """Rank catalog images for a free-text query using taste profile boosts."""
    catalog = build_catalog()
    qk = norm(q)
    local = [c for c in catalog if c.get("local_path")]
    image_pref = profile.get("image_pref", {})
    source_aff = profile.get("source_affinity", {}).get("all", {})
    concept_w = profile.get("concept_weights", {})
    scored = []
    for c in local:
        ik = norm(c["text"])
        if not ik or not (qk & ik):
            continue
        s = sum(WEIGHTS.get(w, 1) for w in (qk & ik))
        for w in (qk & ik):
            s += concept_w.get(w, {}).get("delta", 0)
        s *= 1 + source_aff.get(c["source"], {}).get("delta", 0)
        s *= 1 + image_pref.get(c["id"], {}).get("delta", 0)
        scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    out = [{
        "image": c["id"], "source": c["source"],
        "title": (c.get("title") or "")[:80], "file": os.path.basename(c["local_path"]),
        "score": round(s, 3),
    } for s, c in scored[:20]]
    return {"query": q, "results": out}


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8700
    print(f"taste server on http://localhost:{port}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
