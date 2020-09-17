from yolo import YOLO
from PIL import Image

path = './playtime.jpg'
image = Image.open(path)

yolo = YOLO()
tags = yolo.extract_tag(image)
print(tags)
yolo.close_session()

