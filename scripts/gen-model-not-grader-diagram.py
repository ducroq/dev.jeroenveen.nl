"""Generate the article diagram for /writing/the-model-is-not-the-grader/.

Register: engineer's notebook sketch, vectorised onto the site's dark canvas.
Single-panel left-to-right flowchart of the calibration gate:
'new prompt' to reference set to grader to baseline/new scores to gate.
Gate has two outputs: 'ship' (down) and a loop arrow back to 'new prompt'
labelled 'block. rubric edit? argue it explicitly.'

Structural reference: memory/visual-references/model-not-grader-gemini-draft.png
(Gemini Imagen draft). The reference is on white graph paper; this version
keeps the sketch register but switches to the site's dark canvas to match
existing diagrams in the project.

Voice constraint: no em-dashes anywhere, including the SVG-embedded text.

Pattern follows scripts/gen-senior-trust-diagram.py: parameters at the top,
edit + rerun.
Output: public/diagrams/the-model-is-not-the-grader.svg
"""

from __future__ import annotations

import random
from pathlib import Path

# Output

OUT_PATH = (
    Path(__file__).parent.parent
    / "public" / "diagrams" / "the-model-is-not-the-grader.svg"
)

# Canvas

W, H = 1200, 520

BG = "#0b0b0f"           # site --bg
STROKE = "#8a8895"       # muted neutral (pencil-on-dark)
STROKE_AMBER = "#c88a20" # --amber-dim, accent for the loop-back path
TEXT = "#b8b5b0"         # warm off-white, like pencil
TEXT_DIM = "#7a7a85"

# Sketch params

JITTER = 2.5
SEGMENTS_PER_SIDE = 3
STROKE_WIDTH = 1.5
SKETCH_SEED = 11

# Layout

# new prompt (rounded rect)
PROMPT_X = 80
PROMPT_Y = 270
PROMPT_W = 140
PROMPT_H = 70

# reference set stack
STACK_X = 290
STACK_Y = 260
STACK_W = 90
STACK_H = 60
STACK_LAYERS = 4
STACK_OFFSET = 4

# grader box
GRADER_X = 470
GRADER_Y = 285
GRADER_W = 70
GRADER_H = 60

# score columns
SCORES_X = 590        # left column of numbers
SCORES_GAP = 70       # between two columns
SCORES_TOP = 265
SCORES_ROW = 25
SCORES_VALUES = [
    ("3.4", "3.5"),
    ("3.6", "3.4"),
    ("3.3", "3.2"),
    ("3.5", "3.3"),
]

# curly bracket
BRACKET_X = 730
BRACKET_TOP = 280
BRACKET_BOTTOM = 370

# gate (trapezoid; funnel shape, wider on left, narrower on right)
GATE_X1 = 920
GATE_X2 = 995
GATE_TOP_LEFT_Y = 265
GATE_BOTTOM_LEFT_Y = 380
GATE_TOP_RIGHT_Y = 290
GATE_BOTTOM_RIGHT_Y = 355

# block annotation (top-right)
BLOCK_LABEL_X = 1030
BLOCK_LABEL_Y = 50

# ship label
SHIP_X = 1080
SHIP_Y = 445

# caption
CAPTION_Y = 490


# Path helpers (same primitives as gen-senior-trust-diagram.py)

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


def rough_rounded_rect(
    x: float, y: float, w: float, h: float, r: float, rng: random.Random
) -> str:
    """Wobbly rounded rectangle. Q-curves for corners, jittered edges."""
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER * 0.6, JITTER * 0.6)
    parts = [f"M {jit(x + r):.1f},{jit(y):.1f}"]
    parts.append(f"L {jit(x + w - r):.1f},{jit(y):.1f}")
    parts.append(f"Q {x + w:.1f},{y:.1f} {jit(x + w):.1f},{jit(y + r):.1f}")
    parts.append(f"L {jit(x + w):.1f},{jit(y + h - r):.1f}")
    parts.append(f"Q {x + w:.1f},{y + h:.1f} {jit(x + w - r):.1f},{jit(y + h):.1f}")
    parts.append(f"L {jit(x + r):.1f},{jit(y + h):.1f}")
    parts.append(f"Q {x:.1f},{y + h:.1f} {jit(x):.1f},{jit(y + h - r):.1f}")
    parts.append(f"L {jit(x):.1f},{jit(y + r):.1f}")
    parts.append(f"Q {x:.1f},{y:.1f} {jit(x + r):.1f},{jit(y):.1f}")
    parts.append("Z")
    return " ".join(parts)


def rough_line(
    x1: float, y1: float, x2: float, y2: float,
    rng: random.Random, segments: int = 4, amp: float = 0.6,
) -> str:
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


def rough_polyline(
    points: list[tuple[float, float]], rng: random.Random, amp: float = 0.5,
) -> str:
    """Wobbly polyline through a list of points (first and last unjittered)."""
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER * amp, JITTER * amp)
    parts = [f"M {points[0][0]:.1f},{points[0][1]:.1f}"]
    for p in points[1:-1]:
        parts.append(f"L {jit(p[0]):.1f},{jit(p[1]):.1f}")
    parts.append(f"L {points[-1][0]:.1f},{points[-1][1]:.1f}")
    return " ".join(parts)


# Arrow markers

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


def arrow_path(d: str, amber: bool = False) -> str:
    stroke = STROKE_AMBER if amber else STROKE
    marker = "arr-amber" if amber else "arr"
    return (
        f'<path d="{d}" fill="none" stroke="{stroke}" '
        f'stroke-width="{STROKE_WIDTH}" stroke-linecap="round" '
        f'stroke-linejoin="round" marker-end="url(#{marker})"/>'
    )


def plain_path(d: str, stroke: str = STROKE, width: float = STROKE_WIDTH) -> str:
    return (
        f'<path d="{d}" fill="none" stroke="{stroke}" '
        f'stroke-width="{width}" stroke-linecap="round" '
        f'stroke-linejoin="round"/>'
    )


# Composition helpers

def stack_of_papers(
    x: float, y: float, w: float, h: float,
    layers: int, offset: float, rng: random.Random,
) -> str:
    """Layered rectangles, back-to-front, with a few text-lines on the top sheet."""
    parts: list[str] = []
    for i in range(layers):
        rx = x + (layers - 1 - i) * offset
        ry = y + (layers - 1 - i) * offset
        stroke = STROKE if i == layers - 1 else TEXT_DIM
        parts.append(plain_path(rough_rect(rx, ry, w, h, rng), stroke=stroke))
    # Three short horizontal text-lines on the topmost (last-drawn) sheet
    top_x = x
    top_y = y
    line_top_y = top_y + h * 0.30
    line_spacing = h * 0.20
    line_pad_x = 12
    widths = [0.65, 0.45, 0.55]
    for i in range(3):
        lx1 = top_x + line_pad_x
        lx2 = top_x + line_pad_x + (w - 2 * line_pad_x) * widths[i]
        ly = line_top_y + i * line_spacing
        parts.append(plain_path(
            rough_line(lx1, ly, lx2, ly, rng, segments=3, amp=0.4),
        ))
    return "".join(parts)


def grader_box(x: float, y: float, w: float, h: float, rng: random.Random) -> str:
    parts = [plain_path(rough_rect(x, y, w, h, rng))]
    cx, cy = x + w / 2, y + h / 2 + 9
    parts.append(
        f'<text x="{cx}" y="{cy}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="28" fill="{TEXT}">{{ }}</text>'
    )
    return "".join(parts)


def curly_bracket(x: float, y_top: float, y_bottom: float, point_dx: float = 12) -> str:
    """Right-facing curly bracket. Point sticks out to the right by point_dx."""
    mid = (y_top + y_bottom) / 2
    d = (
        f"M {x:.1f},{y_top:.1f} "
        f"C {x + point_dx * 0.6:.1f},{y_top + (mid - y_top) * 0.3:.1f} "
        f"{x + point_dx:.1f},{y_top + (mid - y_top) * 0.5:.1f} "
        f"{x + point_dx:.1f},{mid:.1f} "
        f"M {x + point_dx:.1f},{mid:.1f} "
        f"C {x + point_dx:.1f},{mid + (y_bottom - mid) * 0.5:.1f} "
        f"{x + point_dx * 0.6:.1f},{y_bottom - (y_bottom - mid) * 0.3:.1f} "
        f"{x:.1f},{y_bottom:.1f}"
    )
    return plain_path(d)


def gate_trapezoid(rng: random.Random) -> str:
    """Right-side gate: funnel-shape trapezoid, wider on left."""
    def jit(v: float) -> float:
        return v + rng.uniform(-JITTER, JITTER)
    d = (
        f"M {jit(GATE_X1):.1f},{jit(GATE_TOP_LEFT_Y):.1f} "
        f"L {jit(GATE_X2):.1f},{jit(GATE_TOP_RIGHT_Y):.1f} "
        f"L {jit(GATE_X2):.1f},{jit(GATE_BOTTOM_RIGHT_Y):.1f} "
        f"L {jit(GATE_X1):.1f},{jit(GATE_BOTTOM_LEFT_Y):.1f} Z"
    )
    return plain_path(d)


# Compose

def diagram_layer(rng: random.Random) -> str:
    parts: list[str] = []

    # 'new prompt' rounded rectangle (left)
    parts.append(plain_path(rough_rounded_rect(
        PROMPT_X, PROMPT_Y, PROMPT_W, PROMPT_H, 14, rng
    )))
    parts.append(
        f'<text x="{PROMPT_X + PROMPT_W / 2}" y="{PROMPT_Y + 32}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="18" fill="{TEXT}">new</text>'
    )
    parts.append(
        f'<text x="{PROMPT_X + PROMPT_W / 2}" y="{PROMPT_Y + 54}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="18" fill="{TEXT}">prompt</text>'
    )

    # Arrow: new prompt to reference set
    parts.append(arrow_path(rough_line(
        PROMPT_X + PROMPT_W + 4, PROMPT_Y + PROMPT_H / 2,
        STACK_X - 6, STACK_Y + STACK_H / 2,
        rng, segments=4, amp=0.4,
    )))

    # reference set stack
    parts.append(stack_of_papers(
        STACK_X, STACK_Y, STACK_W, STACK_H, STACK_LAYERS, STACK_OFFSET, rng,
    ))
    stack_label_cx = STACK_X + STACK_W / 2 + (STACK_LAYERS - 1) * STACK_OFFSET / 2
    parts.append(
        f'<text x="{stack_label_cx}" y="{STACK_Y + STACK_H + 32}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="16" fill="{TEXT}">reference set</text>'
    )

    # Arrow: reference set to grader
    stack_right_x = STACK_X + STACK_W + (STACK_LAYERS - 1) * STACK_OFFSET
    parts.append(arrow_path(rough_line(
        stack_right_x + 4, STACK_Y + STACK_H / 2,
        GRADER_X - 6, GRADER_Y + GRADER_H / 2,
        rng, segments=4, amp=0.4,
    )))

    # grader box
    parts.append(grader_box(GRADER_X, GRADER_Y, GRADER_W, GRADER_H, rng))
    parts.append(
        f'<text x="{GRADER_X + GRADER_W / 2}" y="{GRADER_Y + GRADER_H + 28}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="16" fill="{TEXT}">grader</text>'
    )

    # Arrow: grader to scores
    parts.append(arrow_path(rough_line(
        GRADER_X + GRADER_W + 4, GRADER_Y + GRADER_H / 2,
        SCORES_X - 28, SCORES_TOP + SCORES_ROW * 1.7,
        rng, segments=4, amp=0.4,
    )))

    # Score columns
    col1_x = SCORES_X
    col2_x = SCORES_X + SCORES_GAP
    parts.append(
        f'<text x="{col1_x}" y="{SCORES_TOP}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="16" fill="{TEXT_DIM}">baseline</text>'
    )
    parts.append(
        f'<text x="{col2_x}" y="{SCORES_TOP}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="16" fill="{TEXT_DIM}">new</text>'
    )
    for i, (baseline_val, new_val) in enumerate(SCORES_VALUES):
        y = SCORES_TOP + SCORES_ROW * (i + 1) + 8
        parts.append(
            f'<text x="{col1_x}" y="{y}" text-anchor="middle" '
            f'font-family="JetBrains Mono, ui-monospace, monospace" '
            f'font-size="18" fill="{TEXT}">{baseline_val}</text>'
        )
        parts.append(
            f'<text x="{col2_x}" y="{y}" text-anchor="middle" '
            f'font-family="JetBrains Mono, ui-monospace, monospace" '
            f'font-size="18" fill="{TEXT}">{new_val}</text>'
        )

    # Curly bracket + 'within tolerance?'
    parts.append(curly_bracket(BRACKET_X, BRACKET_TOP, BRACKET_BOTTOM, point_dx=14))
    parts.append(
        f'<text x="{BRACKET_X + 24}" y="{(BRACKET_TOP + BRACKET_BOTTOM) / 2 + 5}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="15" font-style="italic" fill="{TEXT_DIM}">within tolerance?</text>'
    )

    # Gate trapezoid
    parts.append(gate_trapezoid(rng))

    # Ship arrow (down/right from gate)
    gate_right_mid_y = (GATE_TOP_RIGHT_Y + GATE_BOTTOM_RIGHT_Y) / 2
    parts.append(arrow_path(rough_polyline(
        [
            (GATE_X2 + 2, gate_right_mid_y),
            (GATE_X2 + 35, gate_right_mid_y + 35),
            (SHIP_X - 12, SHIP_Y - 28),
        ],
        rng, amp=0.4,
    )))
    parts.append(
        f'<text x="{SHIP_X}" y="{SHIP_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="18" fill="{TEXT}">ship</text>'
    )

    # Loop arrow back to 'new prompt' (amber)
    loop_start_x = GATE_X1 + (GATE_X2 - GATE_X1) * 0.4
    loop_points = [
        (loop_start_x, GATE_TOP_LEFT_Y - 2),
        (loop_start_x, 100),
        (PROMPT_X + PROMPT_W / 2, 100),
        (PROMPT_X + PROMPT_W / 2, PROMPT_Y - 4),
    ]
    parts.append(arrow_path(rough_polyline(loop_points, rng, amp=0.5), amber=True))

    # Block annotation (top-right, amber)
    block_lines = ["block.", "rubric edit?", "argue it", "explicitly"]
    for i, line in enumerate(block_lines):
        parts.append(
            f'<text x="{BLOCK_LABEL_X}" y="{BLOCK_LABEL_Y + i * 22}" '
            f'font-family="JetBrains Mono, ui-monospace, monospace" '
            f'font-size="17" fill="{STROKE_AMBER}">{line}</text>'
        )

    # Bottom caption
    parts.append(
        f'<text x="{W / 2}" y="{CAPTION_Y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-size="22" fill="{TEXT}">what a calibration gate actually does.</text>'
    )

    return "\n  ".join(parts)


# Main

ARIA_LABEL = (
    "Single-panel hand-drawn sketch reading left to right. On the left, a "
    "rounded box labelled 'new prompt'. An arrow goes to a stack of papers "
    "labelled 'reference set'. Another arrow goes to a small box with curly "
    "braces labelled 'grader'. Beyond that, two short columns of numbers "
    "headed 'baseline' and 'new', with a curly bracket and annotation "
    "'within tolerance?'. On the right, a trapezoid gate with two outputs: "
    "a short arrow down to 'ship', and a long arrow looping back across the "
    "top of the picture to the 'new prompt' box, labelled 'block. rubric "
    "edit? argue it explicitly.' Caption beneath: 'what a calibration gate "
    "actually does.'"
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
