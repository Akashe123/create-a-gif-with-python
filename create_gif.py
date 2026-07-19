from PIL import Image
import os

# Folder containing images
image_folder = "images"

# Output GIF file
output_gif = "output.gif"

# Get image filenames
image_files = sorted([
    file for file in os.listdir(image_folder)
    if file.endswith((".png", ".jpg", ".jpeg"))
])

# Open images
images = []

for file in image_files:
    path = os.path.join(image_folder, file)
    img = Image.open(path)
    images.append(img)

# Check if images exist
if images:
    images[0].save(
        output_gif,
        save_all=True,
        append_images=images[1:],
        duration=300,   # 300 milliseconds per frame
        loop=0          # Infinite loop
    )

    print("GIF created successfully!")
else:
    print("No images found.")