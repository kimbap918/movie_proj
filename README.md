## 페어프로그래밍 가이드

개발 환경 설정을 제외한 모든 토픽 개발은 아래 순서에 따라 진행합니다.

1. [로컬/드라이버] main 브랜치에서 개발 토픽에 해당하는 브랜치 생성 및 브랜치 전환

   ```bash
   # 브랜치 생성 & 전환
   git checkout -b [토픽 브랜치명]
   
   # git checkout [브랜치명] : 브랜치를 전환합니다.
   # git checkout -b [브랜치명] : 브랜치를 생성하고 전환합니다. 동일한 브랜치가 있으면 오류가 발생합니다.
   ```

2. [로컬/드라이버] 토픽 개발

3. [로컬/드라이버] 토픽 개발 후 동일한 이름의 원격 저장소 브랜치에 Commit&Push

   ```bash
   git add .
   
   git commit -m '커밋 메세지'
   
   git push origin [토픽 브랜치명]
   ```

4. [원격/드라이버] 토픽 브랜치 병합

   1. 깃허브 PR 생성(토픽 브랜치 → main 브랜치)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/26e2083c-b2d5-4a8a-b700-ce32105916b3/Untitled.png)

   2. 브랜치 병합(토픽 브랜치 → main 브랜치)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dcb1d4ef-2f39-4b36-991b-cfd1ffe561c6/Untitled.png)

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4c24962f-5b89-4c21-aab7-d055a98caf89/Untitled.png)

   3. 토픽 브랜치 삭제

      ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bd4813a2-ea1a-4e7b-beff-52e6884b07f0/Untitled.png)

5. [로컬/전체] main 브랜치 전환 후 Pull

   ```bash
   # main 브랜치로 전환
   git checkout main
   
   # main 브랜치 Pull
   git pull origin main
   ```

6. [로컬/드라이버] 토픽 브랜치 삭제

   ```bash
   # 토픽 브랜치 삭제
   git branch -d [토픽 브랜치명]
   ```

7. 드라이버 변경 후 1번 부터 시작

## 깃 브랜치 명령어

```bash
# 브랜치 생성 & 전환
git checkout -b [브랜치명]

# 브랜치 전환
git checkout [브랜치명]

# 브랜치 삭제
git branch -d [브랜치명]

# 브랜치 이름 변경
git branch -m [기존 브랜치명] [변경할 브랜치명]
```

## 목표

페어 프로그래밍을 통한 영화 리뷰 커뮤니티 서비스를 개발합니다. 아래 조건을 만족해야합니다.

- **CRUD** 구현
- **Staticfiles** 활용 정적 파일(이미지, CSS, JS) 다루기
- Django **Auth** 활용 회원 관리(회원가입 / 회원 조회 / 로그인 / 로그아웃)

## 토픽

### 1. 깃 설정

branch main

- 원격 저장소 생성

- 콜라보레이터 초대

- 로컬 저장소 깃 초기화

  ```bash
  git init
  ```

- 로컬 저장소 .gitignore 생성

  ```bash
  touch .gitignore
  ```

- .gitignore 작성

  - 아래 사이트 입력창에 필요한 언어 & 프레임워크 & 환경 입력 후 생성

  [gitignore.io](https://www.toptal.com/developers/gitignore/)

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] main → [원격/드라이버] main, Commit & Push 수행 [원격/전체] 저장소 Clone 수행 드라이버 변경 [로컬/새 드라이버] setup-django 브랜치에서 다음 토픽 진행

</aside>

------

### 2. 장고 개발환경 설정

branch setup-django

Django 프로젝트 생성

- 가상환경 생성 & 실행

- 필요한 패키지 설치

  주의

  ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d49ddbaf-6c78-4244-973d-0206774246d2/Untitled.png)

- 패키지 목록 저장

  ```bash
  pip freeze > requirements.txt
  ```

- Django 프로젝트 생성

  ```bash
  django-admin startproject config .
  ```

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] setup-django → [원격/드라이버] setup-django, Commit & Push 수행 [원격/드라이버] setup-django → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] setup-django 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] setup-django 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/signup 브랜치에서 다음 토픽 진행

</aside>

### 1. 사전 설정

		#### settings.py

``` python
import os

INSTALLED_APPS = [
    'movie',
    'django_bootstrap5',
  	...
]

TEMPLATES = [  "DIRS": [BASE_DIR / "moviepjt" / "templates"], # BASE_DIR / "프로젝트폴더명" / "템플릿폴더명"
            ]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'config', 'static') # 추가
]

AUTH_USER_MODEL = 'movie.User' # 추가 
```

<br>

#### url 분리

애플리케이션 폴더

templates > movie 폴더 생성

urls.py 파일 생성

#### urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    
]
```

<br>

project 폴더

templates 폴더 생성

#### urls.py 

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls'))
]
```

<br>

templates 폴더 내 base.html 생성

#### base.html

``` html
{% load django_bootstrap5 %}
<!DOCTYPE html>
<html lang="ko">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    {% bootstrap_css %}
    {% block css %}{% endblock css %}
  </head>

  <body>
    <div class="container">
      {% block body %}{% endblock body %}
    </div>
    {% bootstrap_javascript %}
  </body>

</html>
```



------

### 2. 회원가입

branch accounts/signup

앱 App

앱 이름 : accounts

모델 Model

모델 이름 : User

- Django **AbstractUser** 모델 상속

  #### models.py

  ``` python
  from django.db import models
  from django.contrib.auth.models import AbstractUser
  
  # Create your models here.
  class User(AbstractUser):
      pass
  ```

<br>

#### terminal

``` python
> python manage.py makemigrations
> python manage.py migrate
```

<br>

**폼 Form**

- Django 내장 회원가입 폼 UserCreationForm을 상속 받아서 CustomUserCreationForm 작성

  해당 폼은 아래 필드만 출력합니다.

  - username
  - password1
  - password2

#### forms.py

``` python
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')
```

<br>

**기능 View**

회원가입

- `POST` http://127.0.0.1:8000/accounts/signup/
- CustomUserCreationForm을 활용해서 회원가입 구현

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]
```

<br>

#### views.py

``` python
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'movie/signup.html', context)
```

<br>

#### app folder > signup.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block body %}
  <h1>회원가입</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    <button class="btn btn-outline-primary">제출하기</button>
  </form>
{% endblock body %}
```

<br>

**화면 Template**

회원가입 페이지

- `GET` http://127.0.0.1:8000/accounts/signup/
- 회원가입 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/signup → [원격/드라이버] accounts/signup, Commit & Push 수행 [원격/드라이버] accounts/signup → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/signup 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] accounts/signup 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/login 브랜치에서 다음 토픽 진행

</aside>

------

### 3. 로그인

branch accounts/login

**폼 Form**

로그인

- Django 내장 로그인 폼 **AuthenticationForm 활용**

**기능 View**

로그인

- `POST` http://127.0.0.1:8000/accounts/login/
- **AuthenticationForm**를 활용해서 로그인 구현

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
```

<br>

#### views.py

``` python
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('authapp:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'authapp/login.html', context)
```

<br>

#### app folder > login.html

``` python
{% extends 'base.html' %}
{% load django_bootstrap5 %}

{% block body %}
  <h1>로그인</h1>
  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" content="OK" %}
    {% comment %} <button class="btn btn-outline-primary col-12">로그인</button> {% endcomment %}
  </form>
{% endblock %}
```

<br>

**화면 Template**

로그인 페이지

- `GET` http://127.0.0.1:8000/accounts/login/
- 로그인 폼
- 회원가입 페이지 이동 버튼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/login → [원격/드라이버] accounts/login, Commit & Push 수행 [원격/드라이버] accounts/login → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/login 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 [로컬/드라이버] accounts/login 브랜치 삭제 드라이버 변경 [로컬/새 드라이버] accounts/index 브랜치에서 다음 토픽 진행

</aside>

------

### 4. 회원 목록 조회

`branch` accounts/index

**기능 View**

회원 목록 조회

- `GET` http://127.0.0.1:8000/accounts/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
]
```

<br>

#### views.py

``` python
def accounts(request):
    accounts = get_user_model().objects.order_by('-pk')
    context = {
        'accounts': accounts
    }
    return render(request, 'movie/accounts.html', context)
```

<br>

#### app folder > accounts.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block body %}
  <div class="col-lg-9 col-md-12 px-5 mb-3">
    <!-- 테이블 영역 -->
    <table class="table">
      <!-- 테이블 헤드 -->
      <thead class="table-light">
        <tr>
          <th scope="col">PK</th>
          <th scope="col">USER NAME</th>
          <th scope="col">EMAIL</th>
        </tr>
      </thead>
      <!-- 테이블 바디 -->
      <tbody class="table-group-divider">
        {% for account in accounts %}
          <tr>
            <th>{{ account.pk }}</th>
            <th>
              {% comment %} < href="{% url 'movie:detail' account.pk %}"> {% endcomment %}
                {{ account.username }}
            </th>

            <th>{{ account.email }}</th>

          </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>
{% endblock body %}

```

<br>

**화면 Template**

회원 목록 페이지

- `GET` http://127.0.0.1:8000/accounts/
- 회원 목록 출력
- 회원 아이디를 클릭하면 해당 회원 조회 페이지로 이동

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/index → [원격/드라이버] accounts/index, Commit & Push 수행 [원격/드라이버] accounts/index → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/index 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/detail 브랜치에서 다음 토픽 진행

</aside>

------

### 5. 회원 정보 조회

`branch` accounts/detail

**기능 View**

회원 정보 조회

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
]
```

<br>

#### views.py

``` python
def detail(request, pk):
  user = get_user_model().objects.get(pk=pk)
  context = {
    'user': user
    }
  return render(request, 'movie/detail.html', context)
```

<br>

#### app folder > detail.html

``` html
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block body %}
  <h1>상세 페이지</h1>
  <div class="mb-3 mt-3">
    <label for="userpk" class="form-label">순번</label>
    <textarea name='content' class="form-control" id="userpk" rows="3" disabled="disabled" readonly="readonly">{{ user.pk }}</textarea>
  </div>
  <div class="mb-3">
    <label for="username" class="form-label">유저명</label>
    <textarea name='content' class="form-control" id="username" rows="3" disabled="disabled" readonly="readonly">{{ user.username }}</textarea>
  </div>
  <div class="mb-3">
    <label for="useremail" class="form-label">이메일</label>
    <textarea name='content' class="form-control" id="useremail" rows="3" disabled="disabled" readonly="readonly">{{ user.email }}</textarea>
  </div>
  <div class="mt-2">
    <a href="{% url 'movie:update' %}">
      <button class="btn btn-outline-primary">수정하기</button>
    </a>
  </div>
{% endblock body %}
```

<br>

**화면 Template**

회원 조회 페이지(프로필 페이지)

- `GET` http://127.0.0.1:8000/accounts/[int:user_pk](int:user_pk)/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/detail → [원격/드라이버] accounts/detail, Commit & Push 수행 [원격/드라이버] accounts/detail → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/detail 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/update 브랜치에서 다음 토픽 진행

</aside>

------

### 6. 회원 정보 수정

branch accounts/update

**폼 Form**

회원 정보 수정

- Django 내장 회원 수정 폼 UserChangeForm을 상속 받아서 **CustomUserChangeForm** 작성

  해당 폼은 아래 필드만 출력합니다.

  - first_name
  - last_name
  - email

#### forms.py

``` python
from django.contrib.auth.forms import UserChangeForm

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
```

<br>

**기능 View**

회원 정보 수정

- `POST` http://127.0.0.1:8000/accounts/<user_pk>/update/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
]
```

<br>

#### views.py

``` python
from .forms import CustomUserChangeForm
from django.contrib.auth.decorators import login_required

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('movie:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'movie/update.html', context)
```

<br>

**화면 Template**

회원 정보 수정 페이지

- `GET` http://127.0.0.1:8000/accounts/<user_pk>/update/

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/update → [원격/드라이버] accounts/update, Commit & Push 수행 [원격/드라이버] accounts/update → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/update 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] accounts/logout 브랜치에서 다음 토픽 진행

</aside>

------

### 7. 로그아웃

branch accounts/logout

**기능 View**

로그아웃

- `POST` http://127.0.0.1:8000/accounts/logout/

#### proj folder > base.html

``` html
{% load django_bootstrap5 %}
<!DOCTYPE html>
<html lang="ko">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    {% bootstrap_css %}
    {% block css %}{% endblock css %}
  </head>

  <body>
    {% if request.user.is_authenticated %}
      <span>{{ request.user }}님, 환영합니다.</span>
      <a href="{% url 'movie:logout' %}">로그아웃</a>
    {% else %}
      <span>로그인해주세요.</span>
    {% endif %}
    <div class="container">
      {% block body %}{% endblock body %}
    </div>
    {% bootstrap_javascript %}
  </body>
</html>
```

<br>

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
]
```

<br>

#### views.py

``` python
from django.contrib.auth import logout as auth_logout

def logout(request):
  auth_logout(request)
  return redirect('movie:index')
```

<br>

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] accounts/logout → [원격/드라이버] accounts/logout, Commit & Push 수행 [원격/드라이버] accounts/logout → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] accounts/logout 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] template/navbar 브랜치에서 다음 토픽 진행

</aside>

------

### 8. 네비게이션바

branch template/navbar

**화면 Template**

**네비게이션바**

- 리뷰 목록 페이지 이동 버튼
- 리뷰 작성 페이지 이동 버튼
  - 비 로그인 유저는 작성 버튼 출력 X
- 로그인 상태에 따라 다른 화면 출력
  1. 로그인 상태
     - 로그인 한 사용자의 username 출력
       - username을 클릭하면 회원 조회 페이지로 이동
     - 로그아웃 버튼
  2. 비 로그인 상태
     - 로그인 페이지 이동 버튼
     - 회원가입 페이지 이동 버튼

#### base.html

``` python
{% load django_bootstrap5 %}
{% load static %}

<!DOCTYPE html>
<html lang="ko">

  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BobMovie</title>
    <style>
      @font-face {
        font-family: "NetflixSans";
        src: url("fonts/NetflixSans-Regular.woff2") format("woff2");
        font-weight: normal;
        font-style: normal;
      }

      * {
        font-family: 'NetflixSans';
      }

      .nav-logo {
        width: 5rem;
        object-fit: cover;
      }

      a {
        text-decoration: none;
        color: inherit;
      }
    </style>
    {% bootstrap_css %}
    {% block css %}
      <link rel="stylesheet" href="{% static 'css/movie.css' %}">
    {% endblock css %}

  </head>

  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="nav mx-1">
        <a href="{% url 'movie:index' %}"><img class="nav-logo mx-1" src="https://user-images.githubusercontent.com/66688033/193211411-15f19a4c-d81f-409c-955a-ec224c8671be.png"/></a>
      </div>
      <button class="navbar-toggler mx-3" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- 두 항목을 오른쪽으로 밀기 .me-auto -->
        <!-- .navbar-nav으로 full-height와 보다 가벼운 네비게이션(드롭다운을 위한 지원 포함)을 실현. -->
        <ul class="navbar-nav mb-2 mx-3 mb-lg-0 ms-lg-4 align-items-end">
          <li class="nav-item">
            <a class="nav-link active" href="{% url 'movie:index' %}">Home</a>
          </li>
          <li class="nav-item">
            {% comment %} <a class="nav-link" href="{% url 'movie:community' %}">Community</a> {% endcomment %}
          </li>
          {% if request.user.is_authenticated %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'movie:logout' %}">Logout</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:white;" href="{% url 'movie:detail' user.pk %}">{{ request.user }}님, 환영합니다.</a>
          </li>
          {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'movie:signup' %}">Join</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'movie:login' %}">Login</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" style="color:white;">로그인 해주세요</a>
          </li>
          {% endif %}
        </ul>
      </div>
    </nav>
    {% block body %}{% endblock body %}
    <footer class="py-3 bg-dark col-12 position-fixed bottom-0">
      <div class="container px-4 px-lg-5">
        <p class="m-0 text-center text-white">Web Bootstrap PROJ. by 최준혁</p>
      </div>
    </footer>
    {% bootstrap_javascript %}
  </body>

</html>
```



<aside> ❗ 위 과정 완료 후 [로컬/드라이버] template/navbar → [원격/드라이버] template/navbar, Commit & Push 수행 [원격/드라이버] template/navbar → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] template/navbar 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/create 브랜치에서 다음 토픽 진행

</aside>

------

### 9. 리뷰 생성

branch reviews/create

**앱 App**

앱 이름 : reviews

모델 Model

모델 이름 : Review

- 모델 필드

  | 이름       | 역할          | 필드     | 속성              |
  | ---------- | ------------- | -------- | ----------------- |
  | title      | 리뷰 제목     |          |                   |
  | content    | 리뷰 내용     |          |                   |
  | movie_name | 영화 이름     |          |                   |
  | grade      | 영화 평점     |          |                   |
  | created_at | 리뷰 생성시간 | DateTime | auto_now_add=True |
  | updated_at | 리뷰 수정시간 | DateTime | auto_now = True   |

#### models.py

``` python
class Review(models.Model):
    title = models.CharField(max_length=30) # 리뷰 제목
    content = models.TextField(null=False) # 리뷰 내용
    movie_name = models.CharField(max_length=30) # 영화 이름
    grade = models.DecimalField(max_digits=2, decimal_places=1) # 영화 평점
    created_at = models.DateTimeField(auto_now_add=True) # 리뷰 생성시간
    updated_at = models.DateTimeField(auto_now=True) # 리뷰 수정시간
```

<br>

#### terminal

``` terminal
> python manage.py makemigrations
> python manage.py migrate
```

<br>

#### forms.py

``` python
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # 제목, 내용, 이름, 평점을 사용자에게 입력받음 + 유효성 검사
        fields = ['title', 'content', 'movie_name', 'grade']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control', 'style': 'height: 100px;'}),
            'movie_name' : forms.TextInput(attrs={'class':'form-control'}),
            'grade' : forms.TextInput(attrs={'class':'form-control'}),
        }
```

<br>

**기능 View**

데이터 생성

- `POST` http://127.0.0.1:8000/reviews/create/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
]
```

<br>

#### views.py

``` python
from .forms import ReviewForm


def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie:community')
    else:        
        review_form = ReviewForm()
    context = {
        'review_form': review_form
    }
    return render(request, 'movie/create.html', context=context)
```

<br>

#### appfolder > create.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <div class="container mt-3">
    <h1>글쓰기</h1>
    <form action="" method="POST">
      {% csrf_token %}
      {{ review_form.as_p }}
      <button type="submit" class="btn btn-outline-primary">추가</button>
    </form>
  </div>
{% endblock %}
```

**화면 Template**

**리뷰 작성 페이지**

- `GET` http://127.0.0.1:8000/reviews/create/
- 리뷰 작성 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/create → [원격/드라이버] reviews/create, Commit & Push 수행 [원격/드라이버] reviews/create → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/create 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/index 브랜치에서 다음 토픽 진행

</aside>

------

### 10. 리뷰 목록 조회

branch reviews/index

**기능 View**

데이터 목록 조회

- `POST` http://127.0.0.1:8000/reviews/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
]
```

<br>

#### views.py

``` python
from .models import Review

def community(request):
    reviews = Review.objects.order_by('-pk')
    context = {
        'reviews': reviews
    }
    return render(request, 'movie/community.html', context)
```

<br>

#### app folder > community.html

``` python
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
  <style>
    a {
      text-decoration: none;
      color: inherit;
    }
  </style>
{% endblock %}

{% block body %}
  <!-- 게시판 영역 -->
  <section class="mx-5">
    <!-- 게시판 제목 -->
    <div class="text-center my-5 mx-5">
      <a href="{% url 'movie:community' %}">
        <h1>Community</h1>
      </a>
    </div>
    <!-- 게시판 내용 -->
    <div class="row">
      <!-- 테이블 헤더 -->
      <div class="col-lg-3 col-md-12 px-5 mb-3">
        <ul class="list-group">
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Boxoffice</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Movies</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Genres</a>
          </li>
          <li class="list-group-item">
            <a class="text-decoration-none" href="#">Actors</a>
          </li>
        </ul>
      </div>
      <div class="col-lg-9 col-md-12 px-5 mb-3">
        <!-- 테이블 영역 -->
        <table class="table">
          <!-- 테이블 헤드 -->
          <thead class="table-light">
            <tr>
              <th scope="col">순번</th>
              <th scope="col">리뷰 제목</th>
              <th scope="col">영화 이름</th>
            </tr>
          </thead>
          <!-- 테이블 바디 -->
          <tbody class="table-group-divider">
            {% for review in reviews %}
              <tr>
                <th>{{ review.pk }}</th>
                <th>
                  {% comment %} <a href="{% url 'movie:review_detail' review.pk %}">{{ review.title }}</a> {% endcomment %}
                </th>
                <th>{{ review.movie_name }}</th>
              </tr>
            {% endfor %}
          </tbody>
        </table>
        <div class="col-12">
          <a href="{% url 'movie:create' %}">
            <button class="btn btn-outline-primary">리뷰작성</button>
          </a>
        </div>
      </div>
    </div>
  </section>
  <nav class="mt-2 mb-2" aria-label="Page navigation example">
    <ul class="pagination justify-content-center">
      <li class="page-item">
        <a class="page-link" href="#">Previous</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">1</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">2</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">3</a>
      </li>
      <li class="page-item">
        <a class="page-link" href="#">Next</a>
      </li>
    </ul>
  </nav>
{% endblock %}
```

<br>

**화면 Template**

리뷰 **목록 페이지**

- `GET` http://127.0.0.1:8000/reviews/
- 리뷰 목록 출력
- 제목을 클릭하면 해당 리뷰의 정보 페이지로 이동

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/index → [원격/드라이버] reviews/index, Commit & Push 수행 [원격/드라이버] reviews/index → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/index 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/detail 브랜치에서 다음 토픽 진행

</aside>

------

### 11. 리뷰 정보 조회

branch reviews/detail

**기능 View**

데이터 정보 조회

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),
]
```

<br>

#### views.py

``` python

def review_detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review': review
    }
    return render(request, 'movie/review_detail.html', context)
```

<br>

#### app folder > review_detail.html

``` python
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <form class="container mt-3">
    <h1>{{ review.title }}</h1>
    <span>작성시간 :
      {{ review.created_at }}
      | 수정시간 :
      {{ review.updated_at }}</span>
    <div class="mb-3 mt-3">
      <label for="reviewContent" class="form-label">내용</label>
      <textarea name='content' class="form-control" id="reviewContent" rows="3" disabled="disabled" readonly="readonly">{{ review.content }}</textarea>
    </div>
    <div class="mb-3">
      <label for="moviename" class="form-label">영화 제목</label>
      <textarea name='content' class="form-control" id="moviename" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>
    <div class="mb-3">
      <label for="reviewgrade" class="form-label">평점</label>
      <textarea name='content' class="form-control" id="reviewgrade" rows="3" disabled="disabled" readonly="readonly">{{ review.movie_name }}</textarea>
    </div>

    <div class="row">
      <div class="col">
        {% comment %} < href="{% url 'movie:review_update' review.pk %}"> {% endcomment %}
          <button type="button" class="btn btn-outline-primary">리뷰 수정</button>
        

        {% comment %} < href="{% url 'movie:review_delete' review.pk %}"> {% endcomment %}
          <button type="button" class="btn btn-outline-danger">리뷰 삭제</button>

      </div>
    </div>
  </form>
{% endblock %}

```



**화면 Template**

**리뷰 정보 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/
- 해당 리뷰 정보 출력
- 수정 / 삭제 버튼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/detail → [원격/드라이버] reviews/detail, Commit & Push 수행 [원격/드라이버] reviews/detail → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/detail 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/update 브랜치에서 다음 토픽 진행

</aside>

------

### 12. 리뷰 정보 수정

branch reviews/update

**기능 View**

데이터 수정

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('review_udate/<int:pk>', views.review_update, name='review_update'),
]
```

<br>

#### views.py

``` python
def review_update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review_form.save()
            return redirect('movie:review_detail', review.pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        'review_form': review_form
    }
    return render(request, 'movie/review_update.html', context)
```

<br>

#### app folder > review_update.html

``` html
{% extends 'base.html' %}
{% load static %}
{% load django_bootstrap5 %}

{% block css %}
  <link rel="stylesheet" href="{% static 'css/style.css' %}">
{% endblock %}

{% block body %}
  <div class="container mt-3">
    <h1>수정하기</h1>
    <form action="" method="POST">
      {% csrf_token %}
      {{ review_form.as_p }}
      <button type="submit" class="btn btn-outline-primary">수정</button>
    </form>
  </div>
{% endblock %}
```

<br>

**화면 Template**

**리뷰 수정 페이지**

- `GET` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/update/
- 리뷰 수정 폼

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/update → [원격/드라이버] reviews/update, Commit & Push 수행 [원격/드라이버] reviews/update → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/update 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경 [로컬/새 드라이버] reviews/delete 브랜치에서 다음 토픽 진행

</aside>

------

### 13. 리뷰 삭제

branch reviews/delete

**기능 View**

데이터 삭제

- `POST` http://127.0.0.1:8000/reviews/[int:review_pk](int:review_pk)/delete/

#### app folder > urls.py

``` python
from django.urls import path 
from . import views

app_name = "movie"

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('accounts/', views.accounts, name='accounts'),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('update/', views.update, name='update'),
    path('logout/', views.logout, name='logout'),
    path('create/', views.create, name='create'),
    path('community/', views.community, name='community'),
    path('review_detail/<int:pk>/', views.review_detail, name='review_detail'),
    path('review_update/<int:pk>', views.review_update, name='review_update'),
    path('review_delete/<int:pk>', views.review_delete, name='review_delete'),
]
```

<br>

#### views.py

``` python
def review_delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect('movie:community')
```

<br>

<aside> ❗ 위 과정 완료 후 [로컬/드라이버] reviews/delete → [원격/드라이버] reviews/delete, Commit & Push 수행 [원격/드라이버] reviews/delete → [원격/드라이버] main, PR 생성 & Merge 수행 [원격/드라이버] reviews/delete 브랜치 삭제 [원격/전체] main → [로컬/전체] main, Pull 수행 드라이버 변경

</aside>

------

이후 팀원 간 논의하여 적절한 브랜치 이름을 정하여 개발합니다.