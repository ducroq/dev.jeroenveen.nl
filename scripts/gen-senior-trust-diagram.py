"""Generate the article diagram for /writing/senior-developers-trust-ai-less/.

Register: engineer's notebook sketch, vectorised onto the site's dark canvas.
Two-column comparison (junior / senior) with a vertical "VALIDATION" spine.
Each column shows a laptop with abstracted code lines. The senior side adds
annotation arrows pointing at suspect code, with margin notes. A single bottom
caption carries the article's thesis sentence.

Structural reference: `memory/visual-references/senior-trust-gemini-draft.jpg`
(Gemini Imagen draft). The reference was on white graph paper; this version
keeps the sketch register but switches to the site's dark canvas to match
existing diagrams in the project (`the-work-is-splitting.svg`, ese-bot).

Voice constraint: no em-dashes anywhere, including the SVG-embedded text.

Pattern follows scripts/gen-article-diagram.py: parameters at the top, edit + rerun.
Output: public/diagrams/senior-developers-trust-ai-less.svg
"""

from __future__ import annotations

import random
from pathlib import Path

# ─── Output ─────────────────────────────────────────────────────────────────

OUT_PATH = (
    Path(__file__).parent.parent
    / "public" / "diagrams" / "senior-developers-trust-ai-less.svg"
)

# ─── Canvas ─────────────────────────────────────────────────────────────────

W, H = 1000, 540

BG = "#0b0b0f"           # site --bg
STROKE = "#8a8895"       # muted neutral (pencil-on-dark)
STROKE_AMBER = "#c88a20" # --amber-dim, accent for the suspect lines
TEXT = "#b8b5b0"         # warm off-white, like pencil
TEXT_DIM = "#7a7a85"

# ─── Sketch params ──────────────────────────────────────────────────────────

JITTER = 2.5
SEGMENTS_PER_SIDE = 3
STROKE_WIDTH = 1.5
SKETCH_SEED = 7

# ─── Layout ─────────────────────────────────────────────────────────────────

LEFT_X = 300          # left column centre
RIGHT_X = 700         # right column centre
SPINE_X = 500         # vertical "VALIDATION" spine

# Laptop screen
SCREEN_W = 220
SCREEN_H = 150
SCREEN_TOP = 130

# Laptop base (trapezoid)
BASE_PAD = 28
BASE_H = 18

# Code lines inside screen
CODE_WIDTH_FRACS = [0.72, 0.50, 0.85, 0.58, 0.74]   # relative widths, top → bottom

# Headers
HEADER_Y = 80

# Time stamps
TIME_Y = SCREEN_TOP + SCREEN_H + BASE_H + 60

# Spine
SPINE_Y_TOP = 110
SPINE_Y_BOTTOM = 440
SPINE_LETTERS = "VALIDATION"

# Caption
CAPTION_Y = 490


# ─── Path helpers ───────────────────────────────────────────────────────────

def rough_rect(x: float, y: float, w: float, h: float, rng: random.Random) -> str:
    """Return SVG path 'd' for a wobbly rectangle (closed)."""
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


def rough_line(
    x1: float, y1: float, x2: float, y2: float,
    rng: random.Random, segments: int = 4, amp: float = 0.6,
) -> str:
    """Wobbly line. `amp` scales the jitter relative to JITTER."""
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER * amp, JITTER * amp)

    parts = [f"M {x1:.1f},{y1:.1f}"]
    for i in range(1, segments):
        t = i / segments
        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t
        parts.append(f"L {jit(x):.1f},{jit(y):.1f}")
    parts.append(f"L {x2:.1f},{y2:.1f}")
    return " ".join(parts)


# ─── Laptop ─────────────────────────────────────────────────────────────────

def laptop(cx: float, rng: random.Random, accent_line_idx: int | None = None) -> str:
    """Draw a laptop centred on cx: screen + base + code lines inside the screen.

    If `accent_line_idx` is given, that code line gets the amber stroke
    (marks the suspect line in the senior column).
    """
    screen_x = cx - SCREEN_W / 2
    screen_y = SCREEN_TOP
    screen_path = rough_rect(screen_x, screen_y, SCREEN_W, SCREEN_H, rng)

    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER * 0.5, JITTER * 0.5)

    base_y = screen_y + SCREEN_H + 4
    base_path = (
        f"M {jit(cx - SCREEN_W/2):.1f},{jit(base_y):.1f} "
        f"L {jit(cx + SCREEN_W/2):.1f},{jit(base_y):.1f} "
        f"L {jit(cx + SCREEN_W/2 + BASE_PAD):.1f},{jit(base_y + BASE_H):.1f} "
        f"L {jit(cx - SCREEN_W/2 - BASE_PAD):.1f},{jit(base_y + BASE_H):.1f} Z"
    )

    line_spacing = SCREEN_H / (len(CODE_WIDTH_FRACS) + 1)
    code_lines = []
    for i, width_frac in enumerate(CODE_WIDTH_FRACS):
        ly = screen_y + line_spacing * (i + 1)
        lx1 = screen_x + 20
        lx2 = lx1 + (SCREEN_W - 40) * width_frac
        stroke = STROKE_AMBER if i == accent_line_idx else STROKE
        code_lines.append(
            f'<path d="{rough_line(lx1, ly, lx2, ly, rng, 3, amp=0.4)}" '
            f'fill="none" stroke="{stroke}" stroke-width="{STROKE_WIDTH}" '
            f'stroke-linecap="round"/>'
        )

    return (
        f'<path d="{screen_path}" fill="none" stroke="{STROKE}" '
        f'stroke-width="{STROKE_WIDTH}" stroke-linecap="round" '
        f'stroke-linejoin="round"/>'
        f'<path d="{base_path}" fill="none" stroke="{STROKE}" '
        f'stroke-width="{STROKE_WIDTH}" stroke-linecap="round" '
        f'stroke-linejoin="round"/>'
        + "".join(code_lines)
    )


# ─── Annotation arrow + note ────────────────────────────────────────────────

ARROW_MARKER = f"""
<defs>
  <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="{STROKE}"/>
  </marker>
  <marker id="arr-amber" viewBox="0 0 10 10" refX="9" refY="5"
          markerWidth="6" markerHeight="6" orient="auto">
    <path d="M0,0 L10,5 L0,10 z" fill="{STROKE_AMBER}"/>
  </marker>
</defs>
"""


def annotation_arrow(
    x1: float, y1: float, x2: float, y2: float,
    rng: random.Random, amber: bool = False,
) -> str:
    """Wobbly annotation arrow from (x1,y1) note end to (x2,y2) target."""
    stroke = STROKE_AMBER if amber else STROKE
    marker = "arr-amber" if amber else "arr"
    d = rough_line(x1, y1, x2, y2, rng, segments=5, amp=0.5)
    return (
        f'<path d="{d}" fill="none" stroke="{stroke}" '
        f'stroke-width="{STROKE_WIDTH}" stroke-linecap="round" '
        f'marker-end="url(#{marker})"/>'
    )


# ─── Compose ────────────────────────────────────────────────────────────────

def diagram_layer(rng: random.Random) -> str:
    parts: list[str] = []

    # Headers: "junior", "senior" (lowercase mono, project convention)
    parts.append(
        f'<text x="{LEFT_X}" y="{HEADER_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="30" fill="{TEXT}">junior</text>'
    )
    parts.append(
        f'<text x="{RIGHT_X}" y="{HEADER_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="30" fill="{TEXT}">senior</text>'
    )

    # Laptops
    parts.append(laptop(LEFT_X, rng))
    parts.append(laptop(RIGHT_X, rng, accent_line_idx=2))  # amber: suspect line

    # Junior side annotation: "looks good"  →  top of left screen
    junior_note_x, junior_note_y = 70, 170
    parts.append(
        f'<text x="{junior_note_x}" y="{junior_note_y}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="17" fill="{TEXT_DIM}">looks good</text>'
    )
    parts.append(annotation_arrow(
        junior_note_x + 80, junior_note_y - 4,
        LEFT_X - SCREEN_W/2 + 15, SCREEN_TOP + 20,
        rng,
    ))

    # Senior side: two notes pointing into the screen
    # Note 1 (amber): "wait, what is this lookup doing" → suspect (accent) line
    note1_x, note1_y = 820, 175
    parts.append(
        f'<text x="{note1_x}" y="{note1_y}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" fill="{TEXT}">wait, what is</text>'
    )
    parts.append(
        f'<text x="{note1_x}" y="{note1_y + 19}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" fill="{TEXT}">this lookup</text>'
    )
    parts.append(
        f'<text x="{note1_x}" y="{note1_y + 38}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" fill="{TEXT}">doing</text>'
    )
    # Arrow from note 1 to the amber code line (index 2).
    # End x lands well inside the line (40px short of screen right edge), not on the frame.
    line_spacing = SCREEN_H / (len(CODE_WIDTH_FRACS) + 1)
    suspect_y = SCREEN_TOP + line_spacing * 3  # index 2 → row 3 from top
    parts.append(annotation_arrow(
        note1_x - 6, note1_y + 14,
        RIGHT_X + SCREEN_W/2 - 60, suspect_y,
        rng, amber=True,
    ))

    # Note 2: "wrong boundary" → lower code region of senior screen.
    # Bumped up slightly to clear the laptop base and avoid crowding.
    note2_x, note2_y = 820, 250
    parts.append(
        f'<text x="{note2_x}" y="{note2_y}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" fill="{TEXT}">wrong</text>'
    )
    parts.append(
        f'<text x="{note2_x}" y="{note2_y + 19}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" fill="{TEXT}">boundary</text>'
    )
    boundary_y = SCREEN_TOP + line_spacing * 4
    # End x sits in the middle of the (shorter) 4th line, not at the screen frame.
    parts.append(annotation_arrow(
        note2_x - 6, note2_y + 8,
        RIGHT_X + SCREEN_W/2 - 110, boundary_y,
        rng,
    ))

    # Time stamps below the laptops
    parts.append(
        f'<text x="{LEFT_X}" y="{TIME_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="18" font-style="italic" fill="{TEXT_DIM}">seconds</text>'
    )
    parts.append(
        f'<text x="{RIGHT_X}" y="{TIME_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="18" font-style="italic" fill="{TEXT_DIM}">15 minutes</text>'
    )

    # Vertical guide stroke FIRST so the letters sit on top of it.
    parts.append(
        f'<path d="{rough_line(SPINE_X, SPINE_Y_TOP - 18, SPINE_X, SPINE_Y_BOTTOM + 22, random.Random(SKETCH_SEED + 1), segments=10, amp=0.4)}" '
        f'fill="none" stroke="{STROKE}" stroke-width="1.5" '
        f'stroke-linecap="round" opacity="0.55"/>'
    )
    # Vertical spine "VALIDATION" (uppercase reads better stacked)
    n = len(SPINE_LETTERS)
    step = (SPINE_Y_BOTTOM - SPINE_Y_TOP) / (n - 1)
    for i, ch in enumerate(SPINE_LETTERS):
        ly = SPINE_Y_TOP + step * i
        parts.append(
            f'<text x="{SPINE_X}" y="{ly}" text-anchor="middle" '
            f'font-family="JetBrains Mono, ui-monospace, monospace" '
            f'font-size="32" font-weight="500" fill="{TEXT}">{ch}</text>'
        )

    # Bottom caption (article's thesis sentence)
    parts.append(
        f'<text x="{W/2}" y="{CAPTION_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="20" fill="{TEXT}">seniors trust less because they have validated more.</text>'
    )

    return "\n  ".join(parts)


# ─── Main ───────────────────────────────────────────────────────────────────

ARIA_LABEL = (
    "Two-column hand-drawn sketch. Left column labelled 'junior' showing a "
    "laptop with abstracted code lines, annotation 'looks good' and time "
    "stamp 'seconds'. Right column labelled 'senior' showing the same laptop "
    "with annotations 'wait, what is this lookup doing' and 'wrong boundary' "
    "pointing at specific code lines, and time stamp '15 minutes'. A vertical "
    "spine between the columns reads 'VALIDATION'. Caption beneath: 'seniors "
    "trust less because they have validated more.'"
)


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    rng = random.Random(SKETCH_SEED)
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" role="img"
     aria-label="{ARIA_LABEL}">
  <rect width="{W}" height="{H}" fill="{BG}"/>
  {ARROW_MARKER}
  {diagram_layer(rng)}
</svg>
"""
    OUT_PATH.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT_PATH}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
