"""Generate the inside/outside boundary sketch for /writing/verification-is-a-workflow-problem/.

Register: engineer's notebook sketch on the site's dark canvas (matches
gen-model-not-grader-diagram.py and gen-ese-bot-diagram.py).

Job: show why the verifier has to be outside. A solid jittered boundary
encloses the drafting session. The drafter produces a verdict; two errors
stay trapped inside the boundary. Two fresh-session reviewers, outside the
boundary, reach across with amber arrows to surface the errors.

Structural reference: a Gemini Imagen draft used the inside/outside geometry
on cream paper. The output here keeps the geometry but switches to the
site's existing dark-canvas register.

Voice constraint: no em-dashes anywhere, including SVG-embedded text.

Pattern follows scripts/gen-model-not-grader-diagram.py: parameters at the
top, edit + rerun.

Output: public/diagrams/verification-is-a-workflow-problem.svg
"""

from __future__ import annotations

import random
from pathlib import Path

# Output

OUT_PATH = (
    Path(__file__).parent.parent
    / "public" / "diagrams" / "verification-is-a-workflow-problem.svg"
)

# Canvas

W, H = 1200, 520

BG = "#0b0b0f"
STROKE = "#d0d0d6"
STROKE_AMBER = "#c88a20"
TEXT = "#e8e8ed"
TEXT_DIM = "#c8c8d0"

# Sketch params

JITTER = 2.5
SEGMENTS_PER_SIDE = 3
STROKE_WIDTH = 3
SKETCH_SEED = 7
FONT_WEIGHT = "bold"

# Layout

# Drafting session boundary (big enclosing rectangle)
BOUNDARY_X = 70
BOUNDARY_Y = 60
BOUNDARY_W = 1060
BOUNDARY_H = 320

# "drafting session" label (inside top-left of boundary)
SESSION_LABEL_X = BOUNDARY_X + 24
SESSION_LABEL_Y = BOUNDARY_Y + 30

# Drafter (inside, upper-left)
DRAFTER_X = 130
DRAFTER_Y = 130
DRAFTER_W = 160
DRAFTER_H = 70

# Verdict (inside, upper-center)
VERDICT_X = 400
VERDICT_Y = 140
VERDICT_W = 140
VERDICT_H = 60

# Error 1: 5.48 GB (inside, lower-left)
ERR1_X = 380
ERR1_Y = 260
ERR1_W = 190
ERR1_H = 80

# Error 2: category swap (inside, lower-right)
ERR2_X = 620
ERR2_Y = 260
ERR2_W = 240
ERR2_H = 80

# Reviewer 1 (outside, bottom-left)
REV1_X = 250
REV1_Y = 420
REV1_W = 180
REV1_H = 60

# Reviewer 2 (outside, bottom-right)
REV2_X = 740
REV2_Y = 420
REV2_W = 220
REV2_H = 60


# Path helpers (same primitives as gen-model-not-grader-diagram.py)

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


def text_centered(
    x: float, y: float, content: str, size: int = 20,
    color: str = TEXT, italic: bool = False,
) -> str:
    style_attr = ' font-style="italic"' if italic else ''
    return (
        f'<text x="{x}" y="{y}" text-anchor="middle" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-weight="{FONT_WEIGHT}"{style_attr} '
        f'font-size="{size}" fill="{color}">{content}</text>'
    )


def text_left(
    x: float, y: float, content: str, size: int = 20,
    color: str = TEXT, italic: bool = False,
) -> str:
    style_attr = ' font-style="italic"' if italic else ''
    return (
        f'<text x="{x}" y="{y}" '
        f'font-family="JetBrains Mono, ui-monospace, monospace" '
        f'font-weight="{FONT_WEIGHT}"{style_attr} '
        f'font-size="{size}" fill="{color}">{content}</text>'
    )


# Compose

def diagram_layer(rng: random.Random) -> str:
    parts: list[str] = []

    # Boundary (the drafting session container)
    parts.append(plain_path(
        rough_rect(BOUNDARY_X, BOUNDARY_Y, BOUNDARY_W, BOUNDARY_H, rng),
    ))
    parts.append(text_left(
        SESSION_LABEL_X, SESSION_LABEL_Y, "drafting session",
        size=18, color=TEXT_DIM, italic=True,
    ))

    # Drafter (inside)
    parts.append(plain_path(rough_rect(
        DRAFTER_X, DRAFTER_Y, DRAFTER_W, DRAFTER_H, rng,
    )))
    parts.append(text_centered(
        DRAFTER_X + DRAFTER_W / 2,
        DRAFTER_Y + DRAFTER_H / 2 + 8,
        "drafter", size=22,
    ))

    # Drafter to verdict arrow
    parts.append(arrow_path(rough_line(
        DRAFTER_X + DRAFTER_W + 4,
        DRAFTER_Y + DRAFTER_H / 2,
        VERDICT_X - 6,
        VERDICT_Y + VERDICT_H / 2,
        rng, segments=4, amp=0.4,
    )))

    # Verdict (inside)
    parts.append(plain_path(rough_rect(
        VERDICT_X, VERDICT_Y, VERDICT_W, VERDICT_H, rng,
    )))
    parts.append(text_centered(
        VERDICT_X + VERDICT_W / 2,
        VERDICT_Y + VERDICT_H / 2 + 8,
        "verdict", size=22,
    ))

    # Error 1: 5.48 GB (jittered rounded rect, inside)
    parts.append(plain_path(rough_rounded_rect(
        ERR1_X, ERR1_Y, ERR1_W, ERR1_H, 28, rng,
    )))
    parts.append(text_centered(
        ERR1_X + ERR1_W / 2,
        ERR1_Y + ERR1_H / 2 + 8,
        "5.48 GB", size=22,
    ))

    # Error 2: category swap (jittered rounded rect, inside)
    parts.append(plain_path(rough_rounded_rect(
        ERR2_X, ERR2_Y, ERR2_W, ERR2_H, 28, rng,
    )))
    parts.append(text_centered(
        ERR2_X + ERR2_W / 2,
        ERR2_Y + ERR2_H / 2 + 8,
        "category swap", size=22,
    ))

    # Reviewer 1 (outside, bottom-left)
    parts.append(plain_path(rough_rect(
        REV1_X, REV1_Y, REV1_W, REV1_H, rng,
    )))
    parts.append(text_centered(
        REV1_X + REV1_W / 2,
        REV1_Y + REV1_H / 2 + 8,
        "reviewer 1", size=20,
    ))
    parts.append(text_centered(
        REV1_X + REV1_W / 2,
        REV1_Y + REV1_H + 22,
        "fresh session", size=14, color=TEXT_DIM, italic=True,
    ))

    # Reviewer 2 (outside, bottom-right)
    parts.append(plain_path(rough_rect(
        REV2_X, REV2_Y, REV2_W, REV2_H, rng,
    )))
    parts.append(text_centered(
        REV2_X + REV2_W / 2,
        REV2_Y + REV2_H / 2 + 8,
        "reviewer 2", size=20,
    ))
    parts.append(text_centered(
        REV2_X + REV2_W / 2,
        REV2_Y + REV2_H + 22,
        "fresh session", size=14, color=TEXT_DIM, italic=True,
    ))

    # Reviewer 1 to Error 1 (amber, piercing the boundary)
    parts.append(arrow_path(rough_line(
        REV1_X + REV1_W / 2,
        REV1_Y - 4,
        ERR1_X + ERR1_W / 2,
        ERR1_Y + ERR1_H + 4,
        rng, segments=6, amp=0.5,
    ), amber=True))

    # Reviewer 2 to Error 2 (amber, piercing the boundary)
    parts.append(arrow_path(rough_line(
        REV2_X + REV2_W / 2,
        REV2_Y - 4,
        ERR2_X + ERR2_W / 2,
        ERR2_Y + ERR2_H + 4,
        rng, segments=6, amp=0.5,
    ), amber=True))

    return "\n  ".join(parts)


# Main

ARIA_LABEL = (
    "Single-panel hand-drawn sketch on dark canvas. A large rectangular "
    "boundary labelled 'drafting session' encloses four elements: a box "
    "labelled 'drafter' with an arrow leading to a box labelled 'verdict', "
    "and below them, two rounded shapes labelled '5.48 GB' and 'category "
    "swap'. Below the boundary stand two further boxes labelled 'reviewer "
    "1' and 'reviewer 2', each captioned 'fresh session'. Two amber arrows "
    "rise from the reviewer boxes, cross the boundary line, and reach the "
    "two error shapes inside."
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
