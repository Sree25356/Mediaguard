from PIL import Image, ImageChops, ImageEnhance
import matplotlib.pyplot as plt
import os
import sys

def perform_ela(image_path, quality=95):
    try:
        original = Image.open(image_path).convert('RGB')
        temp_path = "temp_ela.jpg"
        original.save(temp_path, 'JPEG', quality=quality)

        temp = Image.open(temp_path)
        ela_image = ImageChops.difference(original, temp)

        enhancer = ImageEnhance.Brightness(ela_image)
        ela_image = enhancer.enhance(30)  # Adjust scale for visibility

        plt.imshow(ela_image)
        plt.title("🧪 Error Level Analysis")
        plt.axis('off')
        plt.show()

        os.remove(temp_path)
    except Exception as e:
        print(f"❌ ELA error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ela_detector.py <image_path>")
    else:
        perform_ela(sys.argv[1])
