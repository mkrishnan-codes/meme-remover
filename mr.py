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
count = 0
moved = 0
for filename in os.listdir(directory):
    count = count+1
    print(count)
    print('#-----processing '+filename+' --------#')
    if (filename.endswith(".jpg") | filename.endswith(".png")):
        currText = pytesseract.image_to_string(Image.open(directory+filename))
        if currText == "":
            print(' : No meme in ' + filename)
        else:
            moved = moved+1
            shutil.move(directory+filename, dest_folder)
            print(str(moved) + ' files moved -'+filename)
        continue
    else:
        print(filename, 'Not an image')
        continue
unmoved = count-moved
print('Total Processed = '+str(count))
print('Total moved = '+str(moved))
print('Unmoved = '+str(unmoved))
