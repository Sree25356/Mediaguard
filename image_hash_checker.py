from PIL import Image
import imagehash
import sys

def get_hash(image_path):
    try:
        image = Image.open(image_path)
        hash_val = imagehash.average_hash(image)
        print(f"🧠 Hash for {image_path}: {hash_val}")
        return hash_val
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python image_hash_checker.py <image1> <image2>")
    else:
        hash1 = get_hash(sys.argv[1])
        hash2 = get_hash(sys.argv[2])
        if hash1 and hash2:
            diff = hash1 - hash2
            print(f"🧪 Hash Difference: {diff}")
            if diff < 5:
                print("✅ Images are likely similar.")
            else:
                print("❗ Images are likely different or edited.")

