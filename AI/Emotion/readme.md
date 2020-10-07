# Emotion Recognition

## 주요 기능

> **감정인식과정**
>  1. Face Detect
>  2. Emotion Recognize
<p align="center"><img src="https://raw.githubusercontent.com/serengil/deepface/master/icon/deepface-icon-labeled.png" width="200" height="240"></p>
- Face Detect
  - 얼굴인식 모델은 대표적으로 ['opencv', 'ssd', 'dlib', 'mtcnn'] 가 있다.
  - <img src="https://i0.wp.com/sefiks.com/wp-content/uploads/2020/08/face-detector-perf.png?resize=768%2C422&ssl=1">
  - ssd가 가장 빠르다.
<br>  
1. 사진을 input으로 주면 특정 크기로 resize한다. (default 300*300)

<br>
<br>
2. Face detect<br>

- 얼굴 감지. mtcnn model 사용
- 두 눈을 인식해 y좌표를 비교해 수평이 되도록 align
- 1 channel image(흑백)으로 변환
- resize 48*48
- get emotion


<br>
<br>
3. 나중에 자세히 적어볼게욥
<br>

- Emotion Recognition
  - 7가지의 감정을 숫자로 표현한다.
  - ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'] 이렇게 7가지

<br>

## 참고

- https://www.erdcloud.com/d/gWqJhsXvpqD9qBvi9
- https://www.inflearn.com/questions/29011
- https://sefiks.com/2020/08/25/deep-face-detection-with-opencv-in-python/
- https://sefiks.com/2020/05/01/a-gentle-introduction-to-face-recognition-in-deep-learning/ 
