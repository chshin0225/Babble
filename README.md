# 👶🏻 AI 기반 육아 기록 서비스, Babble

## 프로젝트 개요

##### 슬로건

- 내 아이의 기록을 스마트하게 남기기, Babble

<br>



## 프로젝트 사용법

### Frontend

```bash
cd vue_front
npm i
npm run serve
```



### Backend

```bash
# 가상환경 먼저 실행 후 진행
cd django_server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```



## ERD

- https://www.erdcloud.com/d/gWqJhsXvpqD9qBvi9

![Babble](Babble.png)



## 주요 기능

- **AI 기반 사진 관리**
  - 사진 업로드 후 YOLO와 Deepface 모델을 이용한 사진 태그 추출
  - 태그를 기반으로 한 앨범 생성 및 사진 정리
- 감정 태그에 따른 사진 분류
- **일기 작성**
  - 육아일기 작성 및 관리
  - 일기와 함께 이미지를 추가한다면 Photo에 이미지 자동 추가
  - 일기 목록을 포토카드뷰, 타임라인뷰, 캘린더뷰 3 가지 모드로 제공
- **아기의 성장 기록 관리**
  -  몸무게, 신장, 머리둘레 기록 및 관리
  - 한눈에 볼 수 있는 그래프 및 통계 페이지 제공
- **권한 및 그룹 관리**
  - 생성자, 공동양육자, 손님으로 나뉘어진 권한 시스템
  - 외가, 친가, 지인 등 그룹 생성 및 그룹별 사진 및 다이어리에 대한 접근 권한 차등 부여

<br>



## 팀원

##### **Seulki Kang**

- 🍺Github: [@cocony12](https://github.com/cocony12)

##### **SunHwan Park**

- 🧙‍♂️Github: [@SunHwan-Park](https://github.com/SunHwan-Park)

##### **Chaewon Shin**  

- 🌮Github: [@chshin0225](https://github.com/chshin0225)

##### **Chae Lin Shin**

- 🍒Github: [@scl2589](https://github.com/scl2589)

##### **SoYun Bang**

- 🥨Github: [@bbangso](https://github.com/bbangso)

##### **Keunwoo Lee**

- 💪Github: [@lkwoo](https://github.com/lkwoo)

<br>

