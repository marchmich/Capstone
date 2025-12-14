import os
import re
import csv
import numpy as np
import rasterio

# Folder containing your .tif files
INPUT_FOLDER = "/Path/to/Governance/dataset"
OUTPUT_CSV = "/path/to/governancestats.csv"

# Pixel → category mapping
CATEGORIES = {
    1: "deforested",
    2: "forest",
    3: "non_forest",
    0: "no_data"
}

# Area per pixel in km^2 (dataset resolution is 1 km x 1 km)
AREA_PER_PIXEL_KM2 = 1.0


def extract_year(filename):
    """
    Extracts a 4-digit year from the filename.
    Example: 'Governance_2003.tif' → 2003
    """
    match = re.search(r'(\d{4})', filename)
    return int(match.group(1)) if match else None


def process_tif(filepath):
    with rasterio.open(filepath) as src:
        data = src.read(1)

    results = {}
    total_pixels = data.size

    for code, label in CATEGORIES.items():
        results[label] = int(np.sum(data == code))

    results["total_pixels"] = total_pixels
    return results


def main():
    rows = []

    for filename in sorted(os.listdir(INPUT_FOLDER)):
        if filename.lower().endswith(".tif"):
            filepath = os.path.join(INPUT_FOLDER, filename)

            year = extract_year(filename)
            if year is None:
                print(f"Skipping {filename} (no year found)")
                continue

            counts = process_tif(filepath)

            total = counts["total_pixels"]

            row = {
                "year": year,
                "forest_pixels": counts["forest"],
                "deforested_pixels": counts["deforested"],
                "non_forest_pixels": counts["non_forest"],
                "no_data_pixels": counts["no_data"],

                "forest_pct": counts["forest"] / total * 100,
                "deforested_pct": counts["deforested"] / total * 100,
                "non_forest_pct": counts["non_forest"] / total * 100,
                "no_data_pct": counts["no_data"] / total * 100,

                "forest_area_km2": counts["forest"] * AREA_PER_PIXEL_KM2,
                "deforested_area_km2": counts["deforested"] * AREA_PER_PIXEL_KM2,
                "non_forest_area_km2": counts["non_forest"] * AREA_PER_PIXEL_KM2,
                "no_data_area_km2": counts["no_data"] * AREA_PER_PIXEL_KM2
            }

            rows.append(row)

    # Make a CSV file
    with open(OUTPUT_CSV, "w", newline="") as csvfile:
        fieldnames = rows[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"CSV created → {OUTPUT_CSV}")


if __name__ == "__main__":
    main()
