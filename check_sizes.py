from PIL import Image
import os

img_dir = r"images"
for img_name in ["pasar_a_idle.png", "pasar_b_idle.png", "pasar_c_idle.png"]:
    try:
        img = Image.open(os.path.join(img_dir, img_name))
        print(f"{img_name}: {img.size}")
    except Exception as e:
        print(f"{img_name}: Error - {e}")
