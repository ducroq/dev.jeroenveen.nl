"""Generate the typographic social/cover image for an article.

Produces a 1200x630 PNG (OG / LinkedIn cover safe) on the site's dark
background with the amber accent. Run from repo root:

    python scripts/gen-social-image.py
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

# ── Site design tokens (from src/styles/global.css) ─────────────────────────
BG = (11, 11, 15)         # --bg        #0b0b0f
TEXT = (232, 232, 237)    # --text      #e8e8ed
TEXT_DIM = (133, 133, 160)# --text-dim  #8585a0
AMBER = (240, 168, 48)    # --amber     #f0a830
BORDER = (42, 42, 53)     # --border    #2a2a35

# ── Canvas ──────────────────────────────────────────────────────────────────
W, H = 1200, 630
PAD_L, PAD_R = 90, 90
PAD_T, PAD_B = 70, 70

# ── Font loading (Consolas; clean mono available on Windows) ────────────────
FONT_REG = r"C:\Windows\Fonts\consola.ttf"
FONT_BLD = r"C:\Windows\Fonts\consolab.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(FONT_BLD if bold else FONT_REG, size)


def render(out_path: Path) -> None:
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    # Left amber accent bar (echoes the project-card top borders)
    draw.rectangle([(0, 0), (10, H)], fill=AMBER)

    # Top label, mirrors .article-label (amber, mono, uppercase, letter-spaced)
    label_font = font(20, bold=True)
    draw.text((PAD_L, PAD_T), "W R I T I N G", font=label_font, fill=AMBER)

    # Headline: the strongest line, broken across three lines for poster rhythm
    head_size = 78
    head_font = font(head_size, bold=True)
    line_h = int(head_size * 1.18)
    headline = [
        "Production is now",
        "cheap and fast.",
        "Validation is not.",
    ]
    head_y = PAD_T + 70
    for i, line in enumerate(headline):
        # The third line gets the amber for emphasis ("Validation is not.")
        fill = AMBER if i == 2 else TEXT
        draw.text((PAD_L, head_y + i * line_h), line, font=head_font, fill=fill)

    # Bottom-left: domain (small, dim, mono)
    domain_font = font(22, bold=False)
    draw.text((PAD_L, H - PAD_B - 24), "dev.jeroenveen.nl", font=domain_font, fill=TEXT_DIM)

    # Bottom-right: article slug breadcrumb
    slug_font = font(18, bold=False)
    slug = "/writing/the-work-is-splitting"
    bbox = draw.textbbox((0, 0), slug, font=slug_font)
    slug_w = bbox[2] - bbox[0]
    draw.text((W - PAD_R - slug_w, H - PAD_B - 22), slug, font=slug_font, fill=TEXT_DIM)

    # Subtle bottom hairline above the footer band
    draw.line([(PAD_L, H - PAD_B - 44), (W - PAD_R, H - PAD_B - 44)], fill=BORDER, width=1)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, "PNG", optimize=True)
    print(f"wrote {out_path} ({out_path.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    render(Path("public/social/the-work-is-splitting.png"))
