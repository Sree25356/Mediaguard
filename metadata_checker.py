from PIL import Image
from PIL.ExifTags import TAGS
import sys

def get_metadata(image_path):
    try:
        image = Image.open(image_path)
        exifdata = image.getexif()
        if not exifdata:
            print("❌ No EXIF metadata found.")
            return

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            print(f"{tag:25}: {data}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python metadata_checker.py <image_path>")
    else:
        get_metadata(sys.argv[1])
