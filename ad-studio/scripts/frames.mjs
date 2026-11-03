// Resumable frame dump for Lemo-Opuscar films (slow 3D renders). Copy into lemo-opuscar/core/render/.
// node core/render/frames.mjs <film dir> <out dir> <fps> <start> <end> <step> [--q 's=0.6667'] [--size 720x1280]
// Run several in parallel with different <start> and the same <step> (e.g. start 0 and 1, step 2).
import fs from 'fs'; import path from 'path';
import { openDemo, closeServer, takeSize } from './page.mjs';
const args = process.argv.slice(2); const take = k => { const i = args.indexOf(k); return i >= 0 ? args.splice(i, 2)[1] : null; };
const { w, h } = takeSize(args), q = take('--q') || '';
const [dir, out, fps, a, b, st] = args; fs.mkdirSync(out, { recursive: true });
const { browser, page } = await openDemo(dir, { w, h, q });
for (let f = +a; f < +b; f += +st) {
  const fn = path.join(out, `f_${String(f).padStart(4, '0')}.jpg`); if (fs.existsSync(fn)) continue;
  await page.evaluate(t => window.render(t), f / +fps);
  await page.screenshot({ path: fn + '.tmp.jpg', type: 'jpeg', quality: 94, timeout: 0 }); fs.renameSync(fn + '.tmp.jpg', fn);
  if (f % 24 === 0) console.log(f, new Date().toISOString());
}
await browser.close(); closeServer();
