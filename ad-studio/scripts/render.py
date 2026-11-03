#!/usr/bin/env python3
"""Render a deterministic HTML ad (window.renderAt(t), window.ready) to MP4.

usage:
  python render.py page.html out.mp4 [--audio mix.wav] [--fps 30] [--size 1080x1920] [--dur 15]
  python render.py page.html stills --stills 1.5,4.2,9.8      # storyboard frames -> stills/t_X.jpg
"""
import argparse, asyncio, os, subprocess
from playwright.async_api import async_playwright

ap = argparse.ArgumentParser()
ap.add_argument('page'); ap.add_argument('out')
ap.add_argument('--audio'); ap.add_argument('--fps', type=float, default=30)
ap.add_argument('--size', default='1080x1920'); ap.add_argument('--dur', type=float)
ap.add_argument('--stills')
a = ap.parse_args()
W, H = map(int, a.size.split('x'))

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(args=['--allow-file-access-from-files'])
        pg = await b.new_page(viewport={'width': W, 'height': H})
        pg.on('pageerror', lambda e: print('PAGE ERROR', e))
        await pg.goto('file://' + os.path.abspath(a.page))
        await pg.evaluate('window.ready')
        if a.stills:
            os.makedirs(a.out, exist_ok=True)
            for t in a.stills.split(','):
                await pg.evaluate(f'renderAt({float(t)})')
                await pg.screenshot(path=f'{a.out}/t_{t}.jpg', type='jpeg', quality=90, timeout=0)
            await b.close(); return
        dur = a.dur or await pg.evaluate('window.DURATION')
        cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'image2pipe', '-framerate', str(a.fps), '-c:v', 'mjpeg', '-i', '-']
        if a.audio: cmd += ['-i', a.audio, '-c:a', 'aac', '-b:a', '192k', '-shortest']
        cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', a.out]
        ff = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        n = int(round(dur * a.fps))
        for f in range(n):
            await pg.evaluate(f'renderAt({f / a.fps})')
            ff.stdin.write(await pg.screenshot(type='jpeg', quality=92, timeout=0))
            if f % int(a.fps * 2) == 0: print(f'{f}/{n}', flush=True)
        ff.stdin.close(); ff.wait(); await b.close()

asyncio.run(main())
