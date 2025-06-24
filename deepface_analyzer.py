from deepface import DeepFace
import sys

def analyze_image(image_path):
    try:
        print(f"Analyzing {image_path}...")
        result = DeepFace.analyze(img_path=image_path, actions=['age', 'gender', 'emotion'], enforce_detection=False)
        print("\n🎯 Analysis Result:")
        print(result[0])
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python deepface_analyzer.py <image_path>")
    else:
        analyze_image(sys.argv[1])

