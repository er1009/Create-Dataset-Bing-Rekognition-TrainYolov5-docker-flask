import os
import shutil
from glob import glob

path, dirs, files = next(os.walk('/usr/src/app/zebra_data/labels_yolo/'))
file_count = len(files)
train_count = int(file_count*0.8)
val_count = file_count - train_count

count = 0

for file_name in glob('/usr/src/app/zebra_data/labels_yolo/*'):
    sample_id = file_name.split('/')[-1].split('.')[0]
    img_name = file_name.split('/')[-1].split('.')[0] + '.jpg'
    img_path = '/usr/src/app/zebra_data/images/' + img_name
    if count < train_count:
        shutil.copy2(file_name, '/usr/src/app/datasets/zebra/labels/train')
        shutil.copy2(img_path, '/usr/src/app/datasets/zebra/images/train')
    else:
        shutil.copy2(file_name, '/usr/src/app/datasets/zebra/labels/val')
        shutil.copy2(img_path, '/usr/src/app/datasets/zebra/images/val')
    count += 1