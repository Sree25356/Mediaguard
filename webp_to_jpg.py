from PIL import Image

input_path = "/home/Mr.sv/Downloads/1.webp"
output_path = "test_images/face.jpg"

img = Image.open(input_path)
img = img.convert("RGB")  # Ensure proper format
img.save(output_path, "JPEG")
print(f"✅ Converted and saved to {output_path}")
