# QA before delivering

Make a contact sheet (`ffmpeg -i ad.mp4 -vf "fps=2,scale=216:384,tile=10x4" -frames:v 1 sheet.jpg`) and full-size frames at every text moment. Check:

- [ ] Duration, resolution and fps are what was promised; audio stream present.
- [ ] Every voice line is audible to the last word (check per-second loudness of the voice track; no silent gap where a line should be).
- [ ] On-screen words match what the voice actually says (the audio wins over the script).
- [ ] No text is cut by the frame edge, covered by the character, or on top of the product.
- [ ] Arabic words are connected and spelled right at full size.
- [ ] No cut-out has leftover background, halos or stray fragments.
- [ ] The product is not oversized; photos are cards or cut-outs, not full-screen.
- [ ] Characters do not pop in again on every cut.
- [ ] No real brand logos, no music unless requested.
- [ ] The ending holds at least 2 s on the name and tagline.
Fix, re-render and re-check before showing the user.
