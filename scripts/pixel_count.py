import os
import numpy as np
from osgeo import gdal
import csv

folder_path = r"."
tif_files = [f for f in os.listdir(folder_path) if f.endswith(".tif")]


output_csv = os.path.join(folder_path, "pixel_counts_all_years.csv")

# Landcover classes
classes = {
    0: "Unclassified",
    1: "Forest",
    2: "Natural grasslands",
    3: "Urban",
    4: "Pastures",
    5: "Secondary forest",
    6: "Water",
    7: "Highly reflective surfaces"
}

pixel_area_ha = 30 * 30 / 10000  # hectares

with open(output_csv, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Layer Name", "Class Value", "Class Name", "Pixel Count", "Percentage (%)", "Area (ha)"])

    for tif in tif_files:
        file_path = os.path.join(folder_path, tif)
        print(f"Processing {tif} ...")
        ds = gdal.Open(file_path)
        band = ds.GetRasterBand(1)
        data = band.ReadAsArray()

        # Mask NoData (15)
        data_masked = np.ma.masked_equal(data, 15)
        total_pixels = data_masked.count()

        for value, name in classes.items():
            count = np.sum(data_masked == value)
            percent = (count / total_pixels * 100) if total_pixels > 0 else 0
            area_ha = count * pixel_area_ha
            writer.writerow([tif, value, name, count, f"{percent:.2f}", f"{area_ha:.2f}"])

print(f"\n Done ✅, CSV saved at: {output_csv}")
