try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
directory = './'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        print(pytesseract.image_to_string(Image.open(filename)))
        continue
    else:
        continue

