import os
from PIL import Image

INPUT_FOLDER = "/path/to/tiff/folder"
OUTPUT_FOLDER = "/path/to/png/folder"

def ensure_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def convert_tiff_to_png(tif_path, png_path):
    img = Image.open(tif_path)
    img.save(png_path)

def main():
    ensure_folder(OUTPUT_FOLDER)

    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(".tif")]

    for filename in files:
        tif_path = os.path.join(INPUT_FOLDER, filename)
        png_name = os.path.splitext(filename)[0] + ".png"
        png_path = os.path.join(OUTPUT_FOLDER, png_name)

        print("Converting:", filename)
        convert_tiff_to_png(tif_path, png_path)

    print("PNGs saved to:", OUTPUT_FOLDER)

if __name__ == "__main__":
    main()
