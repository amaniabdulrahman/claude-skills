# Style B — Follow a reference ad

The user brings a reference video they love. You make their product in the same *feeling*, never a copy of its shots, brand, text or logo.

## Study the reference
```
mkdir -p ref && ffmpeg -i reference.mp4 -vf "fps=2,scale=320:-2,tile=8x4" -frames:v 1 ref/grid.jpg
ffmpeg -i reference.mp4 -vf fps=1 ref/f_%03d.jpg
```
Write down in 6–8 bullets: background (light/dark, texture), how the product appears (cut-out, floating, rotating), typography (weight, size, how words build), colour accents, transitions, pacing (seconds per shot), ending. Show this list to the user before building — it is what you will imitate.

## Common premium "manifesto" grammar (works for food, cosmetics, lifestyle)
- Light warm background, a huge faint brand word as watermark.
- Product cut-out floating with soft shadow and a slow bob.
- Elegant words building one by one; one accent colour for key words.
- A thick brand-colour ribbon sweeping behind the product on the brand line.
- Framed photo cards sliding in from the sides with short captions (moments, places, people — modest and culturally appropriate).
- Blurred foreground particles (beans, petals, spices) drifting for depth.
- Ending: product hero + name + tagline.

## Script for this style
Short emotional lines ("It's not just coffee… it's the gathering."). Voice calm and warm, or no voice with on-screen words only.

## Build
Same template and render script as style A. Cards: white padding 16 px, radius 22 px, slight rotation ±4°, slide in from the side with back easing.
