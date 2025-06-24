import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
import matplotlib.pyplot as plt

# Load the image
image_path = "test_images/face.jpg"
img = cv2.imread(image_path)

# Detect faces and gender
faces, confidences = cv.detect_face(img)
genders, gender_conf = cv.detect_gender(img)

# Draw bounding boxes and labels
for idx, face in enumerate(faces):
    label = f"{genders[idx]} ({gender_conf[idx]*100:.2f}%)"
    (startX, startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    cv2.rectangle(img, (startX, startY), (endX, endY), (0, 255, 0), 2)
    cv2.putText(img, label, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Convert BGR to RGB for matplotlib display
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the result
plt.imshow(img_rgb)
plt.axis('off')
plt.title("Detected Faces & Gender")
plt.show()

