# 🏡 WE-MORY Backend

## 🖥 서버 실행법

1. WeMory 폴더로 진입
2. python3 -m venv <가상환경이름>
3. source venv/bin/activate (MAC기준 가상환경 실행)
5. manage.py가 있는지 확인
6. pip install -r requirements.txt
7. secret.json 파일 WeMory/WeMory/에 넣기 (즉, manage.py가 있는 위치)
8. python3 manage.py makemigrations user
9. python3 manage.py makemigrations account
10. python3 manage.py makemigrations diary
12. python3 manage.py makemigrations post
13. python3 manage.py migrate
14. python3 manage.py runserver

## 👩‍👦 Team [Back]

- 17학번 사물인터넷학과 [김율희](https://github.com/yulhee741)
  - 일기 Model Rest API 설계 및 구현
  - 세부일기 Model API 설계 및 구현
  - 계좌 Model Rest API 설계 및 구현

- 18학번 컴퓨터공학과 [최세환](https://github.com/mactto3487)
  - User Model Rest API 설계 및 구현
  - JWT 토큰 인증 방식 구현
  - AWS EC2 + GUNICORN + NGINX + S3 백엔드 서버 배포
  - AWS CloudFront + S3 프론트 파트 어플리케이션 정적 배포

## 🔨Tech Stack

* 개발 스택
- Django
- DjangoRestFramework
- JWT
- SQLite

* 배포 스택
- AWS EC2
- AWS S3
- GUNICORN
- NGINX

