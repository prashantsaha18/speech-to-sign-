import streamlit as st
import json

st.set_page_config(
    page_title="SignFlow Pro — Speech to Sign Language",
    page_icon="🤟",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ASL_ALPHABET = {
    "a":{"name":"A","thumb":45,"index":90,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":0},
    "b":{"name":"B","thumb":80,"index":10,"middle":10,"ring":10,"pinky":10,"spread":5,"wrist":0},
    "c":{"name":"C","thumb":30,"index":45,"middle":45,"ring":45,"pinky":45,"spread":0,"wrist":0},
    "d":{"name":"D","thumb":70,"index":10,"middle":80,"ring":80,"pinky":80,"spread":0,"wrist":0},
    "e":{"name":"E","thumb":60,"index":75,"middle":75,"ring":75,"pinky":75,"spread":0,"wrist":0},
    "f":{"name":"F","thumb":50,"index":65,"middle":10,"ring":10,"pinky":10,"spread":10,"wrist":0},
    "g":{"name":"G","thumb":20,"index":20,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":90},
    "h":{"name":"H","thumb":70,"index":20,"middle":20,"ring":90,"pinky":90,"spread":5,"wrist":90},
    "i":{"name":"I","thumb":60,"index":90,"middle":90,"ring":90,"pinky":10,"spread":0,"wrist":0},
    "j":{"name":"J","thumb":60,"index":90,"middle":90,"ring":90,"pinky":10,"spread":0,"wrist":30},
    "k":{"name":"K","thumb":30,"index":10,"middle":20,"ring":90,"pinky":90,"spread":20,"wrist":0},
    "l":{"name":"L","thumb":10,"index":10,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":0},
    "m":{"name":"M","thumb":80,"index":80,"middle":80,"ring":80,"pinky":90,"spread":0,"wrist":0},
    "n":{"name":"N","thumb":80,"index":80,"middle":80,"ring":90,"pinky":90,"spread":0,"wrist":0},
    "o":{"name":"O","thumb":30,"index":40,"middle":40,"ring":40,"pinky":40,"spread":0,"wrist":0},
    "p":{"name":"P","thumb":30,"index":20,"middle":30,"ring":90,"pinky":90,"spread":10,"wrist":180},
    "q":{"name":"Q","thumb":20,"index":20,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":180},
    "r":{"name":"R","thumb":70,"index":10,"middle":10,"ring":90,"pinky":90,"spread":-10,"wrist":0},
    "s":{"name":"S","thumb":70,"index":85,"middle":85,"ring":85,"pinky":85,"spread":0,"wrist":0},
    "t":{"name":"T","thumb":50,"index":80,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":0},
    "u":{"name":"U","thumb":70,"index":10,"middle":10,"ring":90,"pinky":90,"spread":5,"wrist":0},
    "v":{"name":"V","thumb":70,"index":10,"middle":10,"ring":90,"pinky":90,"spread":20,"wrist":0},
    "w":{"name":"W","thumb":70,"index":10,"middle":10,"ring":10,"pinky":90,"spread":15,"wrist":0},
    "x":{"name":"X","thumb":70,"index":50,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":0},
    "y":{"name":"Y","thumb":10,"index":90,"middle":90,"ring":90,"pinky":10,"spread":20,"wrist":0},
    "z":{"name":"Z","thumb":70,"index":10,"middle":90,"ring":90,"pinky":90,"spread":0,"wrist":-20},
    " ":{"name":"SPACE","thumb":10,"index":20,"middle":20,"ring":20,"pinky":20,"spread":5,"wrist":0},
}

QUICK_PHRASES = [
    ["👋 Hello","Hello"],["🙏 Thank You","Thank you"],["❓ How are you","How are you"],
    ["✅ Yes","Yes"],["❌ No","No"],["❤️ I Love You","I love you"],
    ["🆘 Help","Help me please"],["👍 Good","Good"],["😊 Nice to meet you","Nice to meet you"],
    ["🏠 Home","Home"],["🍎 Food","Food"],["💧 Water","Water"],
    ["📞 Call","Call"],["🚗 Car","Car"],["💊 Medicine","Medicine"],
    ["🏥 Hospital","Hospital"],["😴 Tired","Tired"],["😤 Sorry","Sorry"],
    ["🎉 Happy","Happy"],["😢 Sad","Sad"],["👨‍👩‍👧 Family","Family"],["🐕 Dog","Dog"],
    ["🐈 Cat","Cat"],["📚 School","School"],["💰 Money","Money"],["⏰ Time","Time"],
]

asl_json     = json.dumps(ASL_ALPHABET)
phrases_json = json.dumps(QUICK_PHRASES)

MAIN_HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Fira+Code:wght@400;500&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
:root{{
  --bg:#030308;--surface:#0b0b14;--surface2:#10101c;--surface3:#161625;
  --border:#1c1c30;--border2:#252540;--border3:#30305a;
  --accent:#6d28d9;--accent2:#8b5cf6;--accent3:#a78bfa;--accent4:#c4b5fd;
  --cyan:#0891b2;--cyan2:#06b6d4;--cyan3:#67e8f9;
  --green:#059669;--green2:#10b981;--green3:#6ee7b7;
  --rose:#be123c;--rose2:#f43f5e;--rose3:#fda4af;
  --amber:#b45309;--amber2:#f59e0b;--amber3:#fcd34d;
  --text:#eeeeff;--text2:#a8a8c8;--text3:#6060a0;
  --font:'Outfit',sans-serif;--mono:'Fira Code',monospace;
  --r:14px;--r2:10px;--r3:8px;
  --shadow:0 8px 32px rgba(0,0,0,0.6);
  --glow-accent:0 0 24px rgba(109,40,217,0.5);
}}
body.light{{
  --bg:#f0f0ff;--surface:#ffffff;--surface2:#f5f5ff;--surface3:#eeeeff;
  --border:#d0d0f0;--border2:#c0c0e8;--border3:#b0b0e0;
  --text:#1a1a3a;--text2:#4040a0;--text3:#8080b0;
}}
html,body{{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;overflow-x:hidden;transition:background .3s,color .3s}}

/* ── ANIMATED BG ── */
.bg-orbs{{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}}
.orb{{position:absolute;border-radius:50%;filter:blur(80px);opacity:.12;animation:drift 20s ease-in-out infinite}}
.orb1{{width:500px;height:500px;background:var(--accent2);top:-10%;left:-10%;animation-delay:0s}}
.orb2{{width:400px;height:400px;background:var(--cyan2);bottom:-10%;right:-10%;animation-delay:-7s}}
.orb3{{width:300px;height:300px;background:var(--rose2);top:40%;left:40%;animation-delay:-14s}}
@keyframes drift{{0%,100%{{transform:translate(0,0) scale(1)}}33%{{transform:translate(40px,-30px) scale(1.05)}}66%{{transform:translate(-30px,40px) scale(.95)}}}}

.app{{position:relative;z-index:1;display:flex;flex-direction:column;min-height:100vh}}

/* ── TOPBAR ── */
.topbar{{
  display:flex;align-items:center;justify-content:space-between;
  padding:14px 24px;border-bottom:1px solid var(--border);
  background:rgba(11,11,20,.85);backdrop-filter:blur(16px);
  position:sticky;top:0;z-index:200;
}}
body.light .topbar{{background:rgba(255,255,255,.85)}}
.logo{{display:flex;align-items:center;gap:10px;text-decoration:none}}
.logo-gem{{
  width:40px;height:40px;border-radius:12px;
  background:linear-gradient(135deg,var(--accent2),var(--cyan2));
  display:flex;align-items:center;justify-content:center;font-size:1.3rem;
  box-shadow:var(--glow-accent);animation:gem-pulse 3s ease-in-out infinite;
}}
@keyframes gem-pulse{{0%,100%{{box-shadow:0 0 16px rgba(139,92,246,.4)}}50%{{box-shadow:0 0 32px rgba(139,92,246,.8),0 0 64px rgba(6,182,212,.3)}}}}
.logo-name{{font-size:1.5rem;font-weight:800;background:linear-gradient(90deg,var(--accent4),var(--cyan3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.logo-tag{{font-family:var(--mono);font-size:.65rem;color:var(--text3);margin-left:4px;padding:2px 7px;background:var(--surface2);border:1px solid var(--border2);border-radius:99px}}
.topbar-right{{display:flex;align-items:center;gap:8px}}
.icon-btn{{
  width:34px;height:34px;border-radius:8px;border:1px solid var(--border2);
  background:var(--surface2);color:var(--text2);font-size:1rem;
  display:flex;align-items:center;justify-content:center;cursor:pointer;
  transition:all .18s;
}}
.icon-btn:hover{{background:var(--border2);color:var(--text)}}
.icon-btn.active{{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:var(--glow-accent)}}
.live-dot{{display:flex;align-items:center;gap:6px;font-family:var(--mono);font-size:.7rem;
  color:var(--green2);padding:4px 10px;background:rgba(16,185,129,.1);
  border:1px solid rgba(16,185,129,.25);border-radius:99px}}
.live-dot::before{{content:'●';animation:blink 1.6s step-end infinite}}
@keyframes blink{{50%{{opacity:.2}}}}

/* ── MAIN LAYOUT ── */
.main{{display:grid;grid-template-columns:1fr 480px;flex:1;overflow:hidden}}

/* ── LEFT ── */
.left{{padding:20px 24px;display:flex;flex-direction:column;gap:16px;overflow-y:auto;max-height:calc(100vh - 61px)}}

/* ── TABS ── */
.tabs{{display:flex;gap:4px;padding:4px;background:var(--surface);border:1px solid var(--border);border-radius:var(--r);overflow-x:auto;flex-shrink:0}}
.tab{{flex:1;min-width:max-content;padding:7px 13px;border:none;background:transparent;color:var(--text3);font-family:var(--font);font-size:.82rem;font-weight:600;border-radius:var(--r2);cursor:pointer;transition:all .18s;white-space:nowrap}}
.tab.on{{background:var(--accent);color:#fff;box-shadow:0 0 12px rgba(109,40,217,.5)}}
.tab:hover:not(.on){{background:var(--border);color:var(--text)}}
.panel{{display:none}}.panel.on{{display:flex;flex-direction:column;gap:12px}}

/* ── CARDS ── */
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--r);padding:14px 16px}}
.card-head{{font-family:var(--mono);font-size:.65rem;font-weight:500;color:var(--text3);text-transform:uppercase;letter-spacing:.1em;margin-bottom:10px;display:flex;align-items:center;gap:8px}}
.card-head::after{{content:'';flex:1;height:1px;background:var(--border)}}

/* ── TEXTAREA ── */
.ta-wrap{{position:relative}}
textarea{{width:100%;min-height:110px;padding:13px 15px 28px;
  background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r2);
  color:var(--text);font-family:var(--font);font-size:.95rem;resize:vertical;outline:none;
  transition:border-color .2s,box-shadow .2s;line-height:1.6}}
textarea:focus{{border-color:var(--accent3);box-shadow:0 0 0 3px rgba(139,92,246,.12)}}
textarea::placeholder{{color:var(--text3)}}
.char-count{{position:absolute;bottom:9px;right:11px;font-family:var(--mono);font-size:.68rem;color:var(--text3)}}

/* ── BUTTONS ── */
.btn{{display:inline-flex;align-items:center;gap:7px;padding:9px 18px;border:none;border-radius:var(--r2);
  font-family:var(--font);font-size:.85rem;font-weight:600;cursor:pointer;transition:all .18s;white-space:nowrap}}
.btn-primary{{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;box-shadow:0 4px 16px rgba(109,40,217,.35)}}
.btn-primary:hover{{transform:translateY(-1px);box-shadow:0 6px 24px rgba(109,40,217,.5)}}
.btn-primary:active{{transform:none}}
.btn-primary:disabled{{opacity:.4;cursor:not-allowed;transform:none}}
.btn-ghost{{background:var(--surface2);color:var(--text2);border:1px solid var(--border2)}}
.btn-ghost:hover{{color:var(--text);border-color:var(--border3)}}
.btn-teal{{background:rgba(6,182,212,.15);color:var(--cyan2);border:1px solid rgba(6,182,212,.3)}}
.btn-teal:hover{{background:rgba(6,182,212,.25)}}
.btn-green{{background:rgba(16,185,129,.15);color:var(--green2);border:1px solid rgba(16,185,129,.3)}}
.btn-green:hover{{background:rgba(16,185,129,.25)}}
.btn-rose{{background:rgba(244,63,94,.15);color:var(--rose2);border:1px solid rgba(244,63,94,.3)}}
.btn-rose:hover{{background:rgba(244,63,94,.25)}}
.btn-amber{{background:rgba(245,158,11,.15);color:var(--amber2);border:1px solid rgba(245,158,11,.3)}}
.btn-amber:hover{{background:rgba(245,158,11,.25)}}
.btn-row{{display:flex;gap:8px;flex-wrap:wrap;align-items:center}}

/* ── MIC ── */
.mic-zone{{display:flex;align-items:center;gap:14px;padding:14px;
  background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r)}}
#micBtn{{
  width:60px;height:60px;border-radius:50%;border:none;cursor:pointer;font-size:1.5rem;
  background:linear-gradient(135deg,var(--rose2),#ff5580);color:#fff;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  transition:all .2s;box-shadow:0 4px 16px rgba(244,63,94,.4);
}}
#micBtn.on{{animation:mic-ring 1.2s ease-in-out infinite}}
@keyframes mic-ring{{0%{{box-shadow:0 0 0 0 rgba(244,63,94,.6)}}70%{{box-shadow:0 0 0 18px rgba(244,63,94,0)}}100%{{box-shadow:0 0 0 0 rgba(244,63,94,0)}}}}
.mic-text{{flex:1}}
.mic-status{{font-weight:600;font-size:.9rem}}
.mic-hint{{font-size:.73rem;color:var(--text3);margin-top:2px}}
canvas#wave{{width:100%;height:44px;border-radius:8px;background:var(--surface3);border:1px solid var(--border);display:block}}
.live-text{{padding:10px 13px;background:var(--surface3);border-radius:var(--r3);border:1px solid var(--border);
  font-family:var(--mono);font-size:.83rem;color:var(--text3);min-height:38px;line-height:1.5}}

/* ── SPEED PRESETS ── */
.speed-presets{{display:flex;gap:6px}}
.preset{{padding:5px 13px;border-radius:99px;border:1px solid var(--border2);background:var(--surface2);
  font-size:.75rem;font-family:var(--mono);color:var(--text3);cursor:pointer;transition:all .15s}}
.preset.on{{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 0 10px rgba(109,40,217,.4)}}
.preset:hover:not(.on){{border-color:var(--border3);color:var(--text)}}
.range-row{{display:flex;align-items:center;gap:10px}}
input[type=range]{{flex:1;-webkit-appearance:none;height:4px;border-radius:4px;background:var(--border2);outline:none;cursor:pointer}}
input[type=range]::-webkit-slider-thumb{{-webkit-appearance:none;width:15px;height:15px;border-radius:50%;background:var(--accent3);cursor:pointer;box-shadow:0 0 6px var(--accent2)}}
.range-val{{font-family:var(--mono);font-size:.75rem;color:var(--accent3);min-width:48px;text-align:right}}

/* ── PHRASES GRID ── */
.phrases-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:7px}}
.phrase{{padding:8px 10px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r3);
  font-size:.78rem;cursor:pointer;transition:all .16s;text-align:left;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--text2)}}
.phrase:hover{{background:rgba(139,92,246,.12);border-color:var(--accent3);color:var(--text);transform:translateY(-1px)}}
.phrase.fav{{border-color:var(--amber2);color:var(--amber3)}}

/* ── QUIZ ── */
.quiz-card{{
  padding:20px;background:var(--surface);border:1px solid var(--border);
  border-radius:var(--r);text-align:center;
}}
.quiz-question{{font-size:3rem;font-weight:800;margin-bottom:6px;
  background:linear-gradient(135deg,var(--accent4),var(--cyan3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.quiz-prompt{{font-size:.9rem;color:var(--text2);margin-bottom:16px}}
.quiz-options{{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:12px}}
.quiz-opt{{padding:12px 8px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r2);
  font-size:1.2rem;font-weight:700;cursor:pointer;transition:all .18s;color:var(--text)}}
.quiz-opt:hover{{background:rgba(139,92,246,.15);border-color:var(--accent3)}}
.quiz-opt.correct{{background:rgba(16,185,129,.2);border-color:var(--green2);color:var(--green3)}}
.quiz-opt.wrong{{background:rgba(244,63,94,.2);border-color:var(--rose2);color:var(--rose3)}}
.quiz-score{{font-family:var(--mono);font-size:.85rem;color:var(--text2)}}
.quiz-streak{{font-size:1.1rem;color:var(--amber3);font-weight:700}}

/* ── ALPHABET ── */
.alpha-grid{{display:grid;grid-template-columns:repeat(7,1fr);gap:6px}}
.alpha-card{{aspect-ratio:1;display:flex;flex-direction:column;align-items:center;justify-content:center;
  background:var(--surface2);border:1px solid var(--border);border-radius:10px;
  cursor:pointer;transition:all .16s}}
.alpha-card:hover{{background:rgba(139,92,246,.12);border-color:var(--accent3);transform:scale(1.06)}}
.alpha-card .l{{font-size:1.3rem;font-weight:800;color:var(--accent3)}}
.alpha-card .s{{font-size:.55rem;color:var(--text3);font-family:var(--mono)}}
.alpha-card.fav-letter{{border-color:var(--amber2)}}

/* ── HISTORY ── */
.hist-list{{display:flex;flex-direction:column;gap:5px;max-height:180px;overflow-y:auto}}
.hist-item{{display:flex;align-items:center;gap:8px;padding:7px 11px;
  background:var(--surface2);border:1px solid var(--border);border-radius:var(--r3);cursor:pointer;transition:all .14s}}
.hist-item:hover{{border-color:var(--accent3)}}
.hist-txt{{flex:1;font-size:.8rem;color:var(--text2);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}
.hist-time{{font-family:var(--mono);font-size:.66rem;color:var(--text3);flex-shrink:0}}
.hist-actions{{display:flex;gap:4px;flex-shrink:0}}
.hist-icon{{font-size:.75rem;cursor:pointer;padding:2px 5px;border-radius:4px;transition:background .14s}}
.hist-icon:hover{{background:var(--border2)}}

/* ── EXPORT MODAL ── */
.modal-overlay{{position:fixed;inset:0;background:rgba(0,0,0,.7);backdrop-filter:blur(4px);z-index:300;display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .2s}}
.modal-overlay.open{{opacity:1;pointer-events:all}}
.modal{{background:var(--surface);border:1px solid var(--border2);border-radius:var(--r);padding:24px;
  width:500px;max-width:90vw;box-shadow:var(--shadow);transform:scale(.96);transition:transform .2s}}
.modal-overlay.open .modal{{transform:scale(1)}}
.modal h3{{font-size:1.1rem;font-weight:700;margin-bottom:4px}}
.modal p{{font-size:.82rem;color:var(--text2);margin-bottom:16px}}
.export-options{{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:16px}}
.export-opt{{padding:14px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r2);
  cursor:pointer;transition:all .16s;text-align:center}}
.export-opt:hover{{border-color:var(--accent3);background:rgba(139,92,246,.1)}}
.export-opt .e-icon{{font-size:1.6rem;margin-bottom:4px}}
.export-opt .e-label{{font-size:.8rem;font-weight:600;color:var(--text)}}
.export-opt .e-desc{{font-size:.7rem;color:var(--text3)}}

/* ── SETTINGS ── */
.settings-grid{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}
.setting-item{{padding:12px;background:var(--surface2);border:1px solid var(--border);border-radius:var(--r2)}}
.setting-label{{font-size:.72rem;color:var(--text3);font-family:var(--mono);text-transform:uppercase;letter-spacing:.08em;margin-bottom:8px}}
.theme-swatches{{display:flex;gap:7px;flex-wrap:wrap}}
.swatch{{width:26px;height:26px;border-radius:50%;cursor:pointer;border:2px solid transparent;transition:all .18s}}
.swatch:hover,.swatch.on{{border-color:#fff;transform:scale(1.2);box-shadow:0 0 8px rgba(255,255,255,.3)}}
.toggle-row{{display:flex;align-items:center;justify-content:space-between;gap:8px}}
.toggle{{position:relative;width:36px;height:20px;flex-shrink:0}}
.toggle input{{opacity:0;width:0;height:0;position:absolute}}
.toggle-track{{position:absolute;inset:0;background:var(--border2);border-radius:99px;cursor:pointer;transition:background .2s}}
.toggle input:checked+.toggle-track{{background:var(--accent)}}
.toggle-track::after{{content:'';position:absolute;left:3px;top:3px;width:14px;height:14px;border-radius:50%;background:#fff;transition:transform .2s;box-shadow:0 1px 3px rgba(0,0,0,.4)}}
.toggle input:checked+.toggle-track::after{{transform:translateX(16px)}}

/* ── RIGHT PANEL ── */
.right{{
  display:flex;flex-direction:column;
  border-left:1px solid var(--border);
  background:var(--surface);
  position:sticky;top:61px;height:calc(100vh - 61px);overflow:hidden;
}}
.canvas-topbar{{display:flex;align-items:center;justify-content:space-between;
  padding:10px 14px;border-bottom:1px solid var(--border)}}
.canvas-title{{font-size:.9rem;font-weight:700;background:linear-gradient(90deg,var(--accent4),var(--cyan3));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.ctrl-row{{display:flex;gap:5px}}
.ctrl{{padding:4px 10px;border:1px solid var(--border2);border-radius:6px;background:transparent;
  color:var(--text3);font-family:var(--mono);font-size:.68rem;cursor:pointer;transition:all .14s}}
.ctrl:hover,.ctrl.on{{background:rgba(139,92,246,.15);color:var(--accent3);border-color:var(--accent)}}

#handCanvas{{display:block;margin:0 auto;flex-shrink:0}}

.progress-area{{padding:8px 14px;border-top:1px solid var(--border)}}
.prog-bar{{height:3px;background:var(--border);border-radius:3px;overflow:hidden;margin-bottom:7px}}
.prog-fill{{height:100%;background:linear-gradient(90deg,var(--accent),var(--cyan2));border-radius:3px;transition:width .3s ease;width:0}}
.letter-row{{display:flex;gap:3px;overflow-x:auto;padding-bottom:2px;scrollbar-width:none}}
.letter-row::-webkit-scrollbar{{display:none}}
.lb{{flex-shrink:0;width:26px;height:26px;display:flex;align-items:center;justify-content:center;
  background:var(--surface3);border:1px solid var(--border);border-radius:5px;
  font-family:var(--mono);font-size:.7rem;font-weight:600;color:var(--text3);transition:all .15s}}
.lb.active{{background:var(--accent);color:#fff;border-color:var(--accent);box-shadow:0 0 10px rgba(109,40,217,.6);transform:scale(1.18)}}
.lb.done{{background:rgba(16,185,129,.1);color:var(--green2);border-color:rgba(16,185,129,.3)}}

.sign-info-bar{{display:flex;align-items:center;gap:11px;padding:10px 14px;border-top:1px solid var(--border)}}
.big-letter{{
  width:50px;height:50px;flex-shrink:0;border-radius:12px;
  background:linear-gradient(135deg,rgba(109,40,217,.2),rgba(6,182,212,.15));
  border:1px solid rgba(139,92,246,.35);
  display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;font-weight:800;color:var(--accent3);
}}
.sign-meta{{flex:1;min-width:0}}
.sign-name{{font-weight:700;font-size:.9rem}}
.sign-sub{{font-size:.72rem;color:var(--text3);font-family:var(--mono);margin-top:1px}}
.play-btn{{padding:7px 13px;font-size:.8rem}}

.stats-strip{{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--border)}}
.stat{{padding:8px 10px;text-align:center;border-right:1px solid var(--border)}}
.stat:last-child{{border-right:none}}
.stat-n{{font-size:1rem;font-weight:800;color:var(--accent3);font-family:var(--mono)}}
.stat-l{{font-size:.6rem;color:var(--text3);text-transform:uppercase;letter-spacing:.07em}}

/* ── TOAST ── */
#toast{{
  position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(70px);
  background:var(--surface2);border:1px solid var(--border2);border-radius:10px;
  padding:9px 18px;font-size:.84rem;box-shadow:var(--shadow);
  transition:transform .3s cubic-bezier(.34,1.56,.64,1);z-index:400;
  display:flex;align-items:center;gap:8px;
}}
#toast.show{{transform:translateX(-50%) translateY(0)}}
#toast .toast-icon{{font-size:1rem}}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{{width:4px;height:4px}}
::-webkit-scrollbar-thumb{{background:var(--border2);border-radius:4px}}

/* ── NOTIFICATIONS ── */
.notif-badge{{
  width:8px;height:8px;border-radius:50%;background:var(--rose2);
  position:absolute;top:5px;right:5px;
}}
</style>
</head>
<body>
<div class="bg-orbs">
  <div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div>
</div>
<div class="app">

<!-- ── TOPBAR ── -->
<nav class="topbar">
  <div class="logo">
    <div class="logo-gem">🤟</div>
    <span class="logo-name">SignFlow</span>
    <span class="logo-tag">PRO</span>
  </div>
  <div class="topbar-right">
    <div class="live-dot">LIVE ASR</div>
    <button class="icon-btn" onclick="openExport()" title="Export">📤</button>
    <button class="icon-btn" id="lightBtn" onclick="toggleLight()" title="Light/Dark mode">🌙</button>
    <button class="icon-btn" onclick="switchToTab('settings')" title="Settings">⚙️</button>
  </div>
</nav>

<!-- ── MAIN GRID ── -->
<div class="main">

<!-- ═══════ LEFT PANEL ═══════ -->
<div class="left">

  <!-- TABS -->
  <div class="tabs" id="tabBar">
    <button class="tab on"  onclick="switchToTab('mic')">🎙️ Mic</button>
    <button class="tab" onclick="switchToTab('type')">⌨️ Type</button>
    <button class="tab" onclick="switchToTab('phrases')">⚡ Phrases</button>
    <button class="tab" onclick="switchToTab('abc')">🔤 A–Z</button>
    <button class="tab" onclick="switchToTab('numbers')">🔢 Numbers</button>
    <button class="tab" onclick="switchToTab('builder')">🏗️ Builder</button>
    <button class="tab" onclick="switchToTab('quiz')">🧠 Quiz</button>
    <button class="tab" onclick="switchToTab('practice')">📝 Practice</button>
    <button class="tab" onclick="switchToTab('history')">🕓 History</button>
    <button class="tab" onclick="switchToTab('shortcuts')">⌨️ Keys</button>
    <button class="tab" onclick="switchToTab('settings')">⚙️ Settings</button>
  </div>

  <!-- TAB: MIC -->
  <div class="panel on" id="panel-mic">
    <div class="card-head">Voice Input</div>
    <div class="mic-zone">
      <button id="micBtn" onclick="toggleMic()">🎤</button>
      <div class="mic-text">
        <div class="mic-status" id="micStatus">Ready to listen</div>
        <div class="mic-hint" id="micHint">Chrome / Edge · Web Speech API</div>
      </div>
    </div>
    <canvas id="wave"></canvas>
    <div class="live-text" id="liveText">Transcript will appear here…</div>
    <div class="btn-row">
      <button class="btn btn-primary" id="signTransBtn" onclick="signTranscript()" disabled>▶ Sign This</button>
      <button class="btn btn-ghost" onclick="clearTrans()">✕ Clear</button>
      <button class="btn btn-teal" onclick="autoSign()" id="autoBtn">🔄 Auto-Sign</button>
    </div>
    <div class="card" style="padding:10px 14px">
      <div class="card-head">Language</div>
      <select id="langSelect" onchange="setLang()" style="width:100%;padding:7px 10px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r3);color:var(--text);font-family:var(--font);font-size:.85rem;outline:none">
        <option value="en-US">🇺🇸 English (US)</option>
        <option value="en-GB">🇬🇧 English (UK)</option>
        <option value="es-ES">🇪🇸 Spanish</option>
        <option value="fr-FR">🇫🇷 French</option>
        <option value="de-DE">🇩🇪 German</option>
        <option value="hi-IN">🇮🇳 Hindi</option>
        <option value="ja-JP">🇯🇵 Japanese</option>
        <option value="pt-BR">🇧🇷 Portuguese</option>
      </select>
      <div style="font-size:.7rem;color:var(--text3);margin-top:6px">Note: All languages are fingerspelled in ASL</div>
    </div>
  </div>

  <!-- TAB: TYPE -->
  <div class="panel" id="panel-type">
    <div class="card-head">Text Input</div>
    <div class="ta-wrap">
      <textarea id="mainInput" placeholder="Type anything… e.g. Hello, nice to meet you!" maxlength="400" oninput="onInput()"></textarea>
      <span class="char-count"><span id="charN">0</span>/400</span>
    </div>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="signFromText()">▶ Animate Signs</button>
      <button class="btn btn-ghost" onclick="clearText()">✕ Clear</button>
      <button class="btn btn-teal" onclick="copyText()">📋 Copy</button>
      <button class="btn btn-amber" onclick="saveFavorite()">⭐ Favorite</button>
    </div>
    <!-- Favorites -->
    <div id="favsSection" style="display:none">
      <div class="card-head">Saved Favorites</div>
      <div id="favList" style="display:flex;flex-direction:column;gap:5px;max-height:140px;overflow-y:auto"></div>
    </div>
  </div>

  <!-- TAB: PHRASES -->
  <div class="panel" id="panel-phrases">
    <div class="card-head">Quick Sign Phrases</div>
    <div class="phrases-grid" id="phrasesGrid"></div>
  </div>

  <!-- TAB: A–Z -->
  <div class="panel" id="panel-abc">
    <div class="card-head">Tap a letter to preview · Long-press to favorite</div>
    <div class="alpha-grid" id="alphaGrid"></div>
    <div class="btn-row">
      <button class="btn btn-primary" onclick="spellAll()">▶ Spell A–Z</button>
      <button class="btn btn-ghost" onclick="spellRandom()">🎲 Random Letter</button>
    </div>
  </div>

  <!-- TAB: NUMBERS -->
  <div class="panel" id="panel-numbers">
    <div class="card-head">ASL Number Signs (0–9)</div>
    <div class="alpha-grid" id="numGrid"></div>
    <div style="margin-top:10px">
      <div class="card-head">Count sequence</div>
      <div class="btn-row" id="numSequences"></div>
    </div>
  </div>

  <!-- TAB: BUILDER -->
  <div class="panel" id="panel-builder">
    <div class="card-head">🏗️ Sentence Builder — drag &amp; drop words</div>
    <div id="wordBank" style="display:flex;flex-wrap:wrap;gap:6px;padding:10px;background:var(--surface2);border:1px solid var(--border);border-radius:var(--r2);min-height:60px"></div>
    <div style="font-size:.72rem;color:var(--text3);margin:6px 0 2px">Drag words into your sentence:</div>
    <div id="sentenceDrop" style="display:flex;flex-wrap:wrap;gap:6px;padding:10px;background:var(--surface3);border:2px dashed var(--border2);border-radius:var(--r2);min-height:52px;transition:border-color .2s"></div>
    <div class="btn-row" style="margin-top:8px">
      <button class="btn btn-primary" onclick="signBuiltSentence()">▶ Sign Sentence</button>
      <button class="btn btn-ghost" onclick="clearBuilder()">✕ Clear</button>
      <button class="btn btn-teal" onclick="shuffleWordBank()">🔀 Shuffle</button>
    </div>
    <div style="margin-top:10px">
      <div class="card-head">Or type a word to add</div>
      <div style="display:flex;gap:8px">
        <input id="builderInput" type="text" placeholder="Type a word…" style="flex:1;padding:8px 12px;background:var(--surface2);border:1px solid var(--border2);border-radius:var(--r3);color:var(--text);font-family:var(--font);font-size:.88rem;outline:none" onkeydown="if(event.key==='Enter')addBuilderWord()">
        <button class="btn btn-ghost" onclick="addBuilderWord()">+ Add</button>
      </div>
    </div>
  </div>

  <!-- TAB: PRACTICE -->
  <div class="panel" id="panel-practice">
    <div class="card-head">📝 Practice Worksheet</div>
    <div class="card" style="padding:12px 14px">
      <div style="font-size:.85rem;font-weight:600;margin-bottom:8px">Generate a printable practice sheet</div>
      <div style="display:flex;flex-direction:column;gap:8px">
        <label style="font-size:.8rem;color:var(--text2)">Difficulty
          <select id="practiceLevel" style="margin-left:8px;padding:4px 8px;background:var(--surface2);border:1px solid var(--border2);border-radius:6px;color:var(--text);font-size:.8rem;outline:none">
            <option value="easy">Easy (A–M)</option>
            <option value="medium" selected>Medium (A–Z)</option>
            <option value="hard">Hard (A–Z + numbers)</option>
            <option value="words">Words only</option>
          </select>
        </label>
        <label style="font-size:.8rem;color:var(--text2)">Questions
          <input type="number" id="practiceCount" value="10" min="5" max="30" style="margin-left:8px;width:60px;padding:4px 8px;background:var(--surface2);border:1px solid var(--border2);border-radius:6px;color:var(--text);font-size:.8rem;outline:none">
        </label>
      </div>
      <div class="btn-row" style="margin-top:10px">
        <button class="btn btn-primary" onclick="generatePractice()">📄 Generate &amp; Export HTML</button>
        <button class="btn btn-teal" onclick="startDrillMode()">🎯 Drill Mode</button>
      </div>
    </div>
    <!-- Drill Mode -->
    <div id="drillZone" style="display:none">
      <div class="card-head" style="margin-top:10px">Drill Mode</div>
      <div style="padding:16px;background:var(--surface);border:1px solid var(--border);border-radius:var(--r);text-align:center">
        <div id="drillPrompt" style="font-size:1.8rem;font-weight:800;color:var(--accent4);margin-bottom:8px">Press Start</div>
        <div id="drillHint" style="font-size:.82rem;color:var(--text3);margin-bottom:12px">Sign this letter on the canvas</div>
        <div class="btn-row" style="justify-content:center">
          <button class="btn btn-primary" id="drillNext" onclick="nextDrill()">▶ Start</button>
          <button class="btn btn-rose" onclick="stopDrill()">■ Stop</button>
        </div>
        <div style="margin-top:10px;font-family:var(--mono);font-size:.78rem;color:var(--text3)" id="drillScore">Score: 0 / 0</div>
      </div>
    </div>
  </div>

  <!-- TAB: SHORTCUTS -->
  <div class="panel" id="panel-shortcuts">
    <div class="card-head">⌨️ Keyboard Shortcuts</div>
    <div id="shortcutList" style="display:flex;flex-direction:column;gap:6px"></div>
    <div style="margin-top:14px">
      <div class="card-head">About SignFlow Pro</div>
      <div style="font-size:.82rem;color:var(--text2);line-height:1.7">
        <b>SignFlow Pro</b> converts speech &amp; text into animated American Sign Language (ASL) fingerspelling.<br><br>
        <b>Pipeline:</b> Microphone → Web Speech API → Text → ASL pose sequence → Canvas hand renderer<br><br>
        <b>Accessibility:</b> Designed to bridge hearing and Deaf communities with real-time, browser-native translation.<br><br>
        <span style="font-family:var(--mono);font-size:.72rem;color:var(--text3)">v3.0 · Built with Streamlit + Vanilla JS</span>
      </div>
    </div>
  </div>
  <div class="panel" id="panel-quiz">
    <div class="card-head">ASL Quiz — Learn Fingerspelling</div>
    <div class="quiz-card">
      <div class="quiz-question" id="qLetter">?</div>
      <div class="quiz-prompt" id="qPrompt">Which letter is being shown?</div>
      <div class="quiz-options" id="qOptions"></div>
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px">
        <div class="quiz-score">Score: <b id="qScore">0</b> / <b id="qTotal">0</b> &nbsp;|&nbsp; <span class="quiz-streak" id="qStreak">🔥 0</span></div>
        <div class="btn-row">
          <button class="btn btn-ghost btn" onclick="newQuestion()">⏭ Skip</button>
          <button class="btn btn-rose btn" onclick="resetQuiz()">↺ Reset</button>
        </div>
      </div>
    </div>
    <div id="quizMode" style="margin-top:8px">
      <div class="card-head">Mode</div>
      <div class="btn-row">
        <button class="btn btn-ghost" id="qmodeRead" onclick="setQMode('read')">👁 Show Sign → Guess Letter</button>
        <button class="btn btn-ghost" id="qmodeType" onclick="setQMode('type')">⌨️ See Letter → Type Sign</button>
      </div>
    </div>
  </div>

  <!-- TAB: HISTORY -->
  <div class="panel" id="panel-history">
    <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px">
      <div class="card-head" style="margin-bottom:0">Recent Translations</div>
      <button class="btn btn-rose btn" style="padding:4px 10px;font-size:.72rem" onclick="clearHistory()">✕ Clear All</button>
    </div>
    <div class="hist-list" id="histList"><div style="font-size:.82rem;color:var(--text3);text-align:center;padding:20px">No history yet</div></div>
    <div class="btn-row" style="margin-top:8px">
      <button class="btn btn-teal" onclick="exportHistory()">📤 Export History</button>
    </div>
  </div>

  <!-- TAB: SETTINGS -->
  <div class="panel" id="panel-settings">
    <div class="card-head">Preferences</div>
    <div class="settings-grid">
      <div class="setting-item">
        <div class="setting-label">Hand Theme</div>
        <div class="theme-swatches" id="swatches"></div>
      </div>
      <div class="setting-item">
        <div class="setting-label">Render Style</div>
        <div class="btn-row">
          <button class="btn btn-ghost" id="r3d" onclick="setRender('3d')" style="font-size:.78rem;padding:6px 12px">3D</button>
          <button class="btn btn-ghost" id="rflat" onclick="setRender('flat')" style="font-size:.78rem;padding:6px 12px">Flat</button>
          <button class="btn btn-ghost" id="rwire" onclick="setRender('wire')" style="font-size:.78rem;padding:6px 12px">Wire</button>
        </div>
      </div>
      <div class="setting-item">
        <div class="setting-label">Options</div>
        <div style="display:flex;flex-direction:column;gap:8px">
          <div class="toggle-row">
            <span style="font-size:.82rem">Mirror hand</span>
            <label class="toggle"><input type="checkbox" id="togMirror" onchange="settings.mirror=this.checked"><span class="toggle-track"></span></label>
          </div>
          <div class="toggle-row">
            <span style="font-size:.82rem">Show labels</span>
            <label class="toggle"><input type="checkbox" id="togLabels" checked onchange="settings.labels=this.checked"><span class="toggle-track"></span></label>
          </div>
          <div class="toggle-row">
            <span style="font-size:.82rem">Auto-sign mic</span>
            <label class="toggle"><input type="checkbox" id="togAutoSign" onchange="settings.autoSign=this.checked"><span class="toggle-track"></span></label>
          </div>
          <div class="toggle-row">
            <span style="font-size:.82rem">Sound effects</span>
            <label class="toggle"><input type="checkbox" id="togSound" onchange="settings.sound=this.checked"><span class="toggle-track"></span></label>
          </div>
        </div>
      </div>
      <div class="setting-item">
        <div class="setting-label">Canvas Size</div>
        <div class="btn-row">
          <button class="btn btn-ghost" onclick="setCanvasSize(380,310)" style="font-size:.78rem;padding:6px 10px">S</button>
          <button class="btn btn-ghost" onclick="setCanvasSize(460,370)" style="font-size:.78rem;padding:6px 10px">M</button>
          <button class="btn btn-ghost" onclick="setCanvasSize(540,430)" style="font-size:.78rem;padding:6px 10px">L</button>
        </div>
      </div>
    </div>
  </div>

  <!-- SPEED (always visible) -->
  <div class="card">
    <div class="card-head">Animation Speed</div>
    <div class="speed-presets" id="presets">
      <button class="preset" onclick="setPreset(200)">⚡ Fast</button>
      <button class="preset on" onclick="setPreset(550)">▶ Normal</button>
      <button class="preset" onclick="setPreset(900)">🐢 Slow</button>
      <button class="preset" onclick="setPreset(1400)">📖 Study</button>
    </div>
    <div class="range-row" style="margin-top:8px">
      <span style="font-size:.75rem;color:var(--text3)">ms/sign</span>
      <input type="range" id="speedRange" min="100" max="1600" value="550" oninput="onSpeedRange()">
      <span class="range-val" id="speedLabel">550ms</span>
    </div>
  </div>

</div><!-- /left -->

<!-- ═══════ RIGHT PANEL ═══════ -->
<div class="right">
  <div class="canvas-topbar">
    <span class="canvas-title">Hand Avatar</span>
    <div class="ctrl-row">
      <button class="ctrl on" id="c3d" onclick="setRender('3d')">3D</button>
      <button class="ctrl" id="cflat" onclick="setRender('flat')">Flat</button>
      <button class="ctrl" id="cwire" onclick="setRender('wire')">Wire</button>
      <button class="ctrl" id="cmirror" onclick="toggleMirror()">↔</button>
      <button class="ctrl" onclick="screenshotCanvas()">📷</button>
    </div>
  </div>

  <canvas id="handCanvas" width="460" height="360"></canvas>

  <div class="progress-area">
    <div class="prog-bar"><div class="prog-fill" id="progFill"></div></div>
    <div class="letter-row" id="letterRow"></div>
  </div>

  <div class="sign-info-bar">
    <div class="big-letter" id="bigLetter">—</div>
    <div class="sign-meta">
      <div class="sign-name" id="signName">Idle</div>
      <div class="sign-sub" id="signSub">Start speaking or type text</div>
    </div>
    <button class="btn btn-primary play-btn" id="playPause" onclick="togglePause()" style="display:none">⏸</button>
  </div>

  <div class="stats-strip">
    <div class="stat"><div class="stat-n" id="sSigns">0</div><div class="stat-l">Signs</div></div>
    <div class="stat"><div class="stat-n" id="sWords">0</div><div class="stat-l">Words</div></div>
    <div class="stat"><div class="stat-n" id="sAcc">—</div><div class="stat-l">Accuracy</div></div>
    <div class="stat"><div class="stat-n" id="sWPM">—</div><div class="stat-l">WPM</div></div>
  </div>
</div>

</div><!-- /main -->
</div><!-- /app -->

<!-- ── EXPORT MODAL ── -->
<div class="modal-overlay" id="exportModal" onclick="closeExport(event)">
  <div class="modal" onclick="event.stopPropagation()">
    <h3>📤 Export / Share</h3>
    <p>Choose an export format for your sign session</p>
    <div class="export-options">
      <div class="export-opt" onclick="doExport('txt')">
        <div class="e-icon">📄</div>
        <div class="e-label">Plain Text</div>
        <div class="e-desc">History as .txt file</div>
      </div>
      <div class="export-opt" onclick="doExport('json')">
        <div class="e-icon">🔧</div>
        <div class="e-label">JSON Data</div>
        <div class="e-desc">Full pose sequence data</div>
      </div>
      <div class="export-opt" onclick="doExport('csv')">
        <div class="e-icon">📊</div>
        <div class="e-label">CSV Log</div>
        <div class="e-desc">Timestamped history</div>
      </div>
      <div class="export-opt" onclick="doExport('png')">
        <div class="e-icon">🖼️</div>
        <div class="e-label">Screenshot</div>
        <div class="e-desc">Current canvas frame</div>
      </div>
    </div>
    <div class="btn-row">
      <button class="btn btn-ghost" onclick="closeExport()">Cancel</button>
    </div>
  </div>
</div>

<div id="toast"><span class="toast-icon" id="toastIcon">✓</span><span id="toastMsg"></span></div>

<script>
// ══════════════════════════════════════════════════════════════════════════════
// DATA
// ══════════════════════════════════════════════════════════════════════════════
const ASL = {asl_json};
const PHRASES = {phrases_json};

const THEMES = [
  {{id:'violet', hand:'#8b5cf6', glow:'rgba(139,92,246,.5)',  skin:'rgba(139,92,246,.07)'}},
  {{id:'cyan',   hand:'#06b6d4', glow:'rgba(6,182,212,.5)',   skin:'rgba(6,182,212,.07)'}},
  {{id:'rose',   hand:'#f43f5e', glow:'rgba(244,63,94,.5)',   skin:'rgba(244,63,94,.07)'}},
  {{id:'amber',  hand:'#f59e0b', glow:'rgba(245,158,11,.5)',  skin:'rgba(245,158,11,.07)'}},
  {{id:'green',  hand:'#10b981', glow:'rgba(16,185,129,.5)',  skin:'rgba(16,185,129,.07)'}},
  {{id:'white',  hand:'#d4d4ff', glow:'rgba(212,212,255,.3)', skin:'rgba(212,212,255,.04)'}},
  {{id:'gold',   hand:'#fbbf24', glow:'rgba(251,191,36,.5)',  skin:'rgba(251,191,36,.07)'}},
  {{id:'pink',   hand:'#ec4899', glow:'rgba(236,72,153,.5)',  skin:'rgba(236,72,153,.07)'}},
];

const settings = {{ mirror:false, labels:true, autoSign:false, sound:false, render:'3d' }};
let theme = THEMES[0];
let speedMs = 550;

// ══════════════════════════════════════════════════════════════════════════════
// CANVAS & ANIMATION
// ══════════════════════════════════════════════════════════════════════════════
let canvas = document.getElementById('handCanvas');
let ctx = canvas.getContext('2d');
let W = canvas.width, H = canvas.height;
let PALM = {{x:W/2, y:H*.70}};

const FBASES = [
  {{x:PALM.x-72,y:PALM.y-28}},
  {{x:PALM.x-40,y:PALM.y-82}},
  {{x:PALM.x-8, y:PALM.y-90}},
  {{x:PALM.x+24,y:PALM.y-84}},
  {{x:PALM.x+55,y:PALM.y-72}},
];
const FLENS = [[36,26,20],[42,28,22],[46,30,22],[40,27,20],[28,20,15]];

let curPose = {{thumb:20,index:20,middle:20,ring:20,pinky:20,spread:5,wrist:0}};
let tgtPose = {{...curPose}};
let animT = 1.0;

function lerp(a,b,t){{return a+(b-a)*Math.min(t,1)}}
function lerpPose(p1,p2,t){{
  const k=['thumb','index','middle','ring','pinky','spread','wrist'],o={{}};
  k.forEach(k=>o[k]=lerp(p1[k],p2[k],t));return o;
}}

function bases(){{
  return settings.mirror ? FBASES.map(b=>( {{x:W-b.x,y:b.y}} )) : FBASES;
}}

function drawFinger(base,segs,bend,sp,isThumb){{
  let x=base.x+sp,y=base.y;
  let angle=(isThumb?-30:-90)*Math.PI/180;
  const bendR=(bend/90)*68*Math.PI/180;
  ctx.beginPath(); ctx.moveTo(x,y);
  const joints=[];
  for(let i=0;i<segs.length;i++){{
    if(i>0) angle+=bendR;
    const nx=x+Math.cos(angle)*segs[i], ny=y+Math.sin(angle)*segs[i];
    ctx.lineTo(nx,ny);
    joints.push({{x:nx,y:ny,r:i===segs.length-1?4:5.5}});
    x=nx;y=ny;
  }}
  const r=settings.render;
  if(r==='3d'){{
    ctx.strokeStyle='rgba(0,0,0,.3)';ctx.lineWidth=13;ctx.lineCap='round';ctx.lineJoin='round';ctx.stroke();
  }}
  if(r==='wire'){{
    ctx.strokeStyle=theme.hand+'88';ctx.lineWidth=1.5;ctx.lineCap='round';ctx.lineJoin='round';ctx.stroke();
  }} else {{
    ctx.strokeStyle=theme.hand;ctx.lineWidth=r==='3d'?9:7;ctx.lineCap='round';ctx.lineJoin='round';ctx.stroke();
  }}
  joints.forEach(j=>{{
    if(r==='wire'){{
      ctx.beginPath();ctx.arc(j.x,j.y,j.r,0,Math.PI*2);ctx.strokeStyle=theme.hand;ctx.lineWidth=1.5;ctx.stroke();
    }} else if(r==='3d'){{
      const g=ctx.createRadialGradient(j.x-1,j.y-1,0,j.x,j.y,j.r+2);
      g.addColorStop(0,'rgba(255,255,255,.45)');g.addColorStop(1,theme.hand+'88');
      ctx.beginPath();ctx.arc(j.x,j.y,j.r+1.5,0,Math.PI*2);ctx.fillStyle=g;ctx.fill();
    }} else {{
      ctx.beginPath();ctx.arc(j.x,j.y,j.r,0,Math.PI*2);ctx.fillStyle=theme.hand+'cc';ctx.fill();
    }}
  }});
}}

function drawScene(pose){{
  ctx.clearRect(0,0,W,H);
  const bg=ctx.createRadialGradient(PALM.x,PALM.y,10,PALM.x,PALM.y,190);
  bg.addColorStop(0,theme.skin);bg.addColorStop(1,'transparent');
  ctx.fillStyle=bg;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(255,255,255,.02)';ctx.lineWidth=1;
  for(let xi=0;xi<W;xi+=30){{ctx.beginPath();ctx.moveTo(xi,0);ctx.lineTo(xi,H);ctx.stroke()}}
  for(let yi=0;yi<H;yi+=30){{ctx.beginPath();ctx.moveTo(0,yi);ctx.lineTo(W,yi);ctx.stroke()}}

  if(settings.render==='3d'){{
    const ps=ctx.createRadialGradient(PALM.x-10,-8+PALM.y,0,PALM.x,PALM.y,72);
    ps.addColorStop(0,theme.hand+'2a');ps.addColorStop(1,'transparent');
    ctx.beginPath();ctx.ellipse(PALM.x,PALM.y,62,70,0,0,Math.PI*2);ctx.fillStyle=ps;ctx.fill();
    ctx.strokeStyle=theme.hand+'22';ctx.lineWidth=1.2;ctx.stroke();
  }}

  const bends=[pose.thumb,pose.index,pose.middle,pose.ring,pose.pinky];
  const sp=pose.spread||0;
  const spreads=[sp*-2.4,sp*-.7,0,sp*.8,sp*1.9];
  const bs=bases();
  for(let i=0;i<5;i++) drawFinger(bs[i],FLENS[i],bends[i],spreads[i],i===0);

  ctx.beginPath();
  for(let i=1;i<5;i++){{const b=bs[i];i===1?ctx.moveTo(b.x,b.y+5):ctx.lineTo(b.x,b.y+5)}}
  ctx.strokeStyle=theme.hand+'44';ctx.lineWidth=settings.render==='3d'?8:6;ctx.lineCap='round';ctx.stroke();

  const glow=ctx.createRadialGradient(PALM.x,PALM.y,40,PALM.x,PALM.y,150);
  glow.addColorStop(0,theme.glow.replace('.5','.1'));glow.addColorStop(1,'transparent');
  ctx.fillStyle=glow;ctx.fillRect(0,0,W,H);
}}

const LERP=.046;
function animFrame(){{
  if(!paused) animT=Math.min(animT+LERP,1);
  drawScene(lerpPose(curPose,tgtPose,animT));
  requestAnimationFrame(animFrame);
}}
requestAnimationFrame(animFrame);

// ══════════════════════════════════════════════════════════════════════════════
// SIGN QUEUE
// ══════════════════════════════════════════════════════════════════════════════
let queue=[],playing=false,paused=false,qIdx=0,qTotal=0;
let totalSigns=0,totalWords=0,sessionStart=Date.now();
let signStartTime=null;

function startSigning(text){{
  if(!text.trim())return;
  queue=[];
  const chars=text.toLowerCase().replace(/[^a-z ]/g,'');
  const labels=[];
  for(const c of chars){{
    if(!ASL[c])continue;
    queue.push({{pose:ASL[c],label:c===' '?'·':c.toUpperCase()}});
    labels.push(c===' '?'·':c.toUpperCase());
  }}
  if(!queue.length)return;
  qTotal=queue.length;qIdx=0;
  totalWords+=(text.match(/\\S+/g)||[]).length;
  signStartTime=Date.now();
  paused=false;
  if(settings.labels){{
    const row=document.getElementById('letterRow');
    row.innerHTML=labels.map((l,i)=>`<span class="lb" data-i="${{i}}">${{l}}</span>`).join('');
  }}
  document.getElementById('progFill').style.width='0%';
  document.getElementById('playPause').style.display='flex';
  document.getElementById('playPause').textContent='⏸';
  addHistory(text);
  if(!playing) processQ();
}}

function processQ(){{
  if(paused){{setTimeout(()=>{{if(!paused)processQ()}},80);return}}
  if(!queue.length){{
    playing=false;
    document.getElementById('playPause').style.display='none';
    document.getElementById('signSub').textContent='✓ Completed';
    document.getElementById('progFill').style.width='100%';
    updateWPM();
    return;
  }}
  playing=true;
  const {{pose,label}}=queue.shift();
  curPose=lerpPose(curPose,tgtPose,animT);
  tgtPose=pose;animT=0;
  totalSigns++;
  document.getElementById('sSigns').textContent=totalSigns;
  document.getElementById('sWords').textContent=totalWords;
  const done=qTotal-queue.length-1;
  document.getElementById('progFill').style.width=(done/qTotal*100)+'%';
  document.querySelectorAll('.lb').forEach((b,i)=>{{
    b.classList.toggle('done',i<qIdx);
    b.classList.toggle('active',i===qIdx);
    if(i===qIdx)b.scrollIntoView({{behavior:'smooth',block:'nearest',inline:'center'}});
  }});
  qIdx++;
  document.getElementById('bigLetter').textContent=label;
  document.getElementById('signName').textContent=label==='·'?'Word Gap':'Letter '+label;
  document.getElementById('signSub').textContent=label==='·'?'Pause between words…':'ASL Fingerspell: '+label;
  if(settings.sound) playClick();
  setTimeout(processQ,speedMs);
}}

function togglePause(){{
  paused=!paused;
  document.getElementById('playPause').textContent=paused?'▶':'⏸';
  if(!paused) processQ();
}}

function updateWPM(){{
  if(!signStartTime||!totalWords)return;
  const mins=(Date.now()-signStartTime)/60000;
  const wpm=Math.round(totalWords/mins);
  document.getElementById('sWPM').textContent=wpm;
}}

// ══════════════════════════════════════════════════════════════════════════════
// TABS
// ══════════════════════════════════════════════════════════════════════════════
const tabNames=['mic','type','phrases','abc','numbers','builder','quiz','practice','history','shortcuts','settings'];

// ══════════════════════════════════════════════════════════════════════════════
// NUMBER SIGNS
// ══════════════════════════════════════════════════════════════════════════════
const NUM_POSES = {{
  '0':{{thumb:30,index:40,middle:40,ring:40,pinky:40,spread:0,wrist:0}},
  '1':{{thumb:70,index:10,middle:90,ring:90,pinky:90,spread:0,wrist:0}},
  '2':{{thumb:70,index:10,middle:10,ring:90,pinky:90,spread:20,wrist:0}},
  '3':{{thumb:30,index:10,middle:10,ring:90,pinky:90,spread:10,wrist:0}},
  '4':{{thumb:70,index:10,middle:10,ring:10,pinky:10,spread:12,wrist:0}},
  '5':{{thumb:10,index:10,middle:10,ring:10,pinky:10,spread:14,wrist:0}},
  '6':{{thumb:30,index:10,middle:10,ring:10,pinky:60,spread:12,wrist:0}},
  '7':{{thumb:30,index:10,middle:10,ring:60,pinky:90,spread:10,wrist:0}},
  '8':{{thumb:30,index:10,middle:60,ring:90,pinky:90,spread:8,wrist:0}},
  '9':{{thumb:50,index:65,middle:90,ring:90,pinky:90,spread:0,wrist:0}},
}};

function buildNumGrid(){{
  const g=document.getElementById('numGrid');
  if(!g||g.children.length)return;
  '0123456789'.split('').forEach(n=>{{
    const c=document.createElement('div');
    c.className='alpha-card';
    c.innerHTML=`<span class="l" style="color:var(--cyan3)">${{n}}</span><span class="s">ASL #</span>`;
    c.onclick=()=>{{
      curPose=lerpPose(curPose,tgtPose,animT);tgtPose=NUM_POSES[n];animT=0;
      document.getElementById('bigLetter').textContent=n;
      document.getElementById('signName').textContent='Number '+n;
      document.getElementById('signSub').textContent='ASL number sign';
    }};
    g.appendChild(c);
  }});
  // Sequence buttons
  const sb=document.getElementById('numSequences');
  [['Count 1–5','12345'],['Count 1–10','1234567890'],['Phone','555'],['Year','2024']].forEach(([lbl,seq])=>{{
    const b=document.createElement('button');
    b.className='btn btn-teal';b.style.fontSize='.78rem';b.textContent=lbl;
    b.onclick=()=>{{
      const q=[],labs=[];
      for(const ch of seq){{if(NUM_POSES[ch]){{q.push({{pose:NUM_POSES[ch],label:ch}});labs.push(ch)}}}}
      queue=q;qTotal=q.length;qIdx=0;paused=false;
      document.getElementById('progFill').style.width='0%';
      if(settings.labels){{document.getElementById('letterRow').innerHTML=labs.map((l,i)=>`<span class="lb" data-i="${{i}}">${{l}}</span>`).join('')}}
      document.getElementById('playPause').style.display='flex';
      if(!playing) processQ();
    }};
    sb.appendChild(b);
  }});
}}

// ══════════════════════════════════════════════════════════════════════════════
// SENTENCE BUILDER
// ══════════════════════════════════════════════════════════════════════════════
const WORD_BANK_DEFAULT=['Hello','My','Name','Is','Nice','To','Meet','You','I','Love','Help','Please','Thank','Good','Bad','Yes','No','Home','Work','School','Food','Water','Happy','Sad','Time','Today','Tomorrow'];
let wordBankItems=[...WORD_BANK_DEFAULT];
let builtSentence=[];

function buildWordBank(){{
  const wb=document.getElementById('wordBank');
  if(!wb)return;
  wb.innerHTML='';
  wordBankItems.forEach(w=>{{
    const chip=document.createElement('div');
    chip.style.cssText='padding:5px 12px;background:var(--surface3);border:1px solid var(--border2);border-radius:20px;font-size:.82rem;cursor:grab;user-select:none;transition:all .15s;color:var(--text)';
    chip.textContent=w;chip.draggable=true;
    chip.addEventListener('dragstart',e=>{{e.dataTransfer.setData('text',w);chip.style.opacity='.4'}});
    chip.addEventListener('dragend',()=>chip.style.opacity='1');
    chip.ondblclick=()=>{{addWordToSentence(w)}};
    wb.appendChild(chip);
  }});
  const drop=document.getElementById('sentenceDrop');
  drop.addEventListener('dragover',e=>{{e.preventDefault();drop.style.borderColor='var(--accent3)'}});
  drop.addEventListener('dragleave',()=>drop.style.borderColor='var(--border2)');
  drop.addEventListener('drop',e=>{{
    e.preventDefault();drop.style.borderColor='var(--border2)';
    addWordToSentence(e.dataTransfer.getData('text'));
  }});
}}

function addWordToSentence(w){{
  builtSentence.push(w);
  const drop=document.getElementById('sentenceDrop');
  const chip=document.createElement('div');
  chip.style.cssText='display:flex;align-items:center;gap:5px;padding:5px 10px;background:rgba(139,92,246,.2);border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent4)';
  chip.innerHTML=`${{w}} <span style="cursor:pointer;font-size:.7rem;color:var(--rose2)" onclick="removeBuilderWord(this,'${{w}}')">✕</span>`;
  drop.appendChild(chip);
}}

function removeBuilderWord(el,w){{
  const i=builtSentence.lastIndexOf(w);
  if(i>=0)builtSentence.splice(i,1);
  el.parentElement.remove();
}}

function signBuiltSentence(){{
  if(builtSentence.length) startSigning(builtSentence.join(' '));
}}
function clearBuilder(){{
  builtSentence=[];document.getElementById('sentenceDrop').innerHTML='';
}}
function shuffleWordBank(){{
  wordBankItems=[...WORD_BANK_DEFAULT].sort(()=>Math.random()-.5);buildWordBank();
}}
function addBuilderWord(){{
  const inp=document.getElementById('builderInput');
  const w=inp.value.trim();
  if(w){{wordBankItems.unshift(w);buildWordBank();inp.value=''}};
}}

// ══════════════════════════════════════════════════════════════════════════════
// PRACTICE / DRILL MODE
// ══════════════════════════════════════════════════════════════════════════════
let drillActive=false,drillIdx=0,drillSeq=[],drillCorrect=0,drillTotal=0,drillTimer=null;

function startDrillMode(){{
  document.getElementById('drillZone').style.display='block';
  drillSeq='abcdefghijklmnopqrstuvwxyz'.split('').sort(()=>Math.random()-.5);
  drillIdx=0;drillCorrect=0;drillTotal=0;drillActive=true;
  nextDrill();
}}
function nextDrill(){{
  if(drillIdx>=drillSeq.length){{
    document.getElementById('drillPrompt').textContent='Done!';
    document.getElementById('drillHint').textContent='Score: '+drillCorrect+'/'+drillTotal;
    clearTimeout(drillTimer);drillActive=false;return;
  }}
  const ch=drillSeq[drillIdx++];
  curPose=lerpPose(curPose,tgtPose,animT);tgtPose=ASL[ch];animT=0;
  document.getElementById('drillPrompt').textContent='?';
  document.getElementById('drillHint').textContent='What letter is this?';
  document.getElementById('bigLetter').textContent='?';
  document.getElementById('signName').textContent='Drill in progress…';
  // Auto-reveal after 3 seconds
  clearTimeout(drillTimer);
  drillTimer=setTimeout(()=>{{
    drillTotal++;
    document.getElementById('drillPrompt').textContent=ch.toUpperCase();
    document.getElementById('drillHint').textContent='ASL Letter '+ch.toUpperCase();
    document.getElementById('drillScore').textContent='Seen: '+drillIdx+' / '+drillSeq.length;
    document.getElementById('bigLetter').textContent=ch.toUpperCase();
  }},2800);
}}
function stopDrill(){{
  clearTimeout(drillTimer);drillActive=false;
  document.getElementById('drillZone').style.display='none';
}}

function generatePractice(){{
  const level=document.getElementById('practiceLevel').value;
  const count=parseInt(document.getElementById('practiceCount').value)||10;
  let pool=[];
  if(level==='easy') pool='abcdefghijklm'.split('');
  else if(level==='medium') pool='abcdefghijklmnopqrstuvwxyz'.split('');
  else if(level==='hard') pool=[...'abcdefghijklmnopqrstuvwxyz'.split(''),...'0123456789'.split('')];
  else pool=['hello','thank you','good','yes','no','help','love','please','home','food','water','happy'];
  const qs=Array.from({{length:count}},()=>pool[Math.floor(Math.random()*pool.length)]);
  const html=`<!DOCTYPE html><html><head><meta charset="UTF-8">
<title>SignFlow Practice Sheet</title>
<style>
body{{font-family:Arial,sans-serif;max-width:800px;margin:40px auto;padding:20px;color:#111}}
h1{{color:#6d28d9;margin-bottom:4px}}p{{color:#666;margin-bottom:24px}}
.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.q{{border:2px solid #e5e7eb;border-radius:10px;padding:16px;page-break-inside:avoid}}
.q-num{{font-size:.75rem;color:#9ca3af;margin-bottom:8px}}
.q-letter{{font-size:2.2rem;font-weight:800;color:#6d28d9;margin-bottom:8px}}
.answer-line{{height:2px;background:#e5e7eb;margin-top:12px}}
.answer-label{{font-size:.68rem;color:#9ca3af;margin-top:4px}}
@media print{{body{{margin:20px}}}}
</style></head><body>
<h1>🤟 SignFlow ASL Practice Sheet</h1>
<p>Practice worksheet — Generated ${{new Date().toLocaleDateString()}} · Difficulty: ${{level}}</p>
<div class="grid">
${{qs.map((q,i)=>`<div class="q"><div class="q-num">Question ${{i+1}}</div>
<div class="q-letter">${{q.toUpperCase()}}</div>
<div style="font-size:.8rem;color:#6b7280">Describe the ASL sign for this letter/word</div>
<div class="answer-line"></div><div class="answer-label">Your answer</div></div>`).join('')}}
</div>
<div style="margin-top:30px;font-size:.75rem;color:#9ca3af;text-align:center">SignFlow Pro · ASL Fingerspelling Practice</div>
</body></html>`;
  const blob=new Blob([html],{{type:'text/html'}});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download='asl-practice-sheet.html';a.click();
  showToast('📄','Practice sheet exported!');
}}

// ══════════════════════════════════════════════════════════════════════════════
// CONFETTI (quiz streak celebration)
// ══════════════════════════════════════════════════════════════════════════════
function confetti(){{
  const colors=['#8b5cf6','#06b6d4','#f43f5e','#10b981','#f59e0b','#ec4899'];
  for(let i=0;i<60;i++){{
    const el=document.createElement('div');
    el.style.cssText=`
      position:fixed;top:-10px;left:${{Math.random()*100}}vw;
      width:${{6+Math.random()*8}}px;height:${{6+Math.random()*8}}px;
      background:${{colors[Math.floor(Math.random()*colors.length)]}};
      border-radius:${{Math.random()>.5?'50%':'2px'}};
      pointer-events:none;z-index:9999;opacity:1;
      animation:confettiFall ${{1.5+Math.random()*2}}s linear forwards;
      animation-delay:${{Math.random()*.4}}s;
    `;
    document.body.appendChild(el);
    setTimeout(()=>el.remove(),4000);
  }}
  if(!document.getElementById('confettiStyle')){{
    const s=document.createElement('style');s.id='confettiStyle';
    s.textContent='@keyframes confettiFall{{to{{transform:translateY(110vh) rotate(720deg);opacity:0}}}}';
    document.head.appendChild(s);
  }}
}}

// ══════════════════════════════════════════════════════════════════════════════
// KEYBOARD SHORTCUTS PANEL
// ══════════════════════════════════════════════════════════════════════════════
function buildShortcuts(){{
  const shortcuts=[
    ['Space','Pause / Resume signing'],
    ['M','Toggle microphone'],
    ['R','Show random letter sign'],
    ['Enter','Sign text from Type tab'],
    ['A–Z keys','Preview that letter\'s sign'],
    ['Ctrl+Enter','Sign text (in textarea)'],
    ['Esc','Close modals'],
  ];
  const list=document.getElementById('shortcutList');
  if(!list||list.children.length)return;
  shortcuts.forEach(([key,desc])=>{{
    const row=document.createElement('div');
    row.style.cssText='display:flex;align-items:center;gap:10px;padding:8px 12px;background:var(--surface2);border:1px solid var(--border);border-radius:8px';
    row.innerHTML=`<kbd style="padding:3px 9px;background:var(--surface3);border:1px solid var(--border2);border-radius:5px;font-family:var(--mono);font-size:.75rem;color:var(--accent3);white-space:nowrap">${{key}}</kbd><span style="font-size:.82rem;color:var(--text2)">${{desc}}</span>`;
    list.appendChild(row);
  }});
}}


function switchToTab(id){{
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('on'));
  document.querySelectorAll('.tab').forEach((b,i)=>b.classList.toggle('on',tabNames[i]===id));
  const p=document.getElementById('panel-'+id);
  if(p) p.classList.add('on');
  if(id==='quiz') initQuiz();
  if(id==='numbers') buildNumGrid();
  if(id==='builder') buildWordBank();
  if(id==='shortcuts') buildShortcuts();
}}

// ══════════════════════════════════════════════════════════════════════════════
// THEMES & RENDER
// ══════════════════════════════════════════════════════════════════════════════
function buildSwatches(){{
  const wrap=document.getElementById('swatches');
  THEMES.forEach((t,i)=>{{
    const s=document.createElement('div');
    s.className='swatch'+(i===0?' on':'');
    s.style.background=t.hand;s.title=t.id;
    s.onclick=()=>{{document.querySelectorAll('.swatch').forEach(x=>x.classList.remove('on'));s.classList.add('on');theme=t}};
    wrap.appendChild(s);
  }});
}}
buildSwatches();

function setRender(m){{
  settings.render=m;
  ['3d','flat','wire'].forEach(x=>{{
    document.getElementById('r'+x)?.classList.toggle('on',x===m);
    document.getElementById('c'+x)?.classList.toggle('on',x===m);
  }});
}}
setRender('3d');

function toggleMirror(){{
  settings.mirror=!settings.mirror;
  document.getElementById('togMirror').checked=settings.mirror;
  document.getElementById('cmirror').classList.toggle('on',settings.mirror);
}}

function setCanvasSize(w,h){{
  canvas.width=W=w;canvas.height=H=h;
  PALM.x=W/2;PALM.y=H*.70;
  FBASES[0]={{x:PALM.x-72,y:PALM.y-28}};
  FBASES[1]={{x:PALM.x-40,y:PALM.y-82}};
  FBASES[2]={{x:PALM.x-8, y:PALM.y-90}};
  FBASES[3]={{x:PALM.x+24,y:PALM.y-84}};
  FBASES[4]={{x:PALM.x+55,y:PALM.y-72}};
}}

function screenshotCanvas(){{
  const link=document.createElement('a');
  link.download='signflow-'+Date.now()+'.png';
  link.href=canvas.toDataURL('image/png');
  link.click();
  showToast('📷','Screenshot saved');
}}

// ══════════════════════════════════════════════════════════════════════════════
// SPEED
// ══════════════════════════════════════════════════════════════════════════════
function setPreset(ms){{
  speedMs=ms;
  document.getElementById('speedRange').value=ms;
  document.getElementById('speedLabel').textContent=ms+'ms';
  document.querySelectorAll('.preset').forEach(b=>b.classList.remove('on'));
  const presets=[200,550,900,1400];
  presets.forEach((v,i)=>{{if(v===ms)document.querySelectorAll('.preset')[i].classList.add('on')}});
}}
function onSpeedRange(){{
  speedMs=parseInt(document.getElementById('speedRange').value);
  document.getElementById('speedLabel').textContent=speedMs+'ms';
  document.querySelectorAll('.preset').forEach(b=>b.classList.remove('on'));
}}

// ══════════════════════════════════════════════════════════════════════════════
// TEXT INPUT
// ══════════════════════════════════════════════════════════════════════════════
function onInput(){{
  const n=document.getElementById('mainInput').value.length;
  document.getElementById('charN').textContent=n;
}}
function signFromText(){{
  const t=document.getElementById('mainInput').value;
  if(t.trim()) startSigning(t);
}}
function clearText(){{
  document.getElementById('mainInput').value='';
  document.getElementById('charN').textContent='0';
}}
function copyText(){{
  navigator.clipboard.writeText(document.getElementById('mainInput').value);
  showToast('📋','Copied to clipboard');
}}

// Favorites
let favorites=JSON.parse(localStorage.getItem('sf_favorites')||'[]');
function saveFavorite(){{
  const t=document.getElementById('mainInput').value.trim();
  if(!t)return;
  if(!favorites.includes(t)){{
    favorites.unshift(t);
    if(favorites.length>10)favorites.pop();
    localStorage.setItem('sf_favorites',JSON.stringify(favorites));
  }}
  renderFavs();
  showToast('⭐','Saved to favorites');
}}
function renderFavs(){{
  const list=document.getElementById('favList');
  if(!favorites.length){{document.getElementById('favsSection').style.display='none';return}}
  document.getElementById('favsSection').style.display='block';
  list.innerHTML=favorites.map((f,i)=>`
    <div style="display:flex;align-items:center;gap:6px;padding:6px 10px;
      background:var(--surface2);border:1px solid var(--border);border-radius:6px;cursor:pointer"
      onclick="useFav('${{f.replace(/'/g,'\\\\\\'')}}')" >
      <span style="flex:1;font-size:.8rem;color:var(--text2);overflow:hidden;text-overflow:ellipsis;white-space:nowrap">${{f}}</span>
      <span style="font-size:.7rem;color:var(--accent3)">▶</span>
      <span style="font-size:.7rem;color:var(--rose2);cursor:pointer" onclick="event.stopPropagation();delFav(${{i}})">✕</span>
    </div>`).join('');
}}
function useFav(t){{document.getElementById('mainInput').value=t;onInput();startSigning(t)}}
function delFav(i){{favorites.splice(i,1);localStorage.setItem('sf_favorites',JSON.stringify(favorites));renderFavs()}}
renderFavs();

// ══════════════════════════════════════════════════════════════════════════════
// PHRASES
// ══════════════════════════════════════════════════════════════════════════════
function buildPhrases(){{
  const grid=document.getElementById('phrasesGrid');
  const favPhrases=JSON.parse(localStorage.getItem('sf_favphrases')||'[]');
  PHRASES.forEach(([label,text])=>{{
    const b=document.createElement('button');
    b.className='phrase'+(favPhrases.includes(text)?' fav':'');
    b.textContent=label;b.title=text;
    b.onclick=()=>{{startSigning(text);showToast('🤟','Signing: '+text)}};
    b.ondblclick=()=>{{
      const fp=JSON.parse(localStorage.getItem('sf_favphrases')||'[]');
      const idx=fp.indexOf(text);
      idx===-1?fp.push(text):fp.splice(idx,1);
      localStorage.setItem('sf_favphrases',JSON.stringify(fp));
      b.classList.toggle('fav',idx===-1);
      showToast('⭐',idx===-1?'Phrase favorited':'Phrase unfavorited');
    }};
    grid.appendChild(b);
  }});
}}
buildPhrases();

// ══════════════════════════════════════════════════════════════════════════════
// ALPHABET GRID
// ══════════════════════════════════════════════════════════════════════════════
let favLetters=JSON.parse(localStorage.getItem('sf_favletters')||'[]');
function buildAlpha(){{
  const grid=document.getElementById('alphaGrid');
  'abcdefghijklmnopqrstuvwxyz'.split('').forEach(ch=>{{
    const card=document.createElement('div');
    card.className='alpha-card'+(favLetters.includes(ch)?' fav-letter':'');
    card.innerHTML=`<span class="l">${{ch.toUpperCase()}}</span><span class="s">ASL</span>`;
    card.onclick=()=>{{
      curPose=lerpPose(curPose,tgtPose,animT);tgtPose=ASL[ch];animT=0;
      document.getElementById('bigLetter').textContent=ch.toUpperCase();
      document.getElementById('signName').textContent='Letter '+ch.toUpperCase();
      document.getElementById('signSub').textContent='ASL preview tap';
    }};
    // Long-press to fav
    let pressTimer;
    card.onmousedown=()=>{{pressTimer=setTimeout(()=>{{
      const idx=favLetters.indexOf(ch);
      idx===-1?favLetters.push(ch):favLetters.splice(idx,1);
      localStorage.setItem('sf_favletters',JSON.stringify(favLetters));
      card.classList.toggle('fav-letter',idx===-1);
      showToast('⭐',idx===-1?ch.toUpperCase()+' added to favorites':'Removed from favorites');
    }},600)}};
    card.onmouseup=card.onmouseleave=()=>clearTimeout(pressTimer);
    grid.appendChild(card);
  }});
}}
buildAlpha();

function spellAll(){{startSigning('abcdefghijklmnopqrstuvwxyz')}}
function spellRandom(){{
  const ch='abcdefghijklmnopqrstuvwxyz'[Math.floor(Math.random()*26)];
  curPose=lerpPose(curPose,tgtPose,animT);tgtPose=ASL[ch];animT=0;
  document.getElementById('bigLetter').textContent=ch.toUpperCase();
  document.getElementById('signName').textContent='Random: '+ch.toUpperCase();
  document.getElementById('signSub').textContent='Can you identify this sign?';
  showToast('🎲','Letter: '+ch.toUpperCase());
}}

// ══════════════════════════════════════════════════════════════════════════════
// QUIZ
// ══════════════════════════════════════════════════════════════════════════════
let quiz={{ letter:'', score:0, total:0, streak:0, mode:'read', active:false }};
function initQuiz(){{if(!quiz.active){{quiz.active=true;newQuestion()}}}}
function newQuestion(){{
  const letters='abcdefghijklmnopqrstuvwxyz'.split('');
  quiz.letter=letters[Math.floor(Math.random()*26)];
  curPose=lerpPose(curPose,tgtPose,animT);tgtPose=ASL[quiz.letter];animT=0;
  document.getElementById('qLetter').textContent='?';
  document.getElementById('qPrompt').textContent='What letter is this hand sign?';
  // Generate options
  const opts=new Set([quiz.letter]);
  while(opts.size<4) opts.add(letters[Math.floor(Math.random()*26)]);
  const shuffled=[...opts].sort(()=>Math.random()-.5);
  document.getElementById('qOptions').innerHTML=shuffled.map(l=>
    `<button class="quiz-opt" onclick="answerQuiz('${{l}}')">${{l.toUpperCase()}}</button>`
  ).join('');
}}
function answerQuiz(guess){{
  const correct=guess===quiz.letter;
  quiz.total++;
  if(correct){{quiz.score++;quiz.streak++;playCorrect()}}
  else{{quiz.streak=0;playWrong()}}
  document.getElementById('qLetter').textContent=quiz.letter.toUpperCase();
  document.querySelectorAll('.quiz-opt').forEach(b=>{{
    b.disabled=true;
    if(b.textContent===quiz.letter.toUpperCase())b.classList.add('correct');
    else if(b.textContent===guess.toUpperCase())b.classList.add('wrong');
  }});
  document.getElementById('qScore').textContent=quiz.score;
  document.getElementById('qTotal').textContent=quiz.total;
  document.getElementById('qStreak').textContent='🔥 '+quiz.streak;
  document.getElementById('sAcc').textContent=Math.round(quiz.score/quiz.total*100)+'%';
  showToast(correct?'🎉':'😬',correct?'Correct! +1':'Wrong — it was '+quiz.letter.toUpperCase());
  if(correct && quiz.streak>0 && quiz.streak%3===0) confetti();
  setTimeout(newQuestion,1400);
}}
function resetQuiz(){{quiz.score=0;quiz.total=0;quiz.streak=0;quiz.active=true;newQuestion();
  document.getElementById('qScore').textContent='0';document.getElementById('qTotal').textContent='0';
  document.getElementById('qStreak').textContent='🔥 0';}}
function setQMode(m){{quiz.mode=m;newQuestion()}}

// ══════════════════════════════════════════════════════════════════════════════
// HISTORY
// ══════════════════════════════════════════════════════════════════════════════
let historyData=[];
function addHistory(text){{
  const ts=new Date();
  historyData.unshift({{text,time:ts.toLocaleTimeString([],{{hour:'2-digit',minute:'2-digit'}})}});
  if(historyData.length>20) historyData.pop();
  renderHistory();
}}
function renderHistory(){{
  const list=document.getElementById('histList');
  if(!historyData.length){{list.innerHTML='<div style="font-size:.82rem;color:var(--text3);text-align:center;padding:20px">No history yet</div>';return}}
  list.innerHTML=historyData.map((h,i)=>`
    <div class="hist-item" onclick="startSigning('${{h.text.replace(/'/g,"\\\\'")}}')">
      <span class="hist-txt">${{h.text.substring(0,60)+(h.text.length>60?'…':'')}}</span>
      <span class="hist-time">${{h.time}}</span>
      <span class="hist-actions">
        <span class="hist-icon" title="Replay" onclick="event.stopPropagation();startSigning('${{h.text.replace(/'/g,"\\\\'")}}')">↺</span>
        <span class="hist-icon" title="Copy" onclick="event.stopPropagation();navigator.clipboard.writeText('${{h.text}}');showToast('📋','Copied')">📋</span>
        <span class="hist-icon" title="Delete" onclick="event.stopPropagation();historyData.splice(${{i}},1);renderHistory()">✕</span>
      </span>
    </div>`).join('');
}}
function clearHistory(){{historyData=[];renderHistory()}}
function exportHistory(){{doExport('csv')}}

// ══════════════════════════════════════════════════════════════════════════════
// MICROPHONE / ASR
// ══════════════════════════════════════════════════════════════════════════════
let recognition=null, listening=false, micStream=null, autoSignOn=false;

function setupASR(){{
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition;
  if(!SR){{
    document.getElementById('micHint').textContent='⚠️ Not supported — use Chrome or Edge';
    return false;
  }}
  recognition=new SR();
  recognition.continuous=true;recognition.interimResults=true;
  recognition.lang=document.getElementById('langSelect').value;
  recognition.onresult=(ev)=>{{
    let interim='',final='';
    for(let i=ev.resultIndex;i<ev.results.length;i++){{
      ev.results[i].isFinal?final+=ev.results[i][0].transcript:interim+=ev.results[i][0].transcript;
    }}
    const el=document.getElementById('liveText');
    el.style.color=final?'var(--accent3)':'var(--text3)';
    el.textContent=(final||interim)||'Listening…';
    if(final.trim()){{
      const btn=document.getElementById('signTransBtn');
      btn.disabled=false;btn.dataset.text=final.trim();
      if(settings.autoSign||autoSignOn) startSigning(final.trim());
    }}
  }};
  recognition.onerror=(e)=>{{setMicUI(false);document.getElementById('micHint').textContent='Error: '+e.error}};
  recognition.onend=()=>{{if(listening)recognition.start()}};
  return true;
}}

async function toggleMic(){{
  if(listening){{
    listening=false;if(recognition)recognition.stop();
    stopWave();if(micStream)micStream.getTracks().forEach(t=>t.stop());
    setMicUI(false);
  }} else {{
    if(!recognition&&!setupASR())return;
    try{{micStream=await navigator.mediaDevices.getUserMedia({{audio:true}});startWave(micStream)}}catch(e){{}}
    listening=true;recognition.start();setMicUI(true);
  }}
}}

function setMicUI(on){{
  const btn=document.getElementById('micBtn');
  btn.className=on?'on':'';
  btn.style.cssText=`
    width:60px;height:60px;border-radius:50%;border:none;cursor:pointer;font-size:1.5rem;
    color:#fff;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .2s;
    background:linear-gradient(135deg,${{on?'#f43f5e,#ff3366':'#f43f5e,#ff5580'}});
    box-shadow:0 4px 16px rgba(244,63,94,.4);
    animation:${{on?'mic-ring 1.2s ease-in-out infinite':'none'}};
  `;
  document.getElementById('micStatus').textContent=on?'🔴 Listening…':'Ready to listen';
  document.getElementById('micHint').textContent=on?'Tap to stop · Speak clearly':'Chrome / Edge · Web Speech API';
  if(!on){{
    const el=document.getElementById('liveText');
    el.textContent='Transcript will appear here…';el.style.color='var(--text3)';
  }}
}}

function signTranscript(){{
  const t=document.getElementById('signTransBtn').dataset.text;
  if(t) startSigning(t);
}}
function clearTrans(){{
  document.getElementById('liveText').textContent='Transcript will appear here…';
  document.getElementById('liveText').style.color='var(--text3)';
  const btn=document.getElementById('signTransBtn');btn.disabled=true;delete btn.dataset.text;
}}
function autoSign(){{
  autoSignOn=!autoSignOn;
  const btn=document.getElementById('autoBtn');
  btn.textContent=autoSignOn?'🔄 Auto ON':'🔄 Auto-Sign';
  btn.className='btn '+(autoSignOn?'btn-green':'btn-teal');
  showToast('🔄','Auto-sign '+(autoSignOn?'enabled':'disabled'));
}}
function setLang(){{if(recognition){{recognition.lang=document.getElementById('langSelect').value;if(listening){{recognition.stop();setTimeout(()=>recognition.start(),200);}}}}}}

// ══════════════════════════════════════════════════════════════════════════════
// WAVEFORM
// ══════════════════════════════════════════════════════════════════════════════
let wCtx=null,analyser=null,wData=null,wRaf=null;
function startWave(stream){{
  wCtx=new(window.AudioContext||window.webkitAudioContext)();
  analyser=wCtx.createAnalyser();analyser.fftSize=256;
  wCtx.createMediaStreamSource(stream).connect(analyser);
  wData=new Uint8Array(analyser.frequencyBinCount);
  drawWave();
}}
function drawWave(){{
  const wc=document.getElementById('wave');
  const wx=wc.getContext('2d');
  const WW=wc.width=wc.offsetWidth||320,WH=44;wc.height=WH;
  if(analyser)analyser.getByteTimeDomainData(wData);
  wx.clearRect(0,0,WW,WH);
  wx.beginPath();
  const sl=WW/(wData?wData.length:128);let x=0;
  for(let i=0;i<(wData?wData.length:128);i++){{
    const v=(wData?wData[i]:128)/128;const y=v*(WH/2);
    i===0?wx.moveTo(x,y):wx.lineTo(x,y);x+=sl;
  }}
  wx.strokeStyle=theme.hand;wx.lineWidth=2;wx.lineCap='round';wx.stroke();
  wRaf=requestAnimationFrame(drawWave);
}}
function stopWave(){{
  if(wRaf)cancelAnimationFrame(wRaf);
  if(wCtx)wCtx.close();wCtx=null;
  const wc=document.getElementById('wave');
  wc.getContext('2d').clearRect(0,0,wc.width,wc.height);
}}

// ══════════════════════════════════════════════════════════════════════════════
// EXPORT
// ══════════════════════════════════════════════════════════════════════════════
function openExport(){{document.getElementById('exportModal').classList.add('open')}}
function closeExport(e){{if(!e||e.target===document.getElementById('exportModal'))document.getElementById('exportModal').classList.remove('open')}}

function doExport(fmt){{
  closeExport();
  if(fmt==='png'){{screenshotCanvas();return}}
  let content='',filename='',type='';
  if(fmt==='txt'){{
    content=historyData.map(h=>`[${{h.time}}] ${{h.text}}`).join('\\n')||'No history';
    filename='signflow-history.txt';type='text/plain';
  }} else if(fmt==='csv'){{
    content='Time,Text\\n'+historyData.map(h=>`"${{h.time}}","${{h.text.replace(/"/g,'""')}}"`).join('\\n');
    filename='signflow-history.csv';type='text/csv';
  }} else if(fmt==='json'){{
    content=JSON.stringify({{history:historyData,stats:{{signs:totalSigns,words:totalWords}},exported:new Date().toISOString()}},null,2);
    filename='signflow-export.json';type='application/json';
  }}
  const a=document.createElement('a');
  a.href=URL.createObjectURL(new Blob([content],{{type}}));
  a.download=filename;a.click();
  showToast('📤','Exported as '+filename);
}}

// ══════════════════════════════════════════════════════════════════════════════
// SOUND FX
// ══════════════════════════════════════════════════════════════════════════════
function playClick(){{
  const ac=new(window.AudioContext||window.webkitAudioContext)();
  const o=ac.createOscillator(),g=ac.createGain();
  o.connect(g);g.connect(ac.destination);
  o.frequency.value=800;g.gain.setValueAtTime(.05,ac.currentTime);
  g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.1);
  o.start();o.stop(ac.currentTime+.1);
}}
function playCorrect(){{
  if(!settings.sound)return;
  const ac=new(window.AudioContext||window.webkitAudioContext)();
  [523,659,784].forEach((f,i)=>{{
    const o=ac.createOscillator(),g=ac.createGain();
    o.connect(g);g.connect(ac.destination);o.frequency.value=f;
    g.gain.setValueAtTime(.06,ac.currentTime+i*.1);
    g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+i*.1+.15);
    o.start(ac.currentTime+i*.1);o.stop(ac.currentTime+i*.1+.15);
  }});
}}
function playWrong(){{
  if(!settings.sound)return;
  const ac=new(window.AudioContext||window.webkitAudioContext)();
  const o=ac.createOscillator(),g=ac.createGain();
  o.connect(g);g.connect(ac.destination);o.type='sawtooth';o.frequency.value=200;
  g.gain.setValueAtTime(.05,ac.currentTime);
  g.gain.exponentialRampToValueAtTime(.001,ac.currentTime+.3);
  o.start();o.stop(ac.currentTime+.3);
}}

// ══════════════════════════════════════════════════════════════════════════════
// TOAST
// ══════════════════════════════════════════════════════════════════════════════
let toastTimer;
function showToast(icon,msg){{
  clearTimeout(toastTimer);
  document.getElementById('toastIcon').textContent=icon;
  document.getElementById('toastMsg').textContent=msg;
  const t=document.getElementById('toast');t.classList.add('show');
  toastTimer=setTimeout(()=>t.classList.remove('show'),2600);
}}

// ══════════════════════════════════════════════════════════════════════════════
// LIGHT MODE
// ══════════════════════════════════════════════════════════════════════════════
let lightMode=false;
function toggleLight(){{
  lightMode=!lightMode;
  document.body.classList.toggle('light',lightMode);
  document.getElementById('lightBtn').textContent=lightMode?'🌙':'☀️';
}}

// ══════════════════════════════════════════════════════════════════════════════
// KEYBOARD SHORTCUTS
// ══════════════════════════════════════════════════════════════════════════════
document.addEventListener('keydown',e=>{{
  if(e.target.tagName==='TEXTAREA'||e.target.tagName==='INPUT')return;
  if(e.key==='Enter') signFromText();
  if(e.key===' '){{e.preventDefault();if(playing)togglePause()}}
  if(e.key==='m')toggleMic();
  if(e.key==='r')spellRandom();
  if(e.key==='?')switchToTab('shortcuts');
  if(e.key==='Escape')closeExport();
  if(e.key>='a'&&e.key<='z'){{
    curPose=lerpPose(curPose,tgtPose,animT);tgtPose=ASL[e.key];animT=0;
    document.getElementById('bigLetter').textContent=e.key.toUpperCase();
    document.getElementById('signName').textContent='Letter '+e.key.toUpperCase();
    document.getElementById('signSub').textContent='ASL preview';
  }}
}});

showToast('🤟','SignFlow Pro v3 ready! Press ? for shortcuts.');
</script>
</body></html>"""

st.components.v1.html(MAIN_HTML, height=900, scrolling=False)

st.markdown("""
<style>
  #MainMenu,footer,[data-testid="stToolbar"],[data-testid="stDecoration"]{visibility:hidden}
  .block-container{padding:0!important;max-width:100%!important}
  header{display:none!important}
  [data-testid="stAppViewContainer"]{padding:0!important}
  section[data-testid="stMain"]{padding:0!important}
</style>""", unsafe_allow_html=True)