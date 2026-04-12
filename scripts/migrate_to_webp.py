import os
import re
from PIL import Image

# Configuration
BASE_DIR = "/home/monday/ernestokitchenwebsite/ernesto-kitchen"
IMAGE_DIR = os.path.join(BASE_DIR, "foodimages")
HTML_FILE = os.path.join(BASE_DIR, "index.html")
ARCHIVE_DIR = os.path.join(IMAGE_DIR, "archiveeditedbutnamed")

def migrate_images():
    converted_count = 0
    for filename in os.listdir(IMAGE_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            source_path = os.path.join(IMAGE_DIR, filename)
            
            # Skip directories
            if os.path.isdir(source_path):
                continue
                
            base_name = os.path.splitext(filename)[0]
            target_name = f"{base_name}.webp"
            target_path = os.path.join(IMAGE_DIR, target_name)
            
            try:
                with Image.open(source_path) as img:
                    # Save as WebP with high quality
                    img.save(target_path, "WEBP", quality=90, optimize=True)
                    print(f"Converted: {filename} -> {target_name}")
                    converted_count += 1
            except Exception as e:
                print(f"Error converting {filename}: {e}")
    return converted_count

def update_html():
    if not os.path.exists(HTML_FILE):
        print(f"HTML file not found: {HTML_FILE}")
        return

    with open(HTML_FILE, 'r') as f:
        content = f.read()

    # Pattern to match foodimages paths with png/jpg extensions
    # Matches: ./foodimages/name.png or foodimages/name.jpg
    pattern = r'(\.?/foodimages/[^"\s\)]+)\.(png|jpg|jpeg)'
    
    # Replacement function to swap extension for .webp
    def replace_ext(match):
        path = match.group(1)
        return f"{path}.webp"

    new_content = re.sub(pattern, replace_ext, content)
    
    if new_content != content:
        with open(HTML_FILE, 'w') as f:
            f.write(new_content)
        print("Updated index.html image references to .webp")
    else:
        print("No image references updated in index.html (already .webp?)")

def main():
    print("Starting WebP migration...")
    count = migrate_images()
    print(f"Total images converted: {count}")
    update_html()
    print("Migration complete!")

if __name__ == "__main__":
    main()
