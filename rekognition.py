import boto3
from glob import glob
import json
import os
from PIL import Image

def main():
    for photo in glob('/home/ubuntu/convert_dataset/*'):
        # print(photo)
        detect_labels_local_file(photo)
        #print("Labels detected: " + str(label_count))

def detect_labels_local_file(photo):

    client=boto3.client('rekognition')
   
    with open(photo, 'rb') as image:
        response = client.detect_labels(Image={'Bytes': image.read()})
        move_image = True
        for label in response['Labels']:
          if label['Name'] == 'Zebra' and len(label['Instances']) != 0 and label['Confidence'] > 0.6:
            if move_image:
              os.rename(photo, "/home/ubuntu/data/images/" + photo.split('/')[-1])
              move_image = False
            im = Image.open("/home/ubuntu/data/images/" + photo.split('/')[-1])
            rgb_im = im.convert("RGB")
            imgWidth, imgHeight = rgb_im.size
            with open('/home/ubuntu/data/labels/' +  photo.split('/')[-1].split('.')[0] + '.txt','w') as label_file:
              for obj in label['Instances']:
                box = obj['BoundingBox']
                left = imgWidth * box['Left']
                top = imgHeight * box['Top']
                width = imgWidth * box['Width']
                height = imgHeight * box['Height']
                
                # Convert COCO bbox coords to Kitti ones
                box = [left, top, width + left, height + top]
                box = [str(b) for b in box]
                
                out_str = [label['Name'] + ' 0.00' + ' 0' + ' 0.00'
                           + ' ' + box[0] + ' ' + box[1] + ' ' + box[2]
                           + ' ' + box[3] + ' 0.00' + ' 0.00' + ' 0.00'
                           + ' 0.00' + ' 0.00' + ' 0.00' + ' 0.00' + '\n']
                label_file.write(out_str[0])
            break
        
    #return len(response['Labels'])

if __name__ == "__main__":
    main()