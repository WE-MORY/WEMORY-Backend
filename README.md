# ๐ก WE-MORY Backend

## ๐ป DEMO

### ํ์๊ฐ์/๋ฉ์ธ/์ผ๊ธฐ๋ฆฌ์คํธ

<span>
  <img src="./DEMO/Wemory_ํ์๊ฐ์.gif" width="240px" />
</span>

<span>
  <img src="./DEMO/Wemory_๋ฉ์ธ.gif" width="240px" />
</span>

<span>
  <img src="./DEMO/Wemory_์ผ๊ธฐ๋ฆฌ์คํธ.gif" width="240px" />
</span>

### ์ถ๊ธ๊ณ์ข ๋ฑ๋ก/์ถ๊ธ ๊ทธ๋ํ

<span>
  <img src="./DEMO/Wemory_์ถ๊ธ๊ณ์ข๋ฑ๋ก.gif" width="240px" />
</span>

<span>
  <img src="./DEMO/Wemory_์ถ๊ธ๊ทธ๋ํ.gif" width="240px" />
</span>

## ๐ฅ ์๋ฒ ์คํ๋ฒ

1. WeMory ํด๋๋ก ์ง์
2. python3 -m venv <๊ฐ์ํ๊ฒฝ์ด๋ฆ>
3. source venv/bin/activate (MAC๊ธฐ์ค ๊ฐ์ํ๊ฒฝ ์คํ)
5. manage.py๊ฐ ์๋์ง ํ์ธ
6. pip install -r requirements.txt
7. secret.json ํ์ผ WeMory/WeMory/์ ๋ฃ๊ธฐ (์ฆ, manage.py๊ฐ ์๋ ์์น)
8. python3 manage.py makemigrations user
9. python3 manage.py makemigrations account
10. python3 manage.py makemigrations diary
12. python3 manage.py makemigrations post
13. python3 manage.py migrate
14. python3 manage.py runserver

## ๐ฉโ๐ฆ Team [Back]

- 17ํ๋ฒ ์ฌ๋ฌผ์ธํฐ๋ทํ๊ณผ [๊น์จํฌ](https://github.com/yulhee741)
  - ์ผ๊ธฐ Model Rest API ์ค๊ณ ๋ฐ ๊ตฌํ
  - ์ธ๋ถ์ผ๊ธฐ Model API ์ค๊ณ ๋ฐ ๊ตฌํ
  - ๊ณ์ข Model Rest API ์ค๊ณ ๋ฐ ๊ตฌํ

- 18ํ๋ฒ ์ปดํจํฐ๊ณตํ๊ณผ [์ต์ธํ](https://github.com/mactto3487)
  - User Model Rest API ์ค๊ณ ๋ฐ ๊ตฌํ
  - JWT ํ ํฐ ์ธ์ฆ ๋ฐฉ์ ๊ตฌํ
  - AWS EC2 + GUNICORN + NGINX + S3 ๋ฐฑ์๋ ์๋ฒ ๋ฐฐํฌ
  - AWS CloudFront + S3 ํ๋ก ํธ ํํธ ์ดํ๋ฆฌ์ผ์ด์ ์ ์  ๋ฐฐํฌ

## ๐จTech Stack

* ๊ฐ๋ฐ ์คํ
- Django
- DjangoRestFramework
- JWT
- SQLite

* ๋ฐฐํฌ ์คํ
- AWS EC2
- AWS S3
- GUNICORN
- NGINX

=======
