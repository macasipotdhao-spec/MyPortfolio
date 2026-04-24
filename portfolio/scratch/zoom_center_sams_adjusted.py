import fitz
import os
import cv2
import numpy as np

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
pdf_path = os.path.join(assets_dir, 'SAMS.pdf')
img_path = os.path.join(assets_dir, 'sams_pdf_thumb.jpg')

if os.path.exists(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
    img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    if pix.n == 4:
        img = cv2.cvtColor(img_data, cv2.COLOR_RGBA2BGR)
    else:
        img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
    doc.close()

    h, w = img.shape[:2]
    crop_h = int(h * 0.6)
    crop_w = int(w * 0.6)
    
    # Calculate center
    start_y = (h - crop_h) // 2
    start_x = (w - crop_w) // 2
    
    # "Move the logo up a little" means the logo is currently too low.
    # To move the logo UP in the final image, we must move the crop window DOWN.
    # Let's shift the crop window down by 8% of the total height.
    shift_down = int(h * 0.08)
    start_y = min(start_y + shift_down, h - crop_h)
    
    cropped = img[start_y:start_y+crop_h, start_x:start_x+crop_w]
    
    cv2.imwrite(img_path, cropped)
    print("Successfully adjusted SAMS thumbnail.")
else:
    print(f"File not found: {pdf_path}")
