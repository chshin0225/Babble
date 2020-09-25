# Emotion Recognition

## 주요 기능

> **감정인식과정**
>  1. Face Detect
>  2. Emotion Recognize

- Face Detect
  - 얼굴인식 모델은 대표적으로 ['opencv', 'ssd', 'dlib', 'mtcnn'] 가 있다.
  - <img src="https://i0.wp.com/sefiks.com/wp-content/uploads/2020/08/face-detector-perf.png?resize=768%2C422&ssl=1">
  - ssd가 가장 빠르다. 이걸로 바꿔야징^^
  1. 사진을 input으로 주면 특정 크기로 resize한다. (default 300*300)
  2. 나중에 자세히 적어볼게욥
  <br>

- Emotion Recognition
  - 7가지의 감정을 숫자로 표현한다.

<br>

## 참고

- https://www.erdcloud.com/d/gWqJhsXvpqD9qBvi9
- https://www.inflearn.com/questions/29011
- https://sefiks.com/2020/08/25/deep-face-detection-with-opencv-in-python/
- https://sefiks.com/2020/05/01/a-gentle-introduction-to-face-recognition-in-deep-learning/ 
