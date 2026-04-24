import fitz
import os
import cv2
import numpy as np

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
pdf_path = os.path.join(assets_dir, 'SAMS.pdf')
img_path = os.path.join(assets_dir, 'sams_pdf_thumb.jpg')

if os.path.exists(pdf_path):
    # Step 1: Extract full page from PDF
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3)) # High res
    # Convert pixmap to numpy array for cv2
    img_data = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.h, pix.w, pix.n)
    if pix.n == 4: # RGBA
        img = cv2.cvtColor(img_data, cv2.COLOR_RGBA2BGR)
    else: # RGB
        img = cv2.cvtColor(img_data, cv2.COLOR_RGB2BGR)
    doc.close()

    # Step 2: Center crop for zoom
    h, w = img.shape[:2]
    # Keep 70% of the center width/height
    crop_h = int(h * 0.6)
    crop_w = int(w * 0.6)
    
    start_y = (h - crop_h) // 2
    start_x = (w - crop_w) // 2
    
    cropped = img[start_y:start_y+crop_h, start_x:start_x+crop_w]
    
    cv2.imwrite(img_path, cropped)
    print(f"Successfully zoomed and centered SAMS thumbnail.")
else:
    print(f"File not found: {pdf_path}")
