"""Generate the LinkedIn / OG cover image for the model-is-not-the-grader article.

This article uses the **diagram-as-cover** variant rather than the typographic
title card produced by `gen-social-image.py`. The published article has a
strong central sketch (the calibration-gate diagram), and using that sketch
as the cover is more honest than a title card: the cover IS the object the
article describes.

The canonical SVG at `public/diagrams/the-model-is-not-the-grader.svg` is
already calibrated for thumbnail legibility (3 px strokes, near-white text,
bold weight) so it renders cleanly when LinkedIn rescales the cover into the
feed-card thumbnail panel. This script just renders it to PNG via headless
Edge (no Cairo dependency on Windows) and composes onto a 1200x630 dark
canvas with the diagram centered vertically. Top/bottom padding uses the
same `#0b0b0f` the SVG declares, so the seam is invisible.

Run from repo root:

    python scripts/gen-model-not-grader-cover.py
"""
import subprocess
from pathlib import Path

from PIL import Image

EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

CANONICAL_SVG = Path("public/diagrams/the-model-is-not-the-grader.svg")
OUT_PNG = Path("public/social/the-model-is-not-the-grader.png")
COVER_W, COVER_H = 1200, 630
BG = (11, 11, 15)  # #0b0b0f, matches the SVG's own background rect


def main() -> None:
    tmp_png = Path("drafts/_tmp_cover.png")
    subprocess.run(
        [
            EDGE,
            "--headless",
            "--disable-gpu",
            f"--screenshot={tmp_png.resolve()}",
            "--window-size=1200,520",
            "--default-background-color=0b0b0fff",
            f"file:///{CANONICAL_SVG.resolve().as_posix()}",
        ],
        check=True,
        capture_output=True,
    )

    diagram = Image.open(tmp_png)
    canvas = Image.new("RGB", (COVER_W, COVER_H), BG)
    canvas.paste(diagram, (0, (COVER_H - diagram.size[1]) // 2))
    OUT_PNG.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(OUT_PNG, "PNG", optimize=True)
    tmp_png.unlink()

    print(f"wrote {OUT_PNG} ({OUT_PNG.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
