import os
from PIL import Image

image_dir = '/home/monday/ernestokitchenwebsite/ernesto-kitchen/foodimages'
files = os.listdir(image_dir)

for filename in files:
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        filepath = os.path.join(image_dir, filename)
        try:
            with Image.open(filepath) as img:
                name, _ = os.path.splitext(filename)
                webp_path = os.path.join(image_dir, f"{name}.webp")
                img.save(webp_path, "WEBP", quality=85)
                print(f"Converted {filename} to {name}.webp")
        except Exception as e:
            print(f"Failed to convert {filename}: {e}")
