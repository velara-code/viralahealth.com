"""VIRALA signature wordmark — original letterforms drawn as geometry (no font software involved).
Writes brand/logo/*.svg. Run: python3 -I brand/source/wordmark.py [display|text]

Design: high-contrast capitals with hairline serifs. The signature is the mirror: V is drawn once, and both A's are
the same V turned through 180° (thick and thin strokes trade sides exactly as classical contrast expects), so the name
opens with V and closes with its rotation. No crossbars. Units: cap height 100.
"""
from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / 'logo'
OUT.mkdir(exist_ok=True)

import sys
# optical cuts: 'display' for large sizes, 'text' (sturdier hairlines) for headers, app navigation and anything under ~40 px tall
CUT = sys.argv[1] if len(sys.argv) > 1 else 'display'
T, h = (14.0, 2.4) if CUT == 'display' else (15.5, 5.2)   # thick stem, hairline
S = 8.0                   # serif overhang beyond a stem
OS = 1.6                  # apex overshoot

def poly(pts): return 'M' + ' L'.join(f'{x:.2f} {y:.2f}' for x, y in pts) + ' Z'
def rect(x0, y0, x1, y1): return poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])

def V():
    # thick diagonal (left) and hairline diagonal (right) meeting in a short flat apex below the baseline
    a, b = 8.0, 8.0 + T                       # thick stroke top edges
    m = 0.270                                 # thick slope dx/dy
    c, d = 63.0, 63.0 + h + .6                # hairline top edges
    n = -0.236                                # hairline slope
    Y = (c - b) / (m - n); X = b + m * Y      # crotch: thick inner edge meets hairline inner edge
    yb = 100 + OS
    shape = poly([(a, 0), (b, 0), (X, Y), (c, 0), (d, 0), (d + n * yb, yb), (a + m * yb, yb)])
    serifs = [rect(a - S, 0, b + S, h), rect(c - S + 1, 0, d + S - 1, h)]
    return [shape] + serifs, d + S - 1

def rot(paths_w):
    """Turn a V through 180° to make the A: x -> W - x, y -> 100 - y."""
    paths, W = paths_w
    out = []
    for p in paths:
        pts = [tuple(map(float, q.split())) for q in p[1:-2].split(' L')]
        out.append(poly([(W - x, 100 - y) for x, y in pts]))
    return out, W

def I():
    return [rect(S, 0, S + T, 100), rect(0, 0, 2 * S + T, h), rect(0, 100 - h, 2 * S + T, 100)], 2 * S + T

def R():
    x0, x1 = S, S + T
    top, mid = 0, 53
    # bowl: outer and inner contours as cubic curves, thick on the right, hairline at top and waist
    bowl = (f'M{x1} {top} L44 {top} C58 {top} 66 10 66 {mid/2:.1f} C66 43 58 {mid} 44 {mid} L{x1} {mid} L{x1} {mid-h} '
            f'L41 {mid-h} C49 {mid-h} 52 42 52 {mid/2:.1f} C52 11 49 {h} 41 {h} L{x1} {h} Z')
    leg = poly([(31, mid - 1), (45.5, mid - 1), (72, 100), (57.5, 100)])
    serifs = [rect(0, 0, x1 + S, h), rect(0, 100 - h, x1 + S, 100), rect(50, 100 - h, 80, 100)]
    return [rect(x0, 0, x1, 100), bowl, leg] + serifs, 80

def L():
    x0, x1 = S, S + T
    foot = 52.0
    return [rect(x0, 0, x1, 100), rect(0, 0, x1 + S, h), rect(0, 100 - h, foot, 100),
            poly([(foot - h, 100), (foot - h, 78), (foot, 78), (foot, 100)])], foot

# letters and the space after each (optically spaced: open diagonals pull closer, stems stand apart)
LETTERS = [('V', V(), 5), ('I', I(), 13), ('R', R(), 3), ('A', rot(V()), 4), ('L', L(), 3), ('A', rot(V()), 0)]

def build(fill='currentColor'):
    x, parts = 0.0, []
    for _, (paths, w), gap in LETTERS:
        parts.append(f'<g transform="translate({x:.2f} 0)">' + ''.join(f'<path d="{p}"/>' for p in paths) + '</g>')
        x += w + gap
    return parts, x

parts, width = build()
vb = f'-2 -4 {width + 4:.1f} 108'
def svg(fill, title=True):
    t = '<title>VIRALA</title>' if title else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="VIRALA">{t}'
            f'<g fill="{fill}">' + ''.join(parts) + '</g></svg>\n')
suffix = '' if CUT == 'display' else '-text'
for name, fill in {'virala-wordmark': 'currentColor', 'virala-wordmark-dusk': '#2C4560', 'virala-wordmark-ivory': '#FAF5F2', 'virala-wordmark-black': '#000000'}.items():
    (OUT / f'{name}{suffix}.svg').write_text(svg(fill))
print(f'wordmark width {width:.1f} units at cap height 100 (ratio {width/100:.2f}:1)')
