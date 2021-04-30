# WEMORY-Backend


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
11. python3 manage.py migrate
12. python3 manage.py runserver
