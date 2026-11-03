#!/usr/bin/env python3
"""Soft sound effects for ads, synthesised with numpy (no music, no samples).

Edit the CUE list at the bottom, then:  python sfx.py out.wav 20
Kinds: whoosh, pop, click, thump, chime, shimmer, heart, snap, air
"""
import sys, wave
import numpy as np
from scipy.signal import butter, lfilter

SR = 48000
OUT, DUR = (sys.argv[1] if len(sys.argv) > 1 else 'sfx.wav'), float(sys.argv[2]) if len(sys.argv) > 2 else 20
buf = np.zeros(int(SR * DUR)); rng = np.random.default_rng(7)

def bp(x, lo, hi): b, a = butter(2, [lo / (SR / 2), hi / (SR / 2)], 'band'); return lfilter(b, a, x)
def lp(x, f): b, a = butter(2, f / (SR / 2)); return lfilter(b, a, x)
def add(t0, y, g):
    i = int(SR * t0); y = y / (np.abs(y).max() + 1e-9) * g; n = min(len(y), len(buf) - i)
    if n > 0: buf[i:i + n] += y[:n]
def tt(d): return np.arange(int(SR * d)) / SR

def whoosh(t0, g=.12, d=.6):
    t = tt(d); x = rng.standard_normal(len(t)); env = np.sin(np.pi * t / d) ** 2
    add(t0, np.concatenate([bp(x[:len(x)//2], 250, 1700), bp(x[len(x)//2:], 400, 2800)]) * env, g)
def pop(t0, g=.15, f=600):
    t = tt(.09); add(t0, np.sin(2 * np.pi * (f * np.exp(-t * 18)) * t * 3) * np.exp(-t * 45), g)
def click(t0, g=.12):
    t = tt(.04); add(t0, bp(rng.standard_normal(len(t)), 1500, 6000) * np.exp(-t * 120), g)
def thump(t0, g=.35, f=60):
    t = tt(.5); y = np.sin(2 * np.pi * f * t) * np.exp(-t * 7); y[:300] *= np.linspace(0, 1, 300); add(t0, y, g)
def chime(t0, g=.08, f=1500):
    t = tt(1.2); add(t0, (np.sin(2 * np.pi * f * t) + .4 * np.sin(2 * np.pi * f * 2.01 * t)) * np.exp(-t * 4), g)
def shimmer(t0, g=.12, d=1.5):
    t = tt(d); env = np.sin(np.pi * t / d) ** 2; x = bp(rng.standard_normal(len(t)), 3000, 9000) * env
    for f in (1760, 1760 * 2.76, 1760 * 5.4): x += np.sin(2 * np.pi * f * t) * env * .08
    add(t0, x, g)
def heart(t0, g=.3):
    for dt, k in ((0, 1), (.16, .7)):
        t = tt(.25); y = np.sin(2 * np.pi * np.cumsum(55 - 25 * t) / SR) * np.exp(-t * 18); add(t0 + dt, y, g * k)
def snap(t0, g=.3):
    for k in range(5): click(t0 + k * .004, g * .8)
    t = tt(2); add(t0, sum(np.sin(2 * np.pi * 660 * m * t) * np.exp(-t * (2 + m)) for m in (1, 2.76, 5.4)), g * .6); thump(t0, g, 42)
def air(t0, g=.08, d=.5):
    t = tt(d); add(t0, lp(rng.standard_normal(len(t)), 2000) * (t / d) ** 2, g)

# ---------- CUE LIST: (time, kind, gain) ----------
CUES = [
    (0.05, 'whoosh', .10), (4.0, 'whoosh', .12), (9.0, 'whoosh', .12),
    (1.2, 'pop', .14), (9.3, 'chime', .09), (9.3, 'thump', .30),
]
for t0, kind, g in CUES: globals()[kind](t0, g)

out = buf / max(1e-9, np.abs(buf).max()) * .8
with wave.open(OUT, 'w') as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((out * 32767).astype(np.int16).tobytes())
print('wrote', OUT)
