import cv2
import matplotlib.pyplot as plt
import sys

# Load the image
image_path = "test_images/face.jpg"  # Change if needed
img = cv2.imread(image_path)

if img is None:
    print(f"❌ Error: Image '{image_path}' not found.")
    sys.exit(1)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load Haar cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Convert BGR to RGB for matplotlib
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the result
plt.imshow(img_rgb)
plt.axis('off')
plt.title(f"Detected Faces: {len(faces)}")
plt.show()

