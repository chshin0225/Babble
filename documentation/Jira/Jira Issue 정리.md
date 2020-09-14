# Jira Issue

>  Issue별로 정리를 하고, Epic/Story/Task로 나누었습니다.

>  Epic은 기능 단위, Story는 각 기능의 CRUD 및 페이지 단위로 작성, 마지막으로 Task는 페이지 안에 세부적인 내용들 (+오류)를 기준으로 작성하였습니다.

<br>

## Frontend

### [Frontend] 개발환경 세팅 - Epic



### [Frontend] Navbar/Sidebar- Epic

- Navbar에 각 메뉴 및 아이콘 추가해서 넣기 - Story

- Sidebar 완성하기 - Story
- 아이들 더보기 페이지 생성 - Story

<br>

### [Frontend] Authentication - Epic

- 회원가입 페이지 생성 - Story
  - 회원가입 페이지 디자인 - Task
  - 회원가입 Input별 경고 메시지 출력 - Task
  - 회원가입 Axios 요청 - Task
- 아기 등록 페이지 생성 - Story
  - 아기 등록/ Babble Box 초대 선택 페이지 생성 - Task
  - 아기 등록 페이지 생성 - Task
  - Babble Box 초대 코드 입력 페이지 생성 - Task
  - 관계 설정 페이지 생성 - Task
- 로그인 페이지 생성 - Story
  - 로그인 페이지 디자인 - Task
  - 로그인 Input별 경고 메시지 출력 - Task
  - 로그인 Axios 요청 - Task
- 로그아웃 기능 구현- Story
- 패스워드 찾기 페이지 생성 - Story (상의 필요)
  - 패스워드 찾기 페이지 (이메일 입력) 디자인 - Task
  - 코드 입력 페이지 디자인 - Task
  - 패스워드 변경 완료 페이지 생성 - Task



<br>

### [Frontend] Photo- Epic

- 공통 Photo Navbar 페이지 - Story

- 전체 사진 뷰 페이지 - Story
- 앨범 검색 페이지 - Story
- 사진 디테일 페이지 - Story
  - 사진 삭제 - Task
- 사진 업로드 페이지 - Story
- 사진 라이브러리 페이지 - Story
- 앨범 생성 페이지 - Story
  - 사진 추가 페이지 - Task
  - 태그 추가 페이지 - Task
- 앨범 디테일 페이지 - Story
- 앨범 설정- Story
  - 앨범 설정 창 - Task
  - 앨범 수정 창 - Task
  - 앨범 표지 선택 - Task
  - 앨범 삭제 - Task

<br>

### [Frontend] Diary - Epic

- 다이어리 추가 버튼 구현 - Task

- 다이어리 포토카드 뷰 페이지 - Story
- 다이어리 캘린더 뷰 페이지 - Story
  - 다이어리 작성한 날 구분 - Task
- 다이어리 타임라인 뷰 페이지 - Story
- 다이어리 디테일 페이지 - Story
  - 다이어리 공유하기 - Task
- 다이어리 작성 페이지 - Story
  - 에디터 기능 추가 - Task
  - 신장 및 몸무게 기록 추가 - Task
- 다이어리 수정 페이지 - Story
- 다이어리 삭제 - Story

<br>

### [Frontend] Settings - Epic

- Babble Box 유저 관리 페이지 - Story

<br>

### [Frontend] Statistics - Epic

- 키 - 성장 그래프 -  Story
  - 상위 % 기입 - Task

<br>

## 나중에 개발

### [Frontend] Notification - Epic

- 알림 센터 디자인 - Story
  - 각 탭 전환 시 해당 탭이 선택되어 있음을 강조 - Task
  - 유저가 확인하지 않은 신규 알림 존재시 '새 알림' 표시 - Task
- Firestore로 알림 실시간 업데이트 - Story
- 알림 랩 구현 - Story
  - 댓글 생성 시 알림 노출 - Task
  - 신규 및 기존 알림 구분하여 노출 - Task



## AI

### [AI] Photo - Epic

- 이미지 태그 - Story
- 표정 인식 - Story 
- 얼굴 인식 - Story



## Backend

### [Backend] 개발환경 세팅 - Epic

- Django 프로젝트 생성 - Story
- Django 프로젝트 ec2 배포 - Story
- Django DB 연결 - Story
- Django Nginx 연동 - Story
- Django https 설정 - Story

### [Backend] User - Epic

- 로그인  - Story
  - 자체 로그인 - Task
  - OAuth 로그인(상의 필요) - Task
- 회원가입  - Story
  - 자체 회원가입 - Task
  - OAuth 회원가입(상의 필요) - Task
- 비밀번호 찾기(상의 필요) - Story
  - 이메일 검증 - Task
  - 비밀번호 재설정 - Task
- 마이페이지 - Story
  - 계정 정보 조회 - Task
  - 계정 정보 수정 - Task
  - 계정 삭제 - Task

### [Backend] Baby - Epic

- Baby CRUD - Story
  - Baby 생성 - Task
  - Baby List 조회 - Task
  - Baby Detail 조회 - Task
  - Baby 수정 - Task
  - Baby 삭제 - Task
- Baby 성장 통계 - Story
  - 성장 통계 조회
- Baby 공유 - Story
  - 공유 URL 생성 - Task
  - 공유 유저 등록 - Task
  - 공유 유저 조회 - Task
  - 공유 유저 권한 수정 - Task
  - 공유 유저 삭제 - Task

### [Backend] Photo - Epic

- Repo CRUD - Story
  - Repo 생성 - Task
  - Repo 조회 - Task
  - Repo 수정 - Task
  - Repo 삭제 - Task
- Photo CRUD - Story
  - Photo 생성 - Task
  - Photo List 조회 - Task
  - Photo Detail 조회 - Task
  - Photo 수정 - Task
  - Photo 삭제 - Task
- Photo 검색 - Story
  - Tag 검색 조회 - Task
- Photo 북마크 - Story
  - Photo 북마크 정보 입력 - Task
  - 북마크된 Photo 조회 - Task
- Photo_Comment CRUD - Story
  - Photo_Comment 생성 - Task
  - Photo_Comment List 조회 - Task
  - Photo_Comment 수정 - Task
  - Photo_Comment 삭제 - Task
- Photo Content - Story
  - 요약 비디오 생성 - Task
  - 아이 얼굴 성장과정 비디오 생성 - Task
  - 성인이 된 아이 얼굴 이미지 생성 - Task

### [Backend] Album - Epic

- Album CRUD - Story
  - Album 생성 - Task
  - Album List 조회 - Task
  - Album Detail 조회 - Task
  - Album 수정 - Task
  - Album 삭제 - Task

### [Backend] Diary - Epic

- Diary CRUD - Story
  - Diary 생성 - Task
  - Diary List 조회 - Task
  - Diary Detail 조회 - Task
  - Diary 수정 - Task
  - Diary 삭제 - Task
- Diary 검색 - Story
  - Tag 검색 조회 - Task
  - 제목/내용 검색 조회 - Task
- Diary 북마크 - Story
  - Diary 북마크 정보 입력 - Task
  - 북마크된 Photo 조회 - Task
- Diary_Comment CRUD - Story
  - Diary_Comment 생성 - Task
  - Diary_Comment List 조회 - Task
  - Diary_Comment 수정 - Task
  - Diary_Comment 삭제 - Task
- Diary 모음집 - Story
  - Diary 모음집 생성 - Task

### [Backend] Tag - Epic

- Tag CRUD - Story
  - Tag 생성 - Task
  - Tag List 조회 - Task
  - Tag 수정 - Task
  - Tag 삭제 - Task

### [Backend] Notification - Epic(상의 필요)

- Firestore를 활용한 알림 - Story
  - 새로운 Photo 등록 알림 - Task
  - 새로운 Baby 공유 유저 등록 알림 - Task
  - 새로운 Diary 등록 알림 -  Task
  - Photo 댓글 알림 - Task
  - Diary 댓글 알림 - Task