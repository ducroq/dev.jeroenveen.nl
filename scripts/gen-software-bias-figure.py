"""Generate the typographic figure for /writing/ai-productivity-software-bias/.

Register: Tufte-style typographic citation. Same pattern as
gen-senior-trust-figure.py. The HAZOP textual-vs-semantic asymmetry is
the article's anchor number-pair; this figure presents it without a
domain-coverage sketch (which would be the asymmetry-as-argument move
the *It Is Both* memory rule warns against).

Output: public/diagrams/ai-productivity-software-bias.svg
"""

from __future__ import annotations

from pathlib import Path

OUT_PATH = Path(__file__).parent.parent / "public" / "diagrams" / "ai-productivity-software-bias.svg"

# ─── Canvas ─────────────────────────────────────────────────────────────────

W, H = 1000, 320

BG = "#0b0b0f"
TEXT = "#e8e8ed"
TEXT_MUTED = "#9898a8"
TEXT_DIM = "#7a7a85"
RULE = "#3a3a48"

# ─── Content ────────────────────────────────────────────────────────────────

CITATION = "ai-assisted hazop  ·  park et al. 2025"
LEFT_NUMBER, LEFT_LABEL = "86%", "textual plausibility"
RIGHT_NUMBER, RIGHT_LABEL = "19–37%", "semantic validity"   # en-dash

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
     aria-label="Park et al. 2025: AI-assisted HAZOP output scored 86% on textual plausibility but 19 to 37% on semantic validity.">
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
