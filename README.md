# 장고 공부

- 기본적인 내용은 노션에 정리되어 있습니다!

- 장고 기초
  
  https://www.notion.so/ssafy-gyur1kim/Django-67e84aa300c24b2ba64f96d9ca717e7c

- REST API
  
  https://www.notion.so/ssafy-gyur1kim/REST-API-94c80266e9704bf19c3c9b56695f18af

---

# 장고 시작하기(+rest framework)

1. 가상환경 설정, 실행
   
   `python -m venv venv`
   
   `source venv/Scripts/activate`

2. 다운받기
   
   `pip install django==3.2.13`
   
   `pip install djangorestframework`
   
   - requirements.txt 파일이 있다면?
     
     `pip install -r requirements.txt`
   
   `pip freeze > requirements.txt` 진행하면 다른 사람이 나와 동일한 환경에서 장고를 실행할 수 있음!

3. 장고 프로젝트 생성하기
   
   `django-admin startproject [mypjt] .` 

4. 앱 생성하기
   
   `python manage.py startapp [app_name]`

5. settings.py에 등록하기
   
    `[프로젝트] - settings.py - INSTALLED_APP` 에 등록할 것!
   
   1. 생성한 앱
   
   2. `rest_framework`  

6. 장고 실행하기
   
   `python manage.py runserver`

---

# REST API에서

### 역참조 할 때

- 내 필드에 외래키가 없음 -> 역참조 매니저를 이용해 받아온다

- 내 필드에 외래키로 존재함 ->


