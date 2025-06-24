import cv2
import hashlib
from PIL import Image, ExifTags, ImageChops, ImageEnhance
import os
import sys
from datetime import datetime
import matplotlib.pyplot as plt

report_lines = []

def log(msg):
    print(msg)
    report_lines.append(msg)

def check_hash(image_path):
    try:
        with open(image_path, 'rb') as f:
            sha256 = hashlib.sha256(f.read()).hexdigest()
            log(f"🔐 SHA256: {sha256}")
    except Exception as e:
        log(f"❌ Hash error: {e}")

def check_metadata(image_path):
    try:
        img = Image.open(image_path)
        exif = img._getexif()
        if not exif:
            log("ℹ️ No EXIF metadata found.")
            return
        log("📸 EXIF Metadata:")
        for tag_id, value in exif.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            log(f"   {tag:25}: {value}")
    except Exception as e:
        log(f"❌ Metadata error: {e}")

def detect_faces(image_path):
    try:
        img = cv2.imread(image_path)
        if img is None:
            log(f"❌ OpenCV can't open image: {image_path}")
            return
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        log(f"🧠 Detected {len(faces)} face(s).")
        cv2.imshow("Face Detection", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        log(f"❌ Face detection error: {e}")

def error_level_analysis(image_path, quality=95):
    try:
        log("🔍 Running Error Level Analysis (ELA)...")
        original = Image.open(image_path).convert('RGB')
        temp_path = "temp_ela.jpg"
        original.save(temp_path, 'JPEG', quality=quality)

        temp = Image.open(temp_path)
        ela_image = ImageChops.difference(original, temp)

        enhancer = ImageEnhance.Brightness(ela_image)
        ela_image = enhancer.enhance(30)

        plt.imshow(ela_image)
        plt.title("🧪 Error Level Analysis (ELA)")
        plt.axis('off')
        plt.show()

        os.remove(temp_path)
        log("✅ ELA completed and displayed.")
    except Exception as e:
        log(f"❌ ELA error: {e}")

def detect_ai_generation(image_path):
    try:
        log("🤖 Checking for AI-generation clues...")
        img = Image.open(image_path)
        width, height = img.size

        suspicious = False
        if width == height and width in [512, 1024, 768]:
            log(f"⚠️ Resolution is {width}x{height} — common in AI images.")
            suspicious = True

        exif = img._getexif()
        if not exif:
            log("⚠️ No EXIF metadata — typical of AI-generated content.")
            suspicious = True
        else:
            for tag_id, value in exif.items():
                tag = ExifTags.TAGS.get(tag_id, tag_id)
                if isinstance(value, str) and any(x in value.lower() for x in ["diffusion", "midjourney", "dalle", "ai", "stability"]):
                    log(f"⚠️ AI clue in metadata: {tag}: {value}")
                    suspicious = True

        if not suspicious:
            log("✅ No strong AI-generation signs found.")
        else:
            log("🧠 ⚠️ Possible AI-generated image detected.")

    except Exception as e:
        log(f"❌ AI detection error: {e}")

def save_report(image_path):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = os.path.basename(image_path)
    with open("MediaGuard_Report.txt", "a") as report:
        report.write(f"\n=== MediaGuard Report ===\n")
        report.write(f"🕒 Timestamp: {timestamp}\n")
        report.write(f"🖼️ Image: {filename}\n")
        report.write("-------------------------\n")
        for line in report_lines:
            report.write(line + "\n")
        report.write("\n=========================\n\n")
    print(f"\n📄 Report saved to MediaGuard_Report.txt")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mediaguard.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.exists(image_path):
        print("❌ File not found:", image_path)
        sys.exit(1)

    print(f"\n🛡️ MediaGuard Analysis for: {image_path}\n")
    log(f"Analyzing: {image_path}")
    check_hash(image_path)
    log("\n------------------------")
    check_metadata(image_path)
    log("\n------------------------")
    detect_faces(image_path)
    log("\n------------------------")
    error_level_analysis(image_path)
    log("\n------------------------")
    detect_ai_generation(image_path)
    save_report(image_path)

