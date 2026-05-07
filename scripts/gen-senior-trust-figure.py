"""Generate the typographic figure for /writing/senior-developers-trust-ai-less/.

Register: Tufte-style typographic citation, not a sketch. Two numbers with
labels, a thin separator, one citation line. No boxes, no arrows, no
atmosphere. The figure highlights the data the article cites; it does not
argue with shape. The asymmetry-as-the-whole-argument move (which the
*It Is Both* memory rule warns against) is deliberately not used here.

Output: public/diagrams/senior-developers-trust-ai-less.svg
"""

from __future__ import annotations

from pathlib import Path

OUT_PATH = Path(__file__).parent.parent / "public" / "diagrams" / "senior-developers-trust-ai-less.svg"

# ─── Canvas ─────────────────────────────────────────────────────────────────

W, H = 1000, 320

BG = "#0b0b0f"
TEXT = "#e8e8ed"
TEXT_MUTED = "#9898a8"
TEXT_DIM = "#7a7a85"
RULE = "#3a3a48"

# ─── Content ────────────────────────────────────────────────────────────────

CITATION = "low trust in ai output  ·  jetbrains 2025"
LEFT_NUMBER, LEFT_LABEL = "61%", "10+ years"
RIGHT_NUMBER, RIGHT_LABEL = "48%", "0–2 years"   # en-dash, not em-dash

# ─── Layout ─────────────────────────────────────────────────────────────────

CITATION_Y = 70
NUMBERS_Y = 195
LABELS_Y = 245
RULE_Y = 285
LEFT_X, RIGHT_X = 320, 680


def main() -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}"
     width="{W}" height="{H}" role="img"
     aria-label="JetBrains 2025: software developers with 10+ years of experience report low trust in AI output 61% of the time. Developers with 0 to 2 years report low trust 48% of the time.">
  <rect width="{W}" height="{H}" fill="{BG}"/>

  <text x="{W/2}" y="{CITATION_Y}" text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="16" fill="{TEXT_DIM}" letter-spacing="2">{CITATION}</text>

  <text x="{LEFT_X}" y="{NUMBERS_Y}" text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="76" font-weight="500" fill="{TEXT}">{LEFT_NUMBER}</text>
  <text x="{LEFT_X}" y="{LABELS_Y}" text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="20" fill="{TEXT_MUTED}">{LEFT_LABEL}</text>

  <text x="{RIGHT_X}" y="{NUMBERS_Y}" text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="76" font-weight="500" fill="{TEXT}">{RIGHT_NUMBER}</text>
  <text x="{RIGHT_X}" y="{LABELS_Y}" text-anchor="middle"
        font-family="JetBrains Mono, ui-monospace, monospace"
        font-size="20" fill="{TEXT_MUTED}">{RIGHT_LABEL}</text>

  <line x1="{W*0.18}" y1="{RULE_Y}" x2="{W*0.82}" y2="{RULE_Y}"
        stroke="{RULE}" stroke-width="1" stroke-linecap="round"/>
</svg>
"""
    OUT_PATH.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT_PATH}  ({len(svg):,} bytes)")


if __name__ == "__main__":
    main()
