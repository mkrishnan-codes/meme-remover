try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import shutil
directory = './samples/'
dest_folder = './samples/separated/'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
os.makedirs(dest_folder)
for filename in os.listdir(directory):

    if (filename.endswith(".jpg") | filename.endswith(".png")):
        print(pytesseract.image_to_string(Image.open(filename)))
        print(filename)
        shutil.move(directory+filename, dest_folder)
        continue
    else:
        print(filename)
        continue
