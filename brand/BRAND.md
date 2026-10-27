# VIRALA Dusk — brand guide

Version 4.1.0-dusk, 2026-10-28. The single source for the website, the app and Instagram: values live in `brand/tokens.json`,
generated with this file and `brand/brand-sheet.html` by `brand/source/brand.py`. Nothing changes in the app until the
Founder approves and HQ records it. Earlier identities are in `brand/archive/` for history only.

**Feeling:** premium, personal, calm, fresh, recognisable. Mostly porcelain and air; Dusk only where it needs weight;
rose on a few italic words only.

## Palette

| Name | Hex | Role |
|---|---|---|
| dusk | `#2C4560` | Signature. Primary buttons, the hero signup card, the Premium card, deep bands, the footer. |
| rose | `#A35866` | The ONE accent. Italic accent words on light grounds; small highlights (numbers, citations) on porcelain and white. On Dusk and night: its tint, roseTint. |
| peach | `#EBB49F` | Glow only: the soft light inside the hero card, the Meet Vira band and the footer, and the mark's back page. Never text. |
| ink | `#1F2A37` | All text on light grounds. No light-grey body text anywhere. |
| mist | `#DCE5EC` | Light blue bands and surfaces. |
| blush | `#F3DCD5` | Soft rose surfaces and bands. |
| porcelain | `#FAF5F2` | Page ground; text and buttons on Dusk. |

Support tones (depth and dark mode only):

| Name | Hex | Role |
|---|---|---|
| duskLight | `#3D5A78` | The lighter end of Dusk gradients. |
| duskDeep | `#1B2B3E` | The deep end of Dusk gradients. |
| night | `#131D29` | Dark mode ground. |
| nightSurface | `#1C2A3A` | Dark mode cards. |
| roseTint | `#E8A6B1` | The one accent on Dusk and night: italic accent words, numbers, the Premium tag, Vira's companion spark. |
| roseLift | `#D98E9B` | The mark's back page on Dusk and night. |
| white | `#FFFDFB` | Raised cards on porcelain. |

Retired everywhere: Fig/plum, lilac, slate #55697C, rust/clay.

**Buttons.** On light grounds: Dusk with porcelain text. On Dusk: porcelain with ink text. In dark mode: porcelain with ink text.

**One accent.** Italic accent words are always rose: #A35866 on light grounds, its tint #E8A6B1 on Dusk and night. Peach is never text; it lives only inside the glow and in the mark.

**Dark mode.** Night blue ground (`#131D29`), porcelain text, mist eyebrows, rose-tint accents; Dusk sections stay Dusk. No brown or plum anywhere.

## Depth

- **glow:** `THE SIGNATURE (as on Instagram): soft peach and rose light inside deep Dusk, in three places only: the hero signup card, the Meet Vira band, the footer. A small bright core fading out (a wide faint glow turns grey on blue): radial-gradient(520px 380px at 84% 0%, rgba(240,178,156,.5), rgba(232,166,177,.22) 42%, transparent 72%), radial-gradient(460px 340px at 6% 104%, rgba(232,166,177,.26), transparent 68%) over the deep band`
- **deepBand:** `linear-gradient(168deg, #2F4A67 0%, #2C4560 40%, #1B2B3E 100%) (plain, for every other deep section)`
- **deepCard:** `radial-gradient(320px 280px at 96% 2%, rgba(240,178,156,.62), rgba(232,166,177,.26) 42%, transparent 74%), radial-gradient(360px 300px at 0% 100%, rgba(232,166,177,.22), transparent 70%), linear-gradient(160deg, #3A5674 0%, #2C4560 50%, #1E3147 100%) (the hero card; the Premium card uses the plain card gradient)`
- **pageGlow:** `radial-gradient(1100px 640px at 100% -12%, rgba(243,220,213,.5), transparent 62%) over porcelain, behind the first screen only`
- **photoBand:** `photo graded saturate(.85) contrast(.95) under a deep Dusk vignette where the text sits: radial rgba(27,43,62,.82 to .22) and linear rgba(44,69,96,.3) to rgba(27,43,62,.55); white text, rose-tint italic; contrast measured from pixels`
- **Rule:** Alternate clearly between porcelain sections and deep Dusk sections; no pale in-between bands. Rose is the one accent. If it starts to look decorated, it is too much.

## Typography

- **Display: Newsreader** — Headlines, card titles, numbers, the footer line. Italic for accent words. weight 440 for h1/h2 (420 italic), 400 for h3, 450 for list and card titles at 18-24 px; optical sizing on; tracking -0.02em at display sizes. SIL Open Font License 1.1 (Google Fonts), free for web and app.
- **Text: Hanken Grotesk** — Body, UI, buttons, labels. weight 400 body, 500 navigation, 600 buttons and labels; labels uppercase with 0.14em tracking. SIL Open Font License 1.1 (Google Fonts), free for web and app.
- **Scale (fluid, one scale on every page):** display 48-96 px, h1 42-76 px, h2 37-64 px, h3 24-32 px, h4 19-22 px, lede 18-22 px, body 17-18 px (line-height 1.65; articles 17-19 px at 1.75, 68 characters), small 15 px, label 12.5 px uppercase.
- **App:** In the app, Newsreader for display and titles; Hanken Grotesk or SF Pro for UI text, following Dynamic Type.
- Alternatives shown to the Founder: Fraunces + Nunito Sans (warmer, rounder); Source Serif 4 + Albert Sans (more editorial).

## The mark

The Life Chapters mark: three pages, unchanged geometry (brand/logo/virala-mark.svg). On light grounds: Dusk front page, rose middle page, peach back page. On Dusk and night: porcelain, peach,
lifted rose. Header, footer, favicon, welcome, social card, 404, Instagram profile, app icon. One mark; no other colourways.

## Vira's symbol

A · Page Spark: VIRALA's own sparkle, built from the mark's soft page curves, with one small companion spark low on the left. On light: Dusk with a rose companion spark. On Dusk and night: porcelain with a rose-tint companion.
The companion spark gently brightens; nothing spins. Static when the visitor prefers reduced motion. Vira page (large, in a soft glow), Premium card, Meet Vira band, welcome. Never in a box on the website. How Vira answers is not decided, so no conversation or chat screen is shown anywhere yet. Files: `brand/vira-symbol/`.

## Icons

- Primary: brand/icon/app-icon-dusk.svg (Dusk gradient, the mark on Dusk) — matches the favicon and Instagram
- Alternative: brand/icon/app-icon-porcelain.svg (the 26 Oct porcelain direction, recoloured)
- iOS: brand/icon/AppIcon.appiconset (Any: Dusk, Dark, Tinted); PNGs in brand/icon/png. Not applied to the app.
- Web: site/assets/favicon.svg, apple-touch-icon.png, icon-192.png, icon-512.png (all Dusk)

## Photography

- Calm and real: soft sea, sky, mist, linen, windows, a notebook. Topic-matched in the Journal.
- No faces, no hand-only close-ups, no fruit, no visible text or logos.
- Graded softly towards Dusk (cooler, slightly desaturated); never filtered to look fake.
- Text on a photo only over a Dusk vignette, with contrast measured from the rendered pixels.
- Licences: Unsplash free licence (or owned), id and photographer recorded in review/PHOTO_RIGHTS_MANIFEST.md.

## Instagram

- Deep Dusk posts with the glow, porcelain Newsreader headlines and one rose-tint italic phrase; porcelain posts with ink and rose italics. Peach only inside the glow.
- The mark small in a corner; the Vira sparkle only on Vira posts.
- Same photo rules as the website.

## Contrast (computed, WCAG 2.x)

| Pair | Ratio | Needs | Use |
|---|---|---|---|
| ink on porcelain | 13.43:1 | 4.5:1 | Body text |
| ink on white | 14.33:1 | 4.5:1 | Text on cards |
| ink on mist | 11.4:1 | 4.5:1 | Text on mist bands |
| ink on blush | 11.08:1 | 4.5:1 | Text on blush bands |
| dusk on porcelain | 9.12:1 | 4.5:1 | Eyebrows, labels |
| dusk on mist | 7.74:1 | 4.5:1 | Eyebrows on mist |
| dusk on blush | 7.53:1 | 4.5:1 | Eyebrows on blush |
| rose on porcelain | 4.68:1 | 4.5:1 | Small rose highlights (numbers, citations) |
| rose on white | 4.99:1 | 4.5:1 | Small rose highlights on cards |
| rose on mist | 3.97:1 | 3.0:1 | Large italic accents on mist surfaces (24 px and up only) |
| porcelain on dusk | 9.12:1 | 4.5:1 | Button label; text on Dusk |
| porcelain on duskLight | 6.62:1 | 4.5:1 | Text on the light end of Dusk gradients |
| roseTint on dusk | 4.95:1 | 4.5:1 | Rose tint on Dusk (accents, numbers) |
| roseTint on duskLight | 3.59:1 | 3.0:1 | Rose-tint italics on the light end of Dusk gradients (large only) |
| ink on porcelain | 13.43:1 | 4.5:1 | Porcelain button label on Dusk (ink on porcelain) |
| ink on roseTint | 7.28:1 | 4.5:1 | The Premium tag |
| porcelain on night | 15.71:1 | 4.5:1 | Dark: text |
| mist on night | 13.32:1 | 4.5:1 | Dark: eyebrows |
| roseTint on night | 8.52:1 | 4.5:1 | Dark: accents |
| porcelain on nightSurface | 13.46:1 | 4.5:1 | Dark: text on cards |
| roseTint on nightSurface | 7.3:1 | 4.5:1 | Dark: accents on cards |

Text on photographs is measured from rendered pixels (review/VERIFICATION.md).
