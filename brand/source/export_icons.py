"""Render the VIRALA Dusk icon set to PNG with headless Chrome (no other tools).
    python3 -I brand/source/export_icons.py <fresh empty scratch dir>
Writes (opaque sRGB PNGs):
    brand/icon/png/app-icon-<dusk|porcelain|dark|tinted>-1024.png, instagram-profile-1080.png (Dusk, circle-safe)
    brand/icon/AppIcon.appiconset/   Xcode single-size set: Any (Dusk), Dark, Tinted + Contents.json (not applied to the app)
    site/assets/apple-touch-icon.png (180), icon-192.png, icon-512.png   web icons from the Dusk icon
"""
import json, math, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
B = ROOT / 'brand'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
TMP = Path(sys.argv[1]).resolve()
assert TMP.is_dir() and not any(TMP.iterdir()), 'pass a fresh, empty scratch directory'


def render(svg, size, out):
    big = max(size, 1024)  # headless Chrome clamps small windows: render large, then resample down
    html = TMP / f'{out.parent.name}-{out.stem}.html'
    html.write_text(f'<!doctype html><html><body style="margin:0;background:#fff"><img src="{svg.as_uri()}" width="{big}" height="{big}" style="display:block"></body></html>')
    png = TMP / f'{out.parent.name}-{out.stem}.png'
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1', '--allow-file-access-from-files',
                    f'--window-size={big},{big}', f'--screenshot={png}', html.as_uri()], capture_output=True, timeout=60)
    if big != size:
        subprocess.run(['sips', '-z', str(size), str(size), str(png), '--out', str(png)], capture_output=True, check=True)
    subprocess.run(['sips', '-s', 'format', 'png', '--matchTo', '/System/Library/ColorSync/Profiles/sRGB Profile.icc', str(png), '--out', str(out)],
                   capture_output=True, check=True)
    info = subprocess.run(['sips', '-g', 'pixelWidth', '-g', 'pixelHeight', str(out)], capture_output=True, text=True).stdout
    assert f'pixelWidth: {size}' in info and f'pixelHeight: {size}' in info, info


PNG = B / 'icon/png'
PNG.mkdir(parents=True, exist_ok=True)
for name in ('dusk', 'porcelain', 'dark', 'tinted'):
    render(B / f'icon/app-icon-{name}.svg', 1024, PNG / f'app-icon-{name}-1024.png')
render(B / 'icon/app-icon-dusk.svg', 1080, PNG / 'instagram-profile-1080.png')
far = math.hypot(544 * .58 / 736 / 2, .58 / 2)  # the mark's farthest point from the centre, as a share of the side
assert far < .5, far  # inside Instagram's circular crop

SET = B / 'icon/AppIcon.appiconset'
SET.mkdir(parents=True, exist_ok=True)
for src, dst in (('dusk', 'AppIcon-1024.png'), ('dark', 'AppIcon-Dark-1024.png'), ('tinted', 'AppIcon-Tinted-1024.png')):
    shutil.copyfile(PNG / f'app-icon-{src}-1024.png', SET / dst)
(SET / 'Contents.json').write_text(json.dumps({'images': [
    {'filename': 'AppIcon-1024.png', 'idiom': 'universal', 'platform': 'ios', 'size': '1024x1024'},
    {'appearances': [{'appearance': 'luminosity', 'value': 'dark'}], 'filename': 'AppIcon-Dark-1024.png', 'idiom': 'universal', 'platform': 'ios', 'size': '1024x1024'},
    {'appearances': [{'appearance': 'luminosity', 'value': 'tinted'}], 'filename': 'AppIcon-Tinted-1024.png', 'idiom': 'universal', 'platform': 'ios', 'size': '1024x1024'}],
    'info': {'author': 'xcode', 'version': 1}}, indent=2) + '\n')

WEB = ROOT / 'site/assets'
for name, size in (('apple-touch-icon.png', 180), ('icon-192.png', 192), ('icon-512.png', 512)):
    render(B / 'icon/app-icon-dusk.svg', size, WEB / name)
print('icon set written: brand/icon/png, brand/icon/AppIcon.appiconset, site/assets web icons')
