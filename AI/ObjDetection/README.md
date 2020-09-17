# keras-yolo3

[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](LICENSE)


## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/).
2. Convert the Darknet YOLO model to a Keras model.
3. Run YOLO detection.

```
wget https://pjreddie.com/media/files/yolov3.weights
python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5
```


### Usage
Use --help to see usage of yolo_video.py

objDetection.py 에서 입력으로 하고자하는 이미지 path를 설정한다.
```bash
$ python objDetection.py
```
---

## 의존성 라이브러리

* 다음과 같은 환경에서 진행했습니다.
    - Python 3.7.9
    - Keras 2.1.5
    - tensorflow 1.15.0
