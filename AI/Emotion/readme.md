# Emotion Recognition

## 주요 기능

> **감정인식과정**
>  1. Face Detect
>  2. Emotion Recognize

<p align="left"><img src="AI/Emotion/images/emotion_recogition_example.jpg" width="300" height="300"></p>

- Face Detect
  - 얼굴인식 모델은 대표적으로 ['opencv', 'ssd', 'dlib', 'mtcnn'] 가 있다.
  - <img src="https://i0.wp.com/sefiks.com/wp-content/uploads/2020/08/face-detector-perf.png?resize=768%2C422&ssl=1">
  - ssd가 가장 빠르다.
<br>


사진 속 감정 추출 과정
- 사진을 input으로 주면 특정 크기로 resize한다. (default 300*300)
- 얼굴 감지. mtcnn model 사용해 사진 속에 얼굴을 찾는다.
- 두 눈을 인식해 y좌표를 비교해 수평이 되도록 align 한다.
- 1 channel image(흑백)으로 변환한다.
- 48*48 크기로 resize 한다.
- deepface에서 만든 emotion recognition 모델로 감정을 추측한다.
- 7가지의 감정의 세기를 숫자로 나타낸다. (총합 100)


나중에 자세히 적어볼게욥
- Emotion Recognition
  - 7가지의 감정을 숫자로 표현한다.
  - ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral'] 이렇게 7가지

<br>

## 참고

- https://www.erdcloud.com/d/gWqJhsXvpqD9qBvi9
- https://www.inflearn.com/questions/29011
- https://sefiks.com/2020/08/25/deep-face-detection-with-opencv-in-python/
- https://sefiks.com/2020/05/01/a-gentle-introduction-to-face-recognition-in-deep-learning/ 
