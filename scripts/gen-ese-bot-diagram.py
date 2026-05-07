"""Generate the architecture sketch for /writing/ese-bot-eu-sovereign-rag/.

Register: engineer's notebook sketch (matches gen-article-diagram.py).
Job: show where each component of the ESE bot stack lives. The article's
prose already names the components and locations; the diagram visualises
the spatial relationship — every byte of the request path stays in the EU
once it crosses the dashed perimeter.

Output: public/diagrams/ese-bot.svg
"""

from __future__ import annotations

import random
from pathlib import Path

# ─── Output ─────────────────────────────────────────────────────────────────

OUT_PATH = Path(__file__).parent.parent / "public" / "diagrams" / "ese-bot.svg"

# ─── Canvas ─────────────────────────────────────────────────────────────────

W, H = 1000, 460

BG = "#0b0b0f"
STROKE = "#8a8895"
STROKE_DIM = "#5a5862"
STROKE_AMBER = "#c88a20"
TEXT = "#b8b5b0"
TEXT_DIM = "#7a7a85"

# ─── Sketch params ──────────────────────────────────────────────────────────

JITTER = 2.5
SEGMENTS_PER_SIDE = 3
STROKE_WIDTH = 1.5
SKETCH_SEED = 9

# ─── Geometry ───────────────────────────────────────────────────────────────

# External: browser (outside the EU perimeter)
BROWSER_X, BROWSER_Y, BROWSER_W, BROWSER_H = 50, 195, 100, 70

# EU envelope (dashed)
EU_X, EU_Y, EU_W, EU_H = 200, 70, 760, 340

# Inside EU
API_X, API_Y, API_W, API_H = 240, 195, 170, 70
WV_X, WV_Y, WV_W, WV_H = 510, 110, 220, 80
MI_X, MI_Y, MI_W, MI_H = 510, 280, 220, 80

# Arrow paths
BROWSER_ARROW_X1 = BROWSER_X + BROWSER_W + 5
BROWSER_ARROW_X2 = API_X - 8
API_OUT_X = API_X + API_W + 5


# ─── Hand-drawn rectangle ──────────────────────────────────────────────────

def rough_rect(x: float, y: float, w: float, h: float, rng: random.Random) -> str:
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER, JITTER)

    points: list[tuple[float, float]] = []
    for i in range(SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w * t), jit(y)))
    for i in range(1, SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w), jit(y + h * t)))
    for i in range(1, SEGMENTS_PER_SIDE + 1):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x + w * (1 - t)), jit(y + h)))
    for i in range(1, SEGMENTS_PER_SIDE):
        t = i / SEGMENTS_PER_SIDE
        points.append((jit(x), jit(y + h * (1 - t))))

    parts = [f"M {points[0][0]:.1f},{points[0][1]:.1f}"]
    for p in points[1:]:
        parts.append(f"L {p[0]:.1f},{p[1]:.1f}")
    parts.append("Z")
    return " ".join(parts)


# ─── Curved arrow path (cubic Bezier) ───────────────────────────────────────

def curve_arrow(x1: float, y1: float, x2: float, y2: float) -> str:
    """Smooth cubic Bezier from (x1,y1) to (x2,y2), bowing horizontally."""
    midx = (x1 + x2) / 2
    return f"M {x1:.1f},{y1:.1f} C {midx:.1f},{y1:.1f} {midx:.1f},{y2:.1f} {x2:.1f},{y2:.1f}"


# ─── SVG ────────────────────────────────────────────────────────────────────

ARROW_MARKER = f"""
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="7" markerHeight="7" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="{STROKE}"/>
  </marker>
</defs>
"""


def diagram_layer(rng: random.Random) -> str:
    eu = rough_rect(EU_X, EU_Y, EU_W, EU_H, rng)
    browser = rough_rect(BROWSER_X, BROWSER_Y, BROWSER_W, BROWSER_H, rng)
    api = rough_rect(API_X, API_Y, API_W, API_H, rng)
    wv = rough_rect(WV_X, WV_Y, WV_W, WV_H, rng)
    mi = rough_rect(MI_X, MI_Y, MI_W, MI_H, rng)

    # arrow targets
    api_cy = API_Y + API_H / 2
    wv_cy = WV_Y + WV_H / 2
    mi_cy = MI_Y + MI_H / 2
    arrow_to_wv = curve_arrow(API_OUT_X, api_cy, WV_X - 8, wv_cy)
    arrow_to_mi = curve_arrow(API_OUT_X, api_cy, MI_X - 8, mi_cy)

    return f"""
  <!-- eu envelope (dashed) -->
  <path d="{eu}" fill="none" stroke="{STROKE_DIM}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"
        stroke-dasharray="6 5"/>
  <text x="{EU_X + 14}" y="{EU_Y + 24}"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="18" font-style="italic" fill="{TEXT_DIM}">eu</text>

  <!-- browser (external) -->
  <path d="{browser}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{BROWSER_X + BROWSER_W/2}" y="{BROWSER_Y + BROWSER_H/2 + 7}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="20" fill="{TEXT}">browser</text>

  <!-- browser → api -->
  <line x1="{BROWSER_ARROW_X1}" y1="{api_cy}" x2="{BROWSER_ARROW_X2}" y2="{api_cy}"
        stroke="{STROKE}" stroke-width="{STROKE_WIDTH}" stroke-linecap="round"
        marker-end="url(#arr)"/>

  <!-- api -->
  <path d="{api}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{API_X + API_W/2}" y="{API_Y + API_H/2 + 8}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="22" fill="{TEXT}">api · de</text>

  <!-- api → weaviate (curved) -->
  <path d="{arrow_to_wv}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round"
        marker-end="url(#arr)"/>

  <!-- weaviate -->
  <path d="{wv}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{WV_X + WV_W/2}" y="{WV_Y + WV_H/2 + 9}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="24" fill="{TEXT}">weaviate · nl</text>

  <!-- api → mistral (curved) -->
  <path d="{arrow_to_mi}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round"
        marker-end="url(#arr)"/>

  <!-- mistral -->
  <path d="{mi}" fill="none" stroke="{STROKE}"
        stroke-width="{STROKE_WIDTH}" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="{MI_X + MI_W/2}" y="{MI_Y + MI_H/2 + 9}"
        text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="24" fill="{TEXT}">mistral · fr</text>
"""


# ─── Compose ────────────────────────────────────────────────────────────────

def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SKETCH_SEED)
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" role="img"
     aria-label="A browser box outside a dashed EU perimeter, with an arrow leading into an API box labelled 'api · de'. Inside the EU, the api connects to two further boxes: 'weaviate · nl' and 'mistral · fr'.">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  {ARROW_MARKER}
  {diagram_layer(rng)}
</svg>
"""
    OUT_PATH.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT_PATH}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
