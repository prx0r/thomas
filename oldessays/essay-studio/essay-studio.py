#!/usr/bin/env python3
"""Essay Studio — a simple essay reader + editor.

Read essays full-screen (two columns on wide screens), edit the working text,
save versions, and track whether you've recorded audio for each essay.
Audio files are uploaded separately to the R2 bucket `essayaudio`; this app
polls the bucket and auto-marks essays as recorded when a matching audio file
appears.

State file: essays/essay-studio-state.json
"""
import json, os, re, shutil, subprocess, sys, threading, time
from pathlib import Path
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs, unquote

ESSAYS = Path("/root/projects/ochema2/essays")
STATE_FILE = ESSAYS / "essay-studio-state.json"
AUDIO_DIR = ESSAYS / "audio"
R2_REMOTE = "r2:essayaudio"
AUDIO_EXTS = (".m4a", ".mp3", ".mp4", ".webm", ".wav", ".ogg", ".aac", ".opus", ".m4b", ".flac")

def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2))


def essay_list():
    out = []
    for d in sorted(ESSAYS.iterdir()):
        if not d.is_dir() or d.name.startswith("."):
            continue
        for f in sorted(d.iterdir()):
            if f.suffix not in (".md", ".json"):
                continue
            text = f.read_text(errors="ignore")
            title = ""
            for line in text.splitlines()[:6]:
                if line.startswith("# "):
                    title = line[2:]
                    break
            if not title and f.suffix == ".json":
                try:
                    title = json.loads(text).get("title", f.stem)
                except Exception:
                    title = f.stem
            if not title:
                title = f.stem.replace("-", " ").replace("_", " ")
            out.append({
                "key": f"{d.name}/{f.name}",
                "collection": d.name,
                "file": f.name,
                "title": title,
                "words": len(text.split()),
                "ext": f.suffix,
                "path": str(f),
            })
    return out


def find_essay(key):
    for e in essay_list():
        if e["key"] == key:
            return e
    return None


def essay_for_audio(path):
    """Map an audio file path in the bucket to an essay key."""
    stem = str(Path(path).with_suffix("")).replace("\\", "/")
    for ext in (".md", ".json"):
        if find_essay(stem + ext):
            return stem + ext
    base = Path(path).stem
    for e in essay_list():
        if Path(e["file"]).stem == base:
            return e["key"]
    return None


def sync_r2_recorded(force=False):
    """Check the essayaudio bucket; mark essays recorded when audio matches."""
    if not force and time.time() - getattr(sync_r2_recorded, "_last", 0) < 30:
        return
    sync_r2_recorded._last = time.time()
    try:
        res = subprocess.run(
            ["rclone", "lsjson", R2_REMOTE, "--recursive"],
            capture_output=True, text=True, timeout=30,
        )
        if res.returncode != 0:
            return
        items = json.loads(res.stdout or "[]")
    except Exception:
        return
    state = load_state()
    changed = False
    for it in items:
        p = it.get("Path", "")
        if not p.lower().endswith(AUDIO_EXTS):
            continue
        key = essay_for_audio(p)
        if not key:
            continue
        s = state.get(key, {})
        if not s.get("recorded"):
            s["audio_path"] = p
            s["recorded"] = True
            state[key] = s
            changed = True
    if changed:
        save_state(state)


def _r2_poller():
    while True:
        try:
            sync_r2_recorded()
        except Exception:
            pass
        time.sleep(60)


PAGE = """<!DOCTYPE html>
<html data-build="v4"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Cache-Control" content="no-store, no-cache, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>Essay Studio</title>
<style>
*{box-sizing:border-box}
html,body{height:100%}
body{font-family:system-ui,-apple-system,sans-serif;background:#0D1117;color:#e8e8e8;margin:0}
@media(min-width:900px){body{display:flex;height:100vh;overflow:hidden}#main{flex:1;overflow-y:auto}}
#side{width:300px;min-width:300px;background:#161B22;border-right:1px solid #2a2f36;overflow-y:auto;display:flex;flex-direction:column}
#side .filter{padding:10px;position:sticky;top:0;background:#161B22;z-index:2}
#side input{width:100%;padding:9px;border-radius:8px;border:1px solid #333;background:#0D1117;color:#eee;font-size:15px}
#side .coll{padding:10px 12px 4px;font-weight:700;color:#D29922;font-size:12px;text-transform:uppercase;letter-spacing:.5px}
#side .ess{padding:9px 12px 9px 18px;cursor:pointer;font-size:14px;border-left:3px solid transparent}
#side .ess.on{border-left-color:#58A6FF;background:#1c232c}
#side .ess .meta{color:#6f7a86;font-size:12px;margin-top:2px}
#side .ess .rec{color:#3fb950;font-weight:700}
#side .ess .norec{color:#6f7a86}
#main{flex:1;overflow-y:auto}
.toolbar{position:sticky;top:0;background:#0D1117;z-index:2;padding:10px 22px;border-bottom:1px solid #2a2f36;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.toolbar h1{font-size:18px;margin:0;font-weight:600}
.toolbar .sub{color:#9a9a9a;font-size:12px}
.badge{display:inline-block;padding:2px 9px;border-radius:12px;font-size:11px;margin-left:6px}
.badge.rec{background:rgba(63,185,80,.15);color:#3fb950}
.badge.norec{background:rgba(139,148,158,.12);color:#8b949e}
.badge.edited{background:rgba(88,166,255,.15);color:#58a6ff}
button{background:#21262d;border:1px solid #30363d;color:#e8e8e8;padding:8px 14px;border-radius:8px;cursor:pointer;font-size:13px}
button.primary{background:#238636;border-color:#2ea043}
button.on{background:#58A6FF;border-color:#79c0ff;color:#0D1117;font-weight:600}
#msg{color:#58a6ff;font-size:12px}
#content{max-width:1200px;margin:0 auto;padding:26px 34px 90px;column-width:520px;column-gap:56px;font:19px/1.75 Georgia,'Times New Roman',serif;color:#d5d0c7}
#content.one-col{column-width:none;max-width:760px}
#content p{margin:0 0 1em}
#content h1,#content h2,#content h3,#content h4{font-family:system-ui,sans-serif;color:#fff;column-span:all}
#content h1{font-size:26px}
#content h2{font-size:22px;margin-top:.5em}
#content blockquote{color:#c9a96a;border-left:3px solid #c9a96a;margin:0 0 1em;padding-left:14px;font-style:italic}
#content .md{white-space:pre-wrap;font:16px/1.6 -apple-system,monospace;color:#9a9a9a}
#content.edit{column-width:none;column-count:1;max-width:900px}
#content.edit > div{margin-bottom:.7em}
#content.edit > div.e{margin:0;height:1em}
#content.edit [contenteditable]{outline:none;border-radius:4px;padding:2px 4px;margin:0 -4px;white-space:pre-wrap;min-height:1.2em}
#content.edit [contenteditable]:focus{background:rgba(88,166,255,.07);box-shadow:0 0 0 2px rgba(88,166,255,.4)}
#content.edit .h{font-family:system-ui,sans-serif;color:#fff;font-weight:600}
#content.edit .q{border-left:3px solid #c9a96a;padding-left:12px;color:#c9a96a;font-style:italic}
#rectick{display:none;font-size:13px;cursor:pointer;align-items:center;gap:6px;color:#9a9a9a}
#ver{max-width:900px;margin:20px auto;padding:0 20px;font-size:12px;color:#8b949e}
#ver li{margin:4px 0}
@media(max-width:900px){
  #side{width:100%;min-width:0;border-right:none;border-bottom:1px solid #2a2f36;max-height:42vh}
  body{flex-direction:column}
  #content{padding:18px 20px 80px;column-width:none;column-count:1}
}
</style></head><body>
<div id="side">
  <div class="filter"><input id="q" placeholder="search title / collection..." oninput="draw()"></div>
  <div id="list"></div>
</div>
<div id="main">
  <div class="toolbar" id="toolbar">
    <h1 id="title">Essay Studio</h1>
    <span class="sub" id="sub"></span>
    <span id="badges"></span>
    <span style="flex:1"></span>
    <span id="msg"></span>
    <label id="rectick"><input type="checkbox" id="rec" style="width:16px;height:16px" onchange="toggleRecTick()"> audio recorded</label>
    <button id="editbtn" style="display:none" onclick="enterEdit()">✎ Edit</button>
    <button id="savebtn" class="primary" style="display:none" onclick="exitEdit(true)">Save</button>
    <button id="cancelbtn" style="display:none" onclick="exitEdit(false)">Cancel</button>
    <button id="reloadbtn" style="display:none" onclick="reloadText()">Reload original</button>
  </div>
  <div id="content" class="one-col"></div>
  <div id="ver"></div>
</div>
<script>
let essays=[], state={}, orig={};
async function init(){
  essays=await (await fetch('/api/essays')).json();
  state=await (await fetch('/api/state')).json();
  draw();
  const h=location.hash.slice(1);
  if(h){const e=essays.find(x=>x.key===decodeURIComponent(h));if(e){openEssay(e);draw();}}
}
function draw(){
  const q=document.getElementById('q').value.toLowerCase();
  const list=document.getElementById('list'); list.innerHTML='';
  const groups={};
  essays.forEach(e=>{ if(e.title.toLowerCase().includes(q)||e.collection.includes(q)) (groups[e.collection]=groups[e.collection]||[]).push(e); });
  for(const coll in groups){
    const h=document.createElement('div'); h.className='coll'; h.textContent=coll+' ('+groups[coll].length+')';
    list.appendChild(h);
    groups[coll].forEach(e=>{
      const s=state[e.key]||{}; const rec=s.recorded;
      const d=document.createElement('div'); d.className='ess'+(state.current===e.key?' on':'');
      d.innerHTML=`${e.title}<div class="meta">${e.words}w · ${rec?'<span class="rec">● recorded</span>':'<span class="norec">○ no audio</span>'}${s.versions&&s.versions.length?' · ✎'+s.versions.length:''}</div>`;
      d.onclick=()=>{state.current=e.key;save();openEssay(e);location.hash=encodeURIComponent(e.key);draw();};
      list.appendChild(d);
    });
  }
  const rec=essays.filter(e=>state[e.key]?.recorded).length;
  const ed=essays.filter(e=>state[e.key]?.versions?.length).length;
  document.getElementById('sub').textContent=rec+' recorded · '+ed+' edited';
}
function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function md(text){
  return text.split(/\\n|\\n/).map(p=>{
    const t=p.trim();
    if(!t)return '';
    if(/^#{1,4}\s/.test(t)){const n=t.match(/^(#+)\s/)[1].length;return '<h'+n+'>'+esc(t.replace(/^#{1,4}\s+/,''))+'</h'+n+'>';}
    if(/^>/.test(t))return '<blockquote>'+esc(t.replace(/^>\s?/,''))+'</blockquote>';
    return '<p>'+esc(t)+'</p>';
  }).join('');
}
function blocks(text){
  const out=[];
  for(const raw of String(text||'').split('\\n')){
    const t=raw.replace(/\\r$/,'');
    if(t===''){out.push({type:'e',text:''});continue;}
    if(t.trim()===''){out.push({type:'p',text:t});continue;}
    if(/^#{1,4}\\s/.test(t)){
      const m=t.match(/^(#+)\\s+(.*)$/);
      out.push({type:'h',mark:m[1],text:m[2]});
      continue;
    }
    const qm=t.match(/^>(.*)$/);
    if(qm){out.push({type:'q',text:qm[1]});continue;}
    out.push({type:'p',text:t});
  }
  return out;
}
function renderBlocks(text,editable){
  return blocks(text).map(b=>{
    if(b.type==='e')return '<div class="e"></div>';
    const cls=b.type==='h'?'h':b.type==='q'?'q':'p';
    const att=editable?' contenteditable="true" data-mark="'+b.mark+'"':'';
    return '<div class="'+cls+'"'+att+'>'+esc(b.text)+'</div>';
  }).join('\\n');
}
function textFromBlocks(){
  const out=[];
  document.querySelectorAll('#content > div').forEach(d=>{
    const t=d.innerText.replace(/\\u00a0/g,' ').replace(/\\u200b/g,'').trim();
    if(d.classList.contains('e')){out.push('');return;}
    if(d.classList.contains('h'))out.push((d.dataset.mark||'#')+' '+t);
    else if(d.classList.contains('q'))out.push('>'+t);
    else out.push(t);
  });
  return out.join('\\n');
}
async function openEssay(e){
  state.current=e.key;
  const s=state[e.key]||{};
  document.getElementById('title').textContent=e.title;
  document.getElementById('sub').textContent=e.collection+' / '+e.file+' · '+e.words+' words';
  const edited=s.versions&&s.versions.length;
  document.getElementById('badges').innerHTML=
    `<span class="badge ${s.recorded?'rec':'norec'}">${s.recorded?'● recorded':'○ not recorded'}</span>`+
    `<span class="badge ${edited?'edited':'norec'}">${edited?'✎ '+s.versions.length+' version(s)':'✎ original'}</span>`;
  const el=document.getElementById('content');
  el.classList.remove('edit');
  const work=(s.work!==undefined&&s.work!=='')?s.work:(orig[e.key]!==undefined?orig[e.key]:null);
  if(work!==null){
    const isMd=/\\n|\\n/.test(work)&&!work.includes('<p>');
    el.innerHTML=isMd?md(work):`<div class="md">${work.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</div>`;
    el.classList.toggle('one-col', !isMd||work.length<2500);
  } else {
    fetch('/api/essay-text?key='+encodeURIComponent(e.key)).then(r=>r.json()).then(j=>{
      orig[e.key]=j.text;
      if(state.current===e.key){
        const isMd=/\\n|\\n/.test(j.text);
        el.innerHTML=isMd?md(j.text):`<div class="md">${j.text.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}</div>`;
        el.classList.toggle('one-col', !isMd||j.text.length<2500);
      }
    });
  }
  const rectick=document.getElementById('rectick');
  rectick.style.display='';
  document.getElementById('rec').checked=!!s.recorded;
  document.getElementById('editbtn').style.display='';
  document.getElementById('savebtn').style.display='none';
  document.getElementById('cancelbtn').style.display='none';
  document.getElementById('reloadbtn').style.display='none';
  renderVersions(e.key);
}
function current(){return essays.find(e=>e.key===state.current);}
function save(){
  const e=current(); if(!e)return;
  fetch('/api/state',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(state)});
}
function enterEdit(){
  const e=current(); if(!e)return;
  const load=(text)=>{
    const el=document.getElementById('content');
    el.classList.add('edit');
    el.innerHTML=renderBlocks(text,true);
    const f=el.querySelector('[contenteditable]'); if(f)f.focus();
    document.getElementById('editbtn').style.display='none';
    document.getElementById('reloadbtn').style.display='';
    document.getElementById('savebtn').style.display='';
    document.getElementById('cancelbtn').style.display='';
    document.getElementById('msg').textContent='editing in place — Save snapshots a version';
  };
  const s=state[e.key]||{};
  const work=(s.work!==undefined&&s.work!=='')?s.work:(orig[e.key]!==undefined?orig[e.key]:null);
  if(work!==null){load(work);}
  else{
    fetch('/api/essay-text?key='+encodeURIComponent(e.key)).then(r=>r.json()).then(j=>{orig[e.key]=j.text;load(j.text);});
  }
}
function exitEdit(saveIt){
  const el=document.getElementById('content');
  let text=null;
  if(saveIt){
    text=textFromBlocks();
    if(text.trim())snapshot(text);
  }
  el.classList.remove('edit');
  document.getElementById('editbtn').style.display='';
  document.getElementById('savebtn').style.display='none';
  document.getElementById('cancelbtn').style.display='none';
  document.getElementById('reloadbtn').style.display='none';
  openEssay(current());
  if(saveIt&&text)document.getElementById('content').scrollIntoView({block:'start'});
}
function renderVersions(key){
  const s=state[key]||{};
  const v=document.getElementById('ver');
  const vs=s.versions||[];
  if(!vs.length){v.innerHTML='';return;}
  v.innerHTML='<b>VERSIONS</b><ul>'+vs.map((x,i)=>
    `<li>#${i+1} · ${new Date(x.ts).toLocaleString()} · ${x.words}w — <button onclick="restore('${key}',${i})">restore</button></li>`
  ).join('')+'</ul>';
}
function snapshot(text,announce=true){
  const e=current(); const s=state[e.key]=state[e.key]||{};
  s.work=text;
  s.versions=s.versions||[];
  s.versions.push({ts:Date.now(), text:text, words:text.split(/\\s+/).filter(Boolean).length});
  document.getElementById('msg').textContent='version #'+s.versions.length+' saved';
  save(); renderVersions(e.key); draw();
  if(announce!==false)setTimeout(()=>document.getElementById('msg').textContent='',2500);
}
function restore(key,i){
  const e=essays.find(x=>x.key===key);
  const s=state[key];
  if(!s||!s.versions||!s.versions[i])return;
  s.work=s.versions[i].text;
  document.getElementById('msg').textContent='restored #'+(i+1);
  save(); openEssay(e); draw();
}
function reloadText(){
  const e=current();
  fetch('/api/essay-text?key='+encodeURIComponent(e.key)).then(r=>r.json()).then(j=>{
    orig[e.key]=j.text;
    const el=document.getElementById('content');
    if(el.classList.contains('edit'))el.innerHTML=renderBlocks(j.text,true);
    document.getElementById('msg').textContent='original loaded from disk';
    setTimeout(()=>document.getElementById('msg').textContent='',2500);
  });
}
function toggleRecTick(){
  const e=current(); if(!e)return;
  state[e.key]=state[e.key]||{};
  state[e.key].recorded=document.getElementById('rec').checked;
  save(); draw();
  const s=state[e.key];
  const edited=s.versions&&s.versions.length;
  document.getElementById('badges').innerHTML=
    `<span class="badge ${s.recorded?'rec':'norec'}">${s.recorded?'● recorded':'○ not recorded'}</span>`+
    `<span class="badge ${edited?'edited':'norec'}">${edited?'✎ '+s.versions.length+' version(s)':'✎ original'}</span>`;
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
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        self.wfile.write(body)

    def _essay(self, key):
        return find_essay(key)

    def do_GET(self):
        u = urlparse(self.path)
        p = u.path
        q = parse_qs(u.query)
        if p == "/":
            self._send(200, PAGE.encode(), "text/html")
        elif p == "/api/essays":
            self._send(200, json.dumps(essay_list()).encode())
        elif p == "/api/state":
            self._send(200, json.dumps(load_state()).encode())
        elif p == "/api/essay-text":
            key = q.get("key", [""])[0]
            e = self._essay(key)
            if not e:
                self._send(404, b"no")
                return
            self._send(200, json.dumps({"text": Path(e["path"]).read_text(errors="ignore")}).encode())
        elif p == "/audio/":
            fname = unquote(self.path[len("/audio/"):])
            fp = AUDIO_DIR / fname
            if not fp.exists():
                self._send(404, b"no audio")
                return
            data = fp.read_bytes()
            self._send(200, data, "audio/mp4")
        else:
            self._send(404, b"not found")

    def do_POST(self):
        u = urlparse(self.path)
        q = parse_qs(u.query)
        if u.path == "/api/state":
            length = int(self.headers.get("Content-Length", 0))
            state = json.loads(self.rfile.read(length))
            save_state(state)
            self._send(200, json.dumps({"ok": True}).encode())
        elif u.path == "/api/sync":
            sync_r2_recorded(force=True)
            self._send(200, json.dumps({"ok": True}).encode())
        else:
            self._send(404, b"not found")


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8701
    AUDIO_DIR.mkdir(exist_ok=True)
    threading.Thread(target=_r2_poller, daemon=True).start()
    sync_r2_recorded(force=True)
    print(f"essay studio on http://localhost:{port}")
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()


if __name__ == "__main__":
    main()
