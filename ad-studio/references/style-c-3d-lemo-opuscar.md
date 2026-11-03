# Style C — 3D product film in code (Lemo-Opuscar)

Uses the open-source library **Lemo-Opuscar** by **Lemomo** — https://github.com/lemomo-ai/lemo-opuscar (MIT code; demo films CC BY 4.0). Always credit it in the project and when the user publishes.

## Install (once)
In Claude Code:
```
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```
or clone it:
```
git clone --depth 1 https://github.com/lemomo-ai/lemo-opuscar.git
cd lemo-opuscar && npm install
```
If a style's font file is missing (e.g. `InterTight-var.woff2` in the glass-product demo), get it from npm: `npm pack @fontsource-variable/inter-tight` and copy `inter-tight-latin-wght-normal.woff2`.

## Pick a style
Show the user the styles that fit ads, one line each, and let them choose:
- **Glass Product Render** (`styles/glass-product`) — dark studio, glass, light sweeps, exploded view. Watches, earbuds, speakers, gadgets, skincare tech.
- **Exploded Teardown** (`styles/teardown`) — technical parts spread with labels. Hardware.
- **Dark Tech Keynote** (`styles/dark-keynote`) — launch-event look. Apps, SaaS.
- **Living Screencast** (`styles/living-screencast`) — app screens that come alive. App ads.
- **Art Deco**, **One-line Drawing**, **Impasto Oil Painting** — luxury, brand story, emotional ads.
Read the chosen `STYLE.md` fully before designing.

## Choose the product honestly
- An exploded view only works for products that really come apart in layers (watch: glass, light ring, display, case, circuit board, battery, sensor back; earbuds; camera). Never "explode" a perfume bottle or a mug — it looks absurd.
- The product is always fictional in shape and name; never reproduce a real product's silhouette or logo.
- Find "the invisible thing the product does" and make it visible as light (a heartbeat as a pulsing light ring, sound as light waves, charge filling a glass cell).

## Build
- New film folder `films/<name>/` with `index.html` + `main.js`. Reuse the style's `studio.js` and material helpers (`glass`, `frosted`, `guideMat`, `setPulses`) from `styles/<style>/demo/`; write your own geometry.
- Vertical ad: `W=1080, H=1920`, camera fov 30–40, product ~40% of height.
- Shots (≈20 s): dark sweep reveal → name title → macro on the hero detail → exploded view (ease-out apart, hover, quick ease-in snap on a beat) → lit from inside → top-down floor light rings → hero end card with name + tagline.
- Text overlay on a 2D canvas: ultra-thin wide-tracked name, Arabic lines in a light Arabic font weight inside frosted-glass bars.
- Storyboard: render 7 stills at half size (`--q half=1 --size 540x960`) first.

## Render speed (tell the user)
- With a GPU (Mac Apple Silicon): seconds per frame or less.
- Without a GPU (cloud/Linux): about 5 s per frame at half size, 10 s at 720p, 15–20 s at 1080p. A 20 s film = 480 frames. Render frames to disk with `scripts/frames.mjs` (resumable), several workers in parallel, then join and upscale:
```
ffmpeg -framerate 24 -i frames/f_%04d.jpg -i sfx.wav -vf "scale=1080:1920:flags=lanczos" -c:v libx264 -preset veryfast -crf 17 -pix_fmt yuv420p -c:a aac -shortest ad.mp4
```
- Set screenshot timeouts to 0; long frames otherwise abort the render.

## Sound
Effects only (no music unless asked): glass shimmer on each light sweep, soft air on cuts, small metal ticks when parts separate, a short silence then a snap (cluster of clicks + inharmonic glass chord + low sub) on reassembly, heartbeat or pulses synced to the light.
