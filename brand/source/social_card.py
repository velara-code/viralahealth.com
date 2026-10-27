"""The VIRALA social card (Open Graph image, 1200 x 630) in VIRALA Dusk. Writes source-assets/social-card.html; render it to
site/assets/social-card.jpg with headless Chrome (see review/VERIFICATION.md). Standard library only.
    python3 -I brand/source/social_card.py"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
P = [l.split("'")[1] for l in (ROOT / 'brand/source/mark.py').read_text().splitlines() if l.startswith(('P1 =', 'P2 =', 'P3 ='))]
mark = ('<svg class="mk" viewBox="0 0 544 736" aria-hidden="true">' +
        ''.join(f'<path fill="{c}" d="{d}"/>' for c, d in zip(('#FAF5F2', '#EBB49F', '#C47784'), P)) + '</svg>')
wm = (ROOT / 'brand/logo/virala-wordmark-text.svg').read_text().strip()
(ROOT / 'source-assets/social-card.html').write_text(f'''<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:NR;src:url("../site/assets/newsreader.woff2");font-weight:300 700}}@font-face{{font-family:NR;font-style:italic;src:url("../site/assets/newsreader-italic.woff2");font-weight:300 700}}
@font-face{{font-family:HG;src:url("../site/assets/hanken-grotesk.woff2");font-weight:300 700}}
body{{margin:0;width:1200px;height:630px;box-sizing:border-box;padding:64px 76px 60px;display:flex;flex-direction:column;justify-content:space-between;color:#FAF5F2;font-family:HG;
background:radial-gradient(520px 400px at 96% 0%,rgba(240,178,156,.55),rgba(232,166,177,.24) 42%,transparent 74%),radial-gradient(480px 360px at 0% 100%,rgba(232,166,177,.24),transparent 70%),linear-gradient(160deg,#2A425C 0%,#23384F 50%,#1B2B3E 100%)}}
.top{{display:flex;align-items:center;gap:22px;font-size:15px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}}.top i{{flex:1;height:1px;background:rgba(250,245,242,.3)}}
.h{{font-family:NR;font-weight:400;font-size:88px;line-height:1;letter-spacing:-.025em;max-width:1000px;margin:0}}.h em{{color:#C47784}}
.base{{display:flex;align-items:flex-end;justify-content:space-between;gap:40px}}
.lk{{display:flex;align-items:center;gap:18px}}.mk{{height:64px;width:auto}}.lk svg:last-child{{height:34px;width:auto;color:#FAF5F2;fill:#FAF5F2}}
.t{{font-family:NR;font-size:38px;line-height:1;letter-spacing:-.01em}}.t em{{color:#C47784}}
</style></head><body><div class="top"><span>For perimenopause &amp; menopause</span><i></i><span>viralahealth.com</span></div>
<p class="h">Don’t just track your symptoms.<br><em>Understand them.</em></p>
<div class="base"><div class="lk">{mark}{wm}</div><p class="t">Your body, <em>understood.</em></p></div></body></html>
''')
print('source-assets/social-card.html written')
