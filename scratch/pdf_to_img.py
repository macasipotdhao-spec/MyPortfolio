import fitz
import os

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')

pdfs = [
    ('SAMS.pdf', 'sams_pdf_thumb.jpg'),
    ('SmartSched.pdf', 'smartsched_pdf_thumb.jpg')
]

for pdf_name, img_name in pdfs:
    pdf_path = os.path.join(assets_dir, pdf_name)
    img_path = os.path.join(assets_dir, img_name)
    if os.path.exists(pdf_path):
        try:
            doc = fitz.open(pdf_path)
            page = doc.load_page(0)  # first page
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # upscale for better quality
            pix.save(img_path)
            print(f"Saved {img_path}")
            doc.close()
        except Exception as e:
            print(f"Error processing {pdf_name}: {e}")
    else:
        print(f"File not found: {pdf_path}")
