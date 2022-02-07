from PIL import Image
import os
from glob import glob

def main():
    for photo in glob('/home/ubuntu/dataset/*'):
        # print(photo)
        if os.path.getsize(photo) > 15000:
          try:
            im = Image.open(photo)
            rgb_im = im.convert("RGB")
            new_name = photo.split('/')[-1].split('.')[0] + '.jpg'
            newsize = (1920, 1080)
            rgb_im = rgb_im.resize(newsize)
            rgb_im.save("/home/ubuntu/convert_dataset/" + new_name)
          except:
            continue
        

if __name__ == "__main__":
    main()