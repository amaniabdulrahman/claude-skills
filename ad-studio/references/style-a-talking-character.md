# Style A — Talking character, 2D motion graphics

Example: a grandmother in a traditional face mask judges modern iced lattes, then praises a traditional coffee brand. Warm cream background, her portrait at the bottom, product cut-outs and words animating above.

## Assets
1. **Character sheet**: one image with 4 expressions of the same character (front, bust): skeptical, shocked, laughing, eyes closed smiling. Cut each one out with rembg. Prompt in `image-prompts.md`.
2. **Product**: the real product photo with its name printed on it (generate it with the name if fictional). Cut it out.
3. **Story photos**: 2–4 supporting images (the "bad" alternative, the ingredients, the ritual), cut out when possible.
4. **Voice**: one file per line. Pick an older/younger voice to match the character. Test one line first for dialect and pronunciation.

## Structure (≈19 s, 9:16)
| Time | Shot | On screen |
|---|---|---|
| 0–1 | Hook | The "problem" object cut-out + first word big |
| 1–2.5 | Detail | Callout labels pointing at what is wrong |
| 2.5–4.3 | Reaction | Orange/brand full-colour background, character large, punchline word |
| 4.3–9.6 | The good way | Ingredients / ritual cut-outs, character smiling |
| 9.6–13.5 | Product | Product slams in on brand colour, then floats with particles |
| 13.5–end | End card | Brand name, tagline, small CTA button with a cursor tap |

## Build
- Copy `templates/ad_template.html`; put each shot in the `SC` list `[t0, t1, () => html]`.
- Character: `<img>` bottom-right, height ~520 px (1080×1920), switch expression by time. On the reaction shot, show the character large (height ~1150 px).
- Word timings: take the speech start of each line from silencedetect, then space words by syllables.
- Render with `scripts/render.py`, mix voice + `scripts/sfx.py` effects.
