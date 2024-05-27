"""
Django settings for seminar_project project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from pathlib import Path
import os
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#o!c011lbqk405tr)p%)i*yn7nr4#w-a2br@p9%fpmibyt_&^('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] #배포를 위해 추가


# Application definition

INSTALLED_APPS = [
    'member',
    'util',
    'users', # 추가
    'lionapp',
    'corsheaders',
    'drf_yasg', # 추가
    'rest_framework',
    'rest_framework_simplejwt', # 추가
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 최상단에 위치할 것
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # 인증된 요청인지 확인
        #'rest_framework.permissions.AllowAny',  # 누구나 접근 가능 
				# (기본적으로 누구나 접근 가능하게 설정하고, 인증된 요청인지 확인하는 api를 따로 지정하게 하려면 
				# 이 옵션을 위의 옵션 대신 켜주어도 됩니다!)
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT를 통한 인증방식 사용
    ),
}
# Django REST framework 설정으로, API의 권한 및 인증 방식을 설정합니다.

REST_USE_JWT = True
# JWT를 기본 인증 방식으로 사용하도록 설정

from datetime import timedelta

SIMPLE_JWT = {
    'SIGNING_KEY': 'hellolikelionhellolikelion', 
		# JWT에서 가장 중요한 인증키입니다! 
		# 이 키가 알려지게 되면 JWT의 인증체계가 다 털릴 수 있으니 노출되지 않게 조심해야합니다!
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
		# access token의 유효시간을 설정합니다.
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
		# refresh token의 유효시간을 설정합니다.
    'ROTATE_REFRESH_TOKENS': False,
		# True로 설정하면 리프레시 토큰이 사용될 때마다 새로운 리프레시 토큰이 발급됩니다.
    'BLACKLIST_AFTER_ROTATION': True,
		# 리프레시 토큰 회전 후, 이전의 리프레시 토큰이 블랙리스트에 추가될지 여부를 나타내는 부울 값입니다. 
		# True로 설정하면 리프레시 토큰이 회전되면서, 이전의 리프레시 토큰은 블랙리스트에 추가되어 더 이상 사용할 수 없게 됩니다.
}
# JWT 설정으로, JSON Web Token의 특정 속성을 설정합니다.

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'BearerAuth': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': "JWT Token"
        }
    },
    'SECURITY_REQUIREMENTS': [{
        'BearerAuth': []
    }]
}

CORS_ALLOW_METHODS = [  # 허용할 옵션
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [  # 허용할 헤더
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

CORS_ALLOW_CREDENTIALS = True

# 2) 모든 출처 지정
CORS_ALLOW_ALL_ORIGINS: True



ROOT_URLCONF = 'seminar_project.urls'
# 프로젝트의 최상위 URL 설정 파일을 지정합니다. 
# (따라서 url은 seminar_project의 urls.py 파일을 항상 먼저 보는 것입니다!)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'seminar_project', 'templates')], # 템플릿 경로 추가하기
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# admin 페이지를 구성할 때 필요합니다!


WSGI_APPLICATION = 'seminar_project.wsgi.application'
# 프로젝트의 WSGI 애플리케이션을 지정합니다. (이것도 배포세션에서 더 배울 예정입니다!)

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
# 데이터베이스 연결 설정으로, 현재는 SQLite를 사용하고 있습니다.

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },# 사용자의 아이디와 유사한 비밀번호를 허용하지 않음
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },# 비밀번호가 설정된 길이 보다 짧지 않도록 검사
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },# 널리 사용되는 암호 목록과 일치하는 비밀번호를 거부합니다. 널리 사용되는 암호를 피하고 보안을 강화합니다. (이거 찾아보면 금지해놓은 재밌는 암호들이 많았던 것으로 기억합니다...ㅋㅋ)
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }, # 비밀번호에 숫자가 포함되어 있는지 확인하여, 숫자를 사용하도록 유도합니다.
]
# 비밀번호 유효성 검사기 설정으로, 사용자 비밀번호의 강도를 제어합니다.

AUTH_USER_MODEL = 'users.User' # 커스텀 유저를 장고에서 사용하기 위함

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr' # 언어 설정입니다.

TIME_ZONE = 'Asia/Seoul' # 시간대 설정입니다.


USE_L10N = True

USE_TZ = True
# 국제화 및 시간대 사용 여부를 설정합니다. 웬만하면 그대로 두시는 것을 추천합니다!

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = 'static/'
# 정적 파일(사진 같은..)의 URL을 설정합니다.

STATIC_ROOT = os.path.join(BASE_DIR,'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# 기본 자동 생성 필드를 생성합니다.