import os
import re
from PIL import Image, ImageDraw, ImageFont

INPUT_FOLDER = "/eccs/home/mmarch22/capstone/archives/governancepng"
OUTPUT_FOLDER = "/eccs/home/mmarch22/capstone/archives/frames_gov"

TITLE_TEXT = "Governance Scenario"
FONT_PATH = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # adjust if needed

# QGIS Colors
COLOR_DEFORESTED = "#e7421b"
COLOR_FOREST = "#2b421b"
COLOR_NONFOREST = "#efca01"

def extract_year(filename):
    """Extract a 4-digit year from the filename."""
    match = re.search(r"(\d{4})", filename)
    if match:
        return int(match.group(1))
    return None


def draw_legend(draw, width, height):
    """Draw legend box at bottom-right corner."""
    padding = 20
    box_width = 260
    box_height = 120
    x0 = width - box_width - padding
    y0 = height - box_height - padding
    x1 = width - padding
    y1 = height - padding

    # Background box
    draw.rectangle([x0, y0, x1, y1], fill="white", outline="black", width=3)

    # Legend entries: (color, label)
    entries = [
        (COLOR_DEFORESTED, "Deforested Area"),
        (COLOR_FOREST, "Forest Area"),
        (COLOR_NONFOREST, "Non-Forest Area"),
    ]

    font = ImageFont.truetype(FONT_PATH, 22)
    box_y = y0 + 10

    for color, label in entries:
        # Color box
        draw.rectangle([x0 + 10, box_y, x0 + 40, box_y + 25], fill=color, outline="black")

        # Label (NO HEX CODE)
        draw.text((x0 + 50, box_y), label, fill="black", font=font)

        box_y += 35


def add_title_year_and_legend(input_path, output_path, year):
    """Open PNG → add title, year, legend → save to output."""
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size

    draw = ImageDraw.Draw(img)
    title_font = ImageFont.truetype(FONT_PATH, 40)
    year_font = ImageFont.truetype(FONT_PATH, 36)

    # Title
    draw.text(
        (width // 2, 30),
        TITLE_TEXT,
        fill="white",
        font=title_font,
        anchor="mm"
    )

    # Year (top-left)
    draw.text(
        (40, 30),
        str(year),
        fill="white",
        font=year_font,
        anchor="lm"
    )

    # Legend
    draw_legend(draw, width, height)

    img.save(output_path)
    print(f"Saved: {output_path}")

def main():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    files = sorted(os.listdir(INPUT_FOLDER))

    for file in files:
        if not file.endswith(".png"):
            continue

        year = extract_year(file)
        if year is None or not (2002 <= year <= 2050):
            continue  # skip files outside range

        input_path = os.path.join(INPUT_FOLDER, file)
        output_path = os.path.join(OUTPUT_FOLDER, file)

        add_title_year_and_legend(input_path, output_path, year)

    print("DONE.")


if __name__ == "__main__":
    main()
