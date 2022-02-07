"""Perform test request"""
import pprint
import time
from glob import glob

import requests

DETECTION_URL = "http://localhost:5000/v1/object-detection/yolov5s"
TEST_IMAGE = "/usr/src/app/datasets/zebra/images/train/10064577.jpg"

image_data = open(TEST_IMAGE, "rb").read()

avg_lat = 0
time.time()
count = 1
responses = []
for file_name in glob('/usr/src/app/zebra_data/images/*'):
    DETECTION_URL = "http://localhost:5000/v1/object-detection/yolov5s"
    TEST_IMAGE = file_name
    image_data = open(TEST_IMAGE, "rb").read()
    before = time.time()
    response = requests.post(DETECTION_URL, files={"image": image_data}).json()
    after = time.time()
    avg_lat += after - before
    count += 1
    responses.append(response)
avg_lat = avg_lat/count

pprint.pprint(response)

responses
