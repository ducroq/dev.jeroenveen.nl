"""Generate the article diagram for /writing/the-work-is-splitting/.

Register: engineer's notebook sketch, not management-book infographic.
- Hand-drawn-style boxes (jittered path corners, like a quick whiteboard rect)
- Plain dark background — no atmosphere, no gradient
- Lowercase monospace labels — terminal/notebook feel
- No BEFORE/AFTER headers, no bottom tagline
- Single small accent: amber stroke on the "make" box

Pattern follows scripts/gen-social-image.py: parameters at the top, edit + rerun.
Output: public/diagrams/the-work-is-splitting.svg
"""

from __future__ import annotations

import random
from pathlib import Path

# ─── Output ─────────────────────────────────────────────────────────────────

OUT_PATH = Path(__file__).parent.parent / "public" / "diagrams" / "the-work-is-splitting.svg"

# ─── Canvas ─────────────────────────────────────────────────────────────────

W, H = 1000, 460

BG = "#0b0b0f"           # site --bg
STROKE = "#8a8895"       # muted neutral (pencil-on-dark)
STROKE_AMBER = "#c88a20" # --amber-dim, not full amber
TEXT = "#b8b5b0"         # warm off-white, like pencil
TEXT_DIM = "#7a7a85"

# ─── Sketch params ──────────────────────────────────────────────────────────

JITTER = 2.5             # max corner displacement in px
SEGMENTS_PER_SIDE = 3    # extra points along each side for organic curves
STROKE_WIDTH = 1.5
SKETCH_SEED = 4          # bump to reseed the jitter pattern

# ─── Diagram geometry ───────────────────────────────────────────────────────

WORK_X, WORK_Y, WORK_W, WORK_H = 100, 120, 260, 170
MAKE_X, MAKE_Y, MAKE_W, MAKE_H = 580, 170, 80, 55
VAL_X, VAL_Y, VAL_W, VAL_H = 580, 255, 340, 170

ARROW_Y = WORK_Y + WORK_H / 2
ARROW_X1, ARROW_X2 = WORK_X + WORK_W + 30, MAKE_X - 30


# ─── Hand-drawn rectangle as a single closed path ───────────────────────────

def rough_rect(x: float, y: float, w: float, h: float, rng: random.Random) -> str:
    """Return an SVG path 'd' attribute for a wobbly rectangle.

    Each side gets SEGMENTS_PER_SIDE-1 intermediate points with small jitter,
    plus jittered corners. Closed path.
    """
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER, JITTER)

    points: list[tuple[float, float]] = []

    # top edge L→R
    for i in range(SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w * t), jit(y)))
    # right edge T→B (skip first, shared with top-right corner)
    for i in range(1, SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w), jit(y + h * t)))
    # bottom edge R→L
    for i in range(1, SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w * (1 - t)), jit(y + h)))
    # left edge B→T (skip first and last, both shared)
    for i in range(1, SEGMENTS_PER_SIDE):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x), jit(y + h * (1 - t))))

    parts = [f"M {points[0][0]:.1f},{points[0][1]:.1f}"]
    for p in points[1:]:
        parts.append(f"L {p[0]:.1f},{p[1]:.1f}")
    parts.append("Z")
    return " ".join(parts)


# ─── Arrow ──────────────────────────────────────────────────────────────────

ARROW_MARKER = f"""
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="7" markerHeight="7" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="{STROKE}"/>
  </marker>
</defs>
"""


# ─── Foreground ────────────────────────────────────────────────────────────

def diagram_layer(rng: random.Random) -> str:
    work_path = rough_rect(WORK_X, WORK_Y, WORK_W, WORK_H, rng)
    make_path = rough_rect(MAKE_X, MAKE_Y, MAKE_W, MAKE_H, rng)
    val_path = rough_rect(VAL_X, VAL_Y, VAL_W, VAL_H, rng)

    return f"""
  <!-- work -->
  <path d="{work_path}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{WORK_X + WORK_W/2}" y="{WORK_Y + WORK_H/2 + 11}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="32" fill="{TEXT}">work</text>
  <text x="{WORK_X}" y="{WORK_Y + WORK_H + 36}"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="20" font-style="italic" fill="{TEXT_DIM}">produce + validate, entangled</text>

  <!-- arrow -->
  <line x1="{ARROW_X1}" y1="{ARROW_Y}" x2="{ARROW_X2}" y2="{ARROW_Y}"
        stroke="{STROKE}" stroke-width="{STROKE_WIDTH}" stroke-linecap="round"
        marker-end="url(#arr)"/>

  <!-- make -->
  <path d="{make_path}" fill="none" stroke="{STROKE_AMBER}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{MAKE_X + MAKE_W/2}" y="{MAKE_Y + MAKE_H/2 + 8}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="22" fill="{TEXT}">make</text>

  <!-- validate -->
  <path d="{val_path}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{VAL_X + VAL_W/2}" y="{VAL_Y + VAL_H/2 + 14}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="42" fill="{TEXT}">validate</text>
"""


# ─── Compose ────────────────────────────────────────────────────────────────

def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SKETCH_SEED)
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" role="img"
     aria-label="A small box labelled 'work' with the note 'produce + validate, entangled', followed by an arrow pointing to a small 'make' box and a much larger 'validate' box.">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  {ARROW_MARKER}
  {diagram_layer(rng)}
</svg>
"""
    OUT_PATH.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT_PATH}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
