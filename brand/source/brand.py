"""VIRALA Dusk: the single brand source for the website, the app and Instagram (28 October 2026).
Writes brand/tokens.json, brand/BRAND.md and brand/brand-sheet.html from the values below; contrast is computed, never typed.
Render the sheet to PNG with headless Chrome (review/VERIFICATION.md). Standard library only.
    python3 -I brand/source/brand.py
Nothing changes in the app until the Founder approves and HQ records it."""
import json
from pathlib import Path

B = Path(__file__).resolve().parent.parent
VERSION, DATE = '4.2.0-dusk', '2026-10-28'

PALETTE = {  # name: (hex, role)
    'dusk':      ('#2C4560', 'Signature. Primary buttons, the hero signup card, the Premium card, deep bands, the footer.'),
    'rose':      ('#C47784', 'The ONE accent, exactly the same on every ground (porcelain, Dusk, dark mode). Only for large italic accent words in headlines (24 px and up). Never small text: numbers, labels, links and citations are ink on light grounds and porcelain on dark.'),
    'peach':     ('#EBB49F', 'Glow only: the soft light inside the hero card, the Meet Vira band and the footer, and the mark\'s back page. Never text.'),
    'ink':       ('#1F2A37', 'All text on light grounds. No light-grey body text anywhere.'),
    'mist':      ('#DCE5EC', 'Light blue bands and surfaces.'),
    'blush':     ('#F3DCD5', 'Soft rose surfaces and bands.'),
    'porcelain': ('#FAF5F2', 'Page ground; text and buttons on Dusk.'),
}
SUPPORT = {  # derived tones: depth and dark mode only
    'duskLight': ('#3D5A78', 'The lighter end of Dusk gradients.'),
    'duskDeep':  ('#1B2B3E', 'The deep end of Dusk gradients.'),
    'night':     ('#131D29', 'Dark mode ground.'),
    'nightSurface': ('#1C2A3A', 'Dark mode cards.'),
    'white':     ('#FFFDFB', 'Raised cards on porcelain.'),
}
ALL = {k: v[0] for k, v in {**PALETTE, **SUPPORT}.items()}

ROLES = {
    'light': {'ground': 'porcelain', 'surface': 'white', 'text': 'ink', 'eyebrow': 'dusk', 'italicAccent': 'rose', 'smallHighlight': 'ink',
              'button': 'dusk', 'buttonText': 'porcelain', 'deepSurface': 'dusk', 'onDeepText': 'porcelain', 'onDeepItalic': 'rose',
              'onDeepButton': 'porcelain', 'onDeepButtonText': 'ink'},
    'dark':  {'ground': 'night', 'surface': 'nightSurface', 'text': 'porcelain', 'eyebrow': 'mist', 'italicAccent': 'rose', 'smallHighlight': 'porcelain',
              'button': 'porcelain', 'buttonText': 'ink', 'deepSurface': 'dusk', 'onDeepText': 'porcelain', 'onDeepItalic': 'rose',
              'onDeepButton': 'porcelain', 'onDeepButtonText': 'ink'},
}


def lum(h):
    c = [int(h[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    c = [x / 12.92 if x <= .04045 else ((x + .055) / 1.055) ** 2.4 for x in c]
    return .2126 * c[0] + .7152 * c[1] + .0722 * c[2]


def ratio(a, b):
    a, b = ALL.get(a, a), ALL.get(b, b)
    la, lb = lum(a), lum(b)
    return round((max(la, lb) + .05) / (min(la, lb) + .05), 2)


PAIRS = [  # (text, background, need, use)
    ('ink', 'porcelain', 4.5, 'Body text'), ('ink', 'white', 4.5, 'Text on cards'), ('ink', 'mist', 4.5, 'Text on mist bands'), ('ink', 'blush', 4.5, 'Text on blush bands'),
    ('dusk', 'porcelain', 4.5, 'Eyebrows, labels'), ('dusk', 'mist', 4.5, 'Eyebrows on mist'), ('dusk', 'blush', 4.5, 'Eyebrows on blush'),
    ('rose', 'porcelain', 3.0, 'Rose italic accent words on porcelain (24 px and up only)'), ('rose', 'white', 3.0, 'Rose italic accent words on cards (24 px and up only)'),
    ('porcelain', 'dusk', 4.5, 'Text on Dusk'), ('porcelain', '#283F58', 4.5, 'Text on the lightest stop of the deep gradients'),
    ('rose', '#283F58', 3.0, 'Rose italics on the deep band (its lightest stop)'), ('rose', '#2A425C', 3.0, 'Rose italics on the deep card (its lightest stop)'),
    ('ink', 'porcelain', 4.5, 'Porcelain button label on Dusk (ink on porcelain)'),
    ('porcelain', 'night', 4.5, 'Dark: text and small emphasis'), ('mist', 'night', 4.5, 'Dark: eyebrows'), ('rose', 'night', 3.0, 'Dark: rose italic accent words'),
    ('porcelain', 'nightSurface', 4.5, 'Dark: text on cards'), ('rose', 'nightSurface', 3.0, 'Dark: rose italics on cards'),
]
contrast = [{'text': t, 'background': b, 'ratio': ratio(t, b), 'required': n, 'use': u, 'pass': ratio(t, b) >= n} for t, b, n, u in PAIRS]
assert all(p['pass'] for p in contrast), [p for p in contrast if not p['pass']]

DEPTH = {
    'glow': 'THE SIGNATURE (as on Instagram): soft peach and rose light inside deep Dusk, in three places only: the hero signup card, the Meet Vira band, the footer. A small bright core fading out (a wide faint glow turns grey on blue): radial-gradient(520px 380px at 84% 0%, rgba(240,178,156,.5), rgba(232,166,177,.22) 42%, transparent 72%), radial-gradient(460px 340px at 6% 104%, rgba(232,166,177,.26), transparent 68%) over the deep band',
    'deepBand': 'linear-gradient(168deg, #283F58 0%, #23384F 45%, #18263A 100%) (plain, for every other deep section)',
    'deepCard': 'radial-gradient(320px 280px at 96% 2%, rgba(240,178,156,.62), rgba(232,166,177,.26) 42%, transparent 74%), radial-gradient(360px 300px at 0% 100%, rgba(232,166,177,.22), transparent 70%), linear-gradient(160deg, #2A425C 0%, #23384F 50%, #1B2B3E 100%) (the hero card; the Premium card uses the plain card gradient)',
    'pageGlow': 'radial-gradient(1100px 640px at 100% -12%, rgba(243,220,213,.5), transparent 62%) over porcelain, behind the first screen only',
    'photoBand': 'photo graded saturate(.85) contrast(.95) under a deep Dusk vignette where the text sits: radial rgba(27,43,62,.82 to .22) and linear rgba(44,69,96,.3) to rgba(27,43,62,.55); white text, rose italic; contrast measured from pixels',
    'rule': 'Alternate clearly between porcelain sections and deep Dusk sections; no pale in-between bands. Rose is the one accent. If it starts to look decorated, it is too much.',
}
TYPE = {
    'display': {'family': 'Newsreader', 'licence': 'SIL Open Font License 1.1 (Google Fonts), free for web and app', 'use': 'Headlines, card titles, numbers, the footer line. Italic for accent words.',
                'settings': 'weight 440 for h1/h2 (420 italic), 400 for h3, 450 for list and card titles at 18-24 px; optical sizing on; tracking -0.02em at display sizes'},
    'text': {'family': 'Hanken Grotesk', 'licence': 'SIL Open Font License 1.1 (Google Fonts), free for web and app', 'use': 'Body, UI, buttons, labels.',
             'settings': 'weight 400 body, 500 navigation, 600 buttons and labels; labels uppercase with 0.14em tracking'},
    'scale': {'display': '40-64 px', 'h1': '36-56 px', 'h2': '32-48 px', 'h3': '20-24 px', 'h4': '18-20 px', 'lede': '17-20 px', 'body': '16-17 px (line-height 1.55; articles 16-18 px at 1.68, about 68 characters)', 'small': '14 px', 'label': '12.5 px uppercase'},
    'spacing': 'Section padding 56-96 px; compact cards with short lines; no tall empty cards. A page should be taken in without heavy scrolling.',
    'app': 'In the app, Newsreader for display and titles; Hanken Grotesk or SF Pro for UI text, following Dynamic Type.',
    'alternatives': ['Fraunces + Nunito Sans (warmer, rounder)', 'Source Serif 4 + Albert Sans (more editorial)'],
}
MARK = {
    'shape': 'The Life Chapters mark: three pages, unchanged geometry (brand/logo/virala-mark.svg).',
    'onLight': {'front': 'dusk', 'middle': 'rose', 'back': 'peach'},
    'onDusk': {'front': 'porcelain', 'middle': 'peach', 'back': 'rose'},
    'files': ['brand/logo/virala-mark.svg', 'brand/logo/virala-mark-dark.svg', 'brand/logo/virala-mark-black.svg', 'brand/logo/virala-mark-white.svg',
              'brand/logo/virala-wordmark*.svg (currentColor, dusk, ivory, black)'],
    'use': 'Header, footer, favicon, welcome, social card, 404, Instagram profile, app icon. One mark; no other colourways.',
}
VIRA = {
    'symbol': 'A · Page Spark: VIRALA\'s own sparkle, built from the mark\'s soft page curves, with one small companion spark low on the left.',
    'onLight': ['dusk', 'rose'], 'onDusk': ['porcelain', 'rose'],
    'listening': 'The companion spark gently brightens; nothing spins. Static when the visitor prefers reduced motion.',
    'files': ['brand/vira-symbol/vira-symbol-one.svg', 'vira-symbol-two.svg', 'vira-symbol-on-dark.svg', 'vira-symbol-black.svg', 'vira-symbol-white.svg'],
    'use': 'Vira page (large, in a soft glow), Premium card, Meet Vira band, welcome. Never in a box on the website. How Vira answers is not decided, so no conversation or chat screen is shown anywhere yet.',
}
ICONS = {
    'primary': 'brand/icon/app-icon-dusk.svg (Dusk gradient, the mark on Dusk) — matches the favicon and Instagram',
    'alternative': 'brand/icon/app-icon-porcelain.svg (the 26 Oct porcelain direction, recoloured)',
    'ios': 'brand/icon/AppIcon.appiconset (Any: Dusk, Dark, Tinted); PNGs in brand/icon/png. Not applied to the app.',
    'web': 'site/assets/favicon.svg, apple-touch-icon.png, icon-192.png, icon-512.png (all Dusk)',
}
PHOTOS = ['Calm and real: soft sea, sky, mist, linen, windows, a notebook. Topic-matched in the Journal.',
          'No faces, no hand-only close-ups, no fruit, no visible text or logos.',
          'Graded softly towards Dusk (cooler, slightly desaturated); never filtered to look fake.',
          'Text on a photo only over a Dusk vignette, with contrast measured from the rendered pixels.',
          'Licences: Unsplash free licence (or owned), id and photographer recorded in review/PHOTO_RIGHTS_MANIFEST.md.']
INSTAGRAM = ['Deep Dusk posts with the glow, porcelain Newsreader headlines and one rose italic phrase (#C47784); porcelain posts with ink and rose italics. Peach only inside the glow.',
             'The mark small in a corner; the Vira sparkle only on Vira posts.', 'Same photo rules as the website.']

tokens = {'name': 'VIRALA Dusk', 'version': VERSION, 'date': DATE,
          'status': 'Website (branch website-soft-2026-10-27). The app adopts it only after Founder approval and an HQ record.',
          'palette': {k: {'value': v, 'role': r} for k, (v, r) in PALETTE.items()},
          'support': {k: {'value': v, 'role': r} for k, (v, r) in SUPPORT.items()},
          'roles': ROLES, 'depth': DEPTH, 'type': TYPE, 'mark': MARK, 'viraSymbol': VIRA, 'icons': ICONS,
          'photography': PHOTOS, 'instagram': INSTAGRAM,
          'retired': ['Fig / plum', 'lilac', 'slate #55697C', 'rust / clay', 'Instrument Serif', 'DM Sans'],
          'contrast': contrast}
(B / 'tokens.json').write_text(json.dumps(tokens, indent=2, ensure_ascii=False) + '\n')

# ---------- BRAND.md ----------
rows = '\n'.join(f'| {k} | `{v}` | {r} |' for k, (v, r) in PALETTE.items())
srows = '\n'.join(f'| {k} | `{v}` | {r} |' for k, (v, r) in SUPPORT.items())
crow = '\n'.join(f'| {p["text"]} on {p["background"]} | {p["ratio"]}:1 | {p["required"]}:1 | {p["use"]} |' for p in contrast)
(B / 'BRAND.md').write_text(f'''# VIRALA Dusk — brand guide

Version {VERSION}, {DATE}. The single source for the website, the app and Instagram: values live in `brand/tokens.json`,
generated with this file and `brand/brand-sheet.html` by `brand/source/brand.py`. Nothing changes in the app until the
Founder approves and HQ records it. Earlier identities are in `brand/archive/` for history only.

**Feeling:** premium, personal, calm, fresh, recognisable. Mostly porcelain and air; Dusk only where it needs weight;
rose on a few italic words only.

## Palette

| Name | Hex | Role |
|---|---|---|
{rows}

Support tones (depth and dark mode only):

| Name | Hex | Role |
|---|---|---|
{srows}

Retired everywhere: Fig/plum, lilac, slate #55697C, rust/clay.

**Buttons.** On light grounds: Dusk with porcelain text. On Dusk: porcelain with ink text. In dark mode: porcelain with ink text.

**One accent.** Italic accent words in headlines are always rose #C47784, the same on every ground and in dark mode, and only at 24 px and up. Small emphasis (numbers, labels, links, citations) is ink on light grounds and porcelain on dark, never rose. Peach is never text; it lives only inside the glow and in the mark. Deep Dusk gradients start no lighter than #283F58 so rose holds 3:1 wherever a headline sits.\n\n**Dark mode.** Night blue ground (`#131D29`), porcelain text, mist eyebrows, rose accents (the same rose); Dusk sections stay Dusk. No brown or plum anywhere.

## Depth

{chr(10).join(f'- **{k}:** `{v}`' if k != 'rule' else f'- **Rule:** {v}' for k, v in DEPTH.items())}

## Typography

- **Display: Newsreader** — {TYPE['display']['use']} {TYPE['display']['settings']}. {TYPE['display']['licence']}.
- **Text: Hanken Grotesk** — {TYPE['text']['use']} {TYPE['text']['settings']}. {TYPE['text']['licence']}.
- **Scale (fluid, one scale on every page):** {', '.join(f'{k} {v}' for k, v in TYPE['scale'].items())}.
- **App:** {TYPE['app']}
- Alternatives shown to the Founder: {'; '.join(TYPE['alternatives'])}.

## The mark

{MARK['shape']} On light grounds: Dusk front page, rose middle page, peach back page. On Dusk and night: porcelain, peach,
lifted rose. {MARK['use']}

## Vira's symbol

{VIRA['symbol']} On light: Dusk with a rose companion spark. On Dusk and night: porcelain with the same rose companion.
{VIRA['listening']} {VIRA['use']} Files: `brand/vira-symbol/`.

## Icons

- Primary: {ICONS['primary']}
- Alternative: {ICONS['alternative']}
- iOS: {ICONS['ios']}
- Web: {ICONS['web']}

## Photography

{chr(10).join('- ' + p for p in PHOTOS)}

## Instagram

{chr(10).join('- ' + p for p in INSTAGRAM)}

## Contrast (computed, WCAG 2.x)

| Pair | Ratio | Needs | Use |
|---|---|---|---|
{crow}

Text on photographs is measured from rendered pixels (review/VERIFICATION.md).
''')

# ---------- brand sheet ----------
P = [l.split("'")[1] for l in (B / 'source/mark.py').read_text().splitlines() if l.startswith(('P1 =', 'P2 =', 'P3 ='))]
def mk(cols, h): return f'<svg viewBox="0 0 544 736" style="height:{h}px;width:auto">' + ''.join(f'<path fill="{c}" d="{d}"/>' for c, d in zip(cols, P)) + '</svg>'
spark = (B / 'vira-symbol/vira-symbol-two.svg').read_text().strip()
spark_d = (B / 'vira-symbol/vira-symbol-on-dark.svg').read_text().strip()
wm = (B / 'logo/virala-wordmark-text.svg').read_text().strip()
sw = ''.join(f'<div class="sw"><i style="background:{v}"></i><b>{k.capitalize()}</b><code>{v}</code><span>{r.split(".")[0]}.</span></div>' for k, (v, r) in PALETTE.items())
scale = ''.join(f'<div class="sc"><span>{k}</span><p class="s-{k}">{t}</p></div>' for k, t in (
    ('display', 'Don’t just track your symptoms.<br><em>Understand them.</em>'), ('h2', 'Real understanding, free. <em>More, when you want it.</em>'),
    ('h3', 'Remembers what you choose'), ('body', 'Tell her once. What you choose to share is carried forward, so you never start from zero, and you can change or delete it anytime.'),
    ('label', 'VIRALA PREMIUM')))
(B / 'brand-sheet.html').write_text(f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><title>VIRALA Dusk — brand sheet</title><style>
@font-face{{font-family:NR;src:url("fonts/newsreader.woff2");font-weight:300 700}}@font-face{{font-family:NR;font-style:italic;src:url("fonts/newsreader-italic.woff2");font-weight:300 700}}
@font-face{{font-family:HG;src:url("fonts/hanken-grotesk.woff2");font-weight:300 700}}
*{{box-sizing:border-box}}body{{margin:0;width:1600px;padding:64px 72px;background:radial-gradient(900px 500px at 100% 0%,rgba(243,220,213,.8),transparent 62%),#FAF5F2;color:#1F2A37;font:17px/1.6 HG}}
h1{{font:400 76px/1 NR;letter-spacing:-.025em;margin:0 0 10px}}h1 em,h2 em,.s-display em,.s-h2 em{{font-style:italic;color:#C47784}}
h2{{font:400 34px/1.1 NR;margin:0 0 20px}}.lead{{max-width:62ch;margin:0 0 44px;font-size:19px}}
.lab{{font:600 12.5px/1.5 HG;letter-spacing:.14em;text-transform:uppercase;color:#2C4560;margin:0 0 14px}}
section{{padding:36px 0;border-top:1px solid rgba(31,42,55,.16)}}
.pal{{display:grid;grid-template-columns:repeat(7,1fr);gap:14px}}.sw i{{display:block;height:120px;border-radius:20px;border:1px solid rgba(31,42,55,.1)}}.sw b{{display:block;font:450 21px/1.2 NR;margin-top:12px}}.sw code{{font-size:13px}}.sw span{{display:block;font-size:13.5px;line-height:1.45;margin-top:6px}}
.two{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}.tile{{border-radius:28px;padding:40px;display:flex;align-items:center;gap:22px;min-height:200px}}
.light{{background:#FAF5F2;border:1px solid rgba(31,42,55,.12)}}.dusk{{background:radial-gradient(320px 280px at 96% 2%,rgba(240,178,156,.62),rgba(232,166,177,.26) 42%,transparent 74%),radial-gradient(360px 300px at 0% 100%,rgba(232,166,177,.22),transparent 70%),linear-gradient(160deg,#2A425C,#23384F 50%,#1B2B3E);color:#FAF5F2}}
.tile .wm{{height:40px;width:auto}}.light .wm{{color:#2C4560;fill:#2C4560}}.dusk .wm{{color:#FAF5F2;fill:#FAF5F2}}
.tile svg[role=img]{{height:96px;width:96px}}.icons{{display:flex;gap:24px;align-items:center}}.icons img{{width:150px;height:150px;border-radius:34px;box-shadow:0 20px 40px -24px rgba(27,43,62,.5)}}
.depth{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}}.depth div{{height:150px;border-radius:24px;padding:18px;font:600 12.5px/1.4 HG;letter-spacing:.12em;text-transform:uppercase}}
.sc{{display:grid;grid-template-columns:110px 1fr;gap:24px;align-items:baseline;padding:10px 0}}.sc span{{font:600 12.5px HG;letter-spacing:.12em;text-transform:uppercase;color:#2C4560}}
.s-display{{font:400 72px/1 NR;letter-spacing:-.025em;margin:0}}.s-h2{{font:400 46px/1.08 NR;margin:0}}.s-h3{{font:400 28px/1.16 NR;margin:0}}.s-body{{margin:0;max-width:62ch}}.s-label{{font:600 12.5px HG;letter-spacing:.14em;margin:0;color:#2C4560}}
.btns{{display:flex;gap:16px;align-items:center}}.btn{{display:inline-flex;padding:14px 28px;border-radius:999px;font:600 16px HG}}
ul{{margin:0;padding-left:1.2em}}li+li{{margin-top:6px}}
</style></head><body>
<p class="lab">VIRALA brand · {VERSION} · {DATE}</p><h1>VIRALA <em>Dusk.</em></h1>
<p class="lead">Premium, personal, calm, fresh. Mostly porcelain and air; Dusk where it needs weight; rose on a few italic words. One source for the website, the app and Instagram: <code>brand/tokens.json</code>.</p>
<section><p class="lab">Palette</p><div class="pal">{sw}</div></section>
<section><p class="lab">The mark and Vira’s symbol</p><div class="two">
<div class="tile light">{mk(('#2C4560', '#C47784', '#EBB49F'), 96)}{wm}<span style="flex:1"></span>{spark}</div>
<div class="tile dusk">{mk(('#FAF5F2', '#EBB49F', '#C47784'), 96)}{wm}<span style="flex:1"></span>{spark_d}</div></div></section>
<section><p class="lab">Type · Newsreader + Hanken Grotesk (OFL)</p>{scale}
<div class="btns" style="margin-top:20px"><span class="btn" style="background:#2C4560;color:#FAF5F2">Join the list →</span><span class="btn" style="background:#FAF5F2;color:#1F2A37;border:1px solid rgba(31,42,55,.2)">On Dusk: porcelain →</span><span class="btn" style="background:#23384F;color:#FAF5F2;border:1px solid rgba(250,245,242,.6);padding:7px 12px;font-size:11px;letter-spacing:.12em">PREMIUM</span></div></section>
<section><p class="lab">Depth</p><div class="depth">
<div style="background:radial-gradient(240px 200px at 88% 0%,rgba(240,178,156,.6),rgba(232,166,177,.26) 42%,transparent 74%),radial-gradient(240px 180px at 6% 104%,rgba(232,166,177,.26),transparent 68%),linear-gradient(168deg,#283F58,#23384F 45%,#18263A);color:#FAF5F2">The glow · hero card, Meet Vira, footer</div><div style="background:linear-gradient(168deg,#283F58,#23384F 45%,#18263A);color:#FAF5F2">Deep Dusk · plain</div>
<div style="background:#FAF5F2;border:1px solid rgba(31,42,55,.14)">Porcelain</div><div style="background:#FFFDFB;border:1px solid rgba(31,42,55,.14);box-shadow:0 20px 40px -30px rgba(27,43,62,.4)">Card on porcelain</div></div></section>
<section><p class="lab">App icon set (not applied to the app)</p><div class="icons"><img src="icon/png/app-icon-dusk-1024.png" alt=""><img src="icon/png/app-icon-porcelain-1024.png" alt=""><img src="icon/png/app-icon-dark-1024.png" alt=""><img src="icon/png/app-icon-tinted-1024.png" alt="">
<p style="max-width:34ch;margin:0 0 0 12px">Dusk (primary, matches the favicon and Instagram) · Porcelain (alternative) · Dark · Tinted.</p></div></section>
<section class="two"><div><p class="lab">Photography</p><ul>{''.join(f'<li>{p}</li>' for p in PHOTOS)}</ul></div>
<div><p class="lab">Rules</p><ul><li>All text in ink on light grounds; porcelain on Dusk and night.</li><li>One accent: rose #C47784 on every ground, for large italic accent words only (24 px and up). Small emphasis: ink on light, porcelain on dark.</li><li>Peach is never text: only inside the glow (hero card, Meet Vira, footer).</li><li>{DEPTH['rule']}</li><li>Every text pair WCAG AA ({len(contrast)} pairs computed in tokens.json).</li></ul></div></section>
</body></html>
''')
print(f'brand/tokens.json, BRAND.md, brand-sheet.html written; {len(contrast)} contrast pairs, all AA')
