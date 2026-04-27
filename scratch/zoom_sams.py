import cv2
import os

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
img_path = os.path.join(assets_dir, 'sams_pdf_thumb.jpg')

if os.path.exists(img_path):
    img = cv2.imread(img_path)
    if img is not None:
        h, w = img.shape[:2]
        # We want to zoom in. Let's crop 15% from left and right, and 20% from the bottom.
        # This effectively zooms in on the top-center part of the document.
        crop_left = int(w * 0.15)
        crop_right = int(w * 0.85)
        crop_top = int(h * 0.05) # crop a tiny bit of the top margin if there is white space
        crop_bottom = int(h * 0.75) # keep the top 70% of the vertical space
        
        cropped = img[crop_top:crop_bottom, crop_left:crop_right]
        cv2.imwrite(img_path, cropped)
        print(f"Successfully zoomed and saved {img_path}")
    else:
        print("Failed to load image.")
else:
    print(f"File not found: {img_path}")
