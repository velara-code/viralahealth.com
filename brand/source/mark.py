"""VIRALA Life Chapters mark in VIRALA Dusk (28 October 2026): the established three-page geometry, unchanged, in the
Dusk palette, plus the app-icon set and the website favicon. One mark everywhere: header, footer, favicon, welcome, social
card, 404, Instagram and (once approved) the app.
Writes brand/logo/virala-mark*.svg, brand/icon/app-icon-*.svg and site/assets/favicon.svg.
Run: python3 -I brand/source/mark.py   (PNG exports: python3 -I brand/source/export_icons.py <fresh empty dir>)"""
from pathlib import Path
B = Path(__file__).resolve().parent.parent
P1 = 'M0 48 C60 108 158 132 202 174 C234 204 242 224 242 274 L242 608 C242 665 249 695 272 736 C218 680 122 633 60 595 C20 570 0 537 0 492 Z'
P2 = 'M136 0 C196 51 252 78 322 113 C369 137 390 167 390 220 L390 482 C390 570 368 610 316 661 L276 704 C264 664 268 625 268 588 L268 270 C268 204 233 168 187 142 L136 114 Z'
P3 = 'M416 244 L506 291 C535 307 544 325 544 355 L544 503 C544 540 529 560 495 578 L326 668 C390 602 416 556 416 484 Z'

DUSK, DUSK_LIGHT, NIGHT, ROSE, ROSE_LIFT, PEACH, PORCELAIN = '#2C4560', '#3D5A78', '#131D29', '#A35866', '#D98E9B', '#EBB49F', '#FAF5F2'
# front page / middle page / back page
ON_LIGHT = (DUSK, ROSE, PEACH)          # on porcelain, mist, blush
ON_DUSK = (PORCELAIN, PEACH, ROSE_LIFT)  # on Dusk and night blue (rose lifted so the small back page stays visible)
PALETTES = {'': ON_LIGHT, '-dark': ON_DUSK, '-black': ('#000000',) * 3, '-white': ('#FFFFFF',) * 3}


def mark(c1, c2, c3):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 544 736" role="img" aria-label="VIRALA"><path fill="{c1}" d="{P1}"/>'
            f'<path fill="{c2}" d="{P2}"/><path fill="{c3}" d="{P3}"/></svg>\n')


for suffix, cols in PALETTES.items():
    (B / f'logo/virala-mark{suffix}.svg').write_text(mark(*cols))


def icon(bg0, bg1, glow, cols, size=1024, rx=0, scale=.58):
    """The mark centred on a gradient tile; `glow` is a faint corner light (the Dusk depth recipe)."""
    k = size * scale / 736; tx = (size - 544 * k) / 2; ty = (size - 736 * k) / 2
    g = (f'<radialGradient id="r" cx=".82" cy=".14" r=".75"><stop offset="0" stop-color="{glow}" stop-opacity=".2"/>'
         f'<stop offset="1" stop-color="{glow}" stop-opacity="0"/></radialGradient>') if glow else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" role="img" aria-label="VIRALA"><defs><linearGradient id="g" x1="0" y1="0" x2=".7" y2="1">'
            f'<stop offset="0" stop-color="{bg0}"/><stop offset="1" stop-color="{bg1}"/></linearGradient>{g}</defs><rect width="{size}" height="{size}" rx="{rx}" fill="url(#g)"/>'
            + (f'<rect width="{size}" height="{size}" rx="{rx}" fill="url(#r)"/>' if glow else '')
            + f'<g transform="translate({tx:.1f} {ty:.1f}) scale({k:.4f})"><path fill="{cols[0]}" d="{P1}"/><path fill="{cols[1]}" d="{P2}"/><path fill="{cols[2]}" d="{P3}"/></g></svg>\n')


(B / 'icon').mkdir(exist_ok=True)
ICONS = {
    'app-icon-dusk': (DUSK_LIGHT, '#1E3147', PEACH, ON_DUSK),            # primary: matches Instagram and the favicon
    'app-icon-porcelain': (PORCELAIN, '#F3E6E1', None, ON_LIGHT),       # alternative: light
    'app-icon-dark': ('#1C2A3A', NIGHT, PEACH, ON_DUSK),                # iOS Dark appearance
    'app-icon-tinted': ('#000000', '#000000', None, ('#FFFFFF', '#C8C8C8', '#9A9A9A')),  # iOS Tinted appearance
}
for name, (a, b, glow, cols) in ICONS.items():
    (B / f'icon/{name}.svg').write_text(icon(a, b, glow, cols))
# Favicon: the Dusk tile, rounded, the mark enlarged so it holds at 16-32 px
(B.parent / 'site/assets/favicon.svg').write_text(icon(DUSK_LIGHT, '#1E3147', None, ON_DUSK, rx=228, scale=.68))
print('mark, icons and favicon written (VIRALA Dusk)')
