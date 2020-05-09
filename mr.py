try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os
import shutil
directory = '/Users/manu/Documents/whatsapp/'
dest_folder = '/Users/manu/Documents/whatsapp/memes-separated'
pytesseract.pytesseract.tesseract_cmd = r'/usr/local/bin/tesseract'
# os.makedirs(dest_folder)
for filename in os.listdir(directory):

    if (filename.endswith(".jpg") | filename.endswith(".png")):
        currText = pytesseract.image_to_string(Image.open(directory+filename)
        if "".__eq__(currText):
            print('No meme')
            # print(pytesseract.image_to_string(Image.open(directory+filename)))
            # print(filename)
        # shutil.move(directory+filename, dest_folder)
        continue
    else:
        print(filename)
        continue
