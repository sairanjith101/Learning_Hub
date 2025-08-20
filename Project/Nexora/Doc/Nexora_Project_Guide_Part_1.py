
# Part 1 — Setup + Accounts (JWT)

## 1) Create project & env


# Windows PowerShell
# python -m venv .venv
# .venv\Scripts\Activate.ps1

# macOS/Linux
# python3 -m venv .venv
# source .venv/bin/activate

# pip install Django djangorestframework djangorestframework-simplejwt PyMySQL
# pip freeze > requirements.txt

# django-admin startproject nexora .
# python manage.py startapp accounts

## 2) Create MySQL DB (example)

# CREATE DATABASE nexora CHARACTER SET utf8mb4;
# CREATE USER 'nexora_user'@'%' IDENTIFIED BY 'StrongPassword123!';
# GRANT ALL PRIVILEGES ON nexora.* TO 'nexora_user'@'%';
# FLUSH PRIVILEGES;


## 3) `nexora/__init__.py` (enable PyMySQL)

# nexora/__init__.py
import pymysql
pymysql.install_as_MySQLdb()

## 4) `nexora/settings.py`

# Replace the file with this minimal, production-ready base:

from pathlib import Path
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'change-this-in-production'
DEBUG = True
ALLOWED_HOSTS = ['*']  # tighten in prod

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party
    'rest_framework',

    # local apps
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nexora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'nexora.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nexora',
        'USER': 'nexora_user',
        'PASSWORD': 'StrongPassword123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model (roles)
AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


## 5) `nexora/urls.py`


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('accounts.urls')),  # accounts routes live here
]


## 6) `accounts/models.py` (Custom User with roles)


from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SELLER = 'SELLER', 'Seller'
        CUSTOMER = 'CUSTOMER', 'Customer'

    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


## 7) `accounts/admin.py`


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone', 'address')}),
        ('Roles', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')


## 8) `accounts/serializers.py`


from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.ChoiceField(choices=User.Roles.choices, default=User.Roles.CUSTOMER)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'phone', 'address', 'role')

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'phone', 'address', 'role')
        read_only_fields = ('id', 'username', 'role', 'email')


## 9) `accounts/views.py`


from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from rest_framework.response import Response

from .serializers import RegisterSerializer, ProfileSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

class MeView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


## 10) `accounts/urls.py`


from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, MeView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
]


## 11) Migrate & create superuser


# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser  # create an admin for /admin
# python manage.py runserver



## 12) Quick Postman tests

# 1. **Register**


# POST http://127.0.0.1:8000/api/auth/register/
# Content-Type: application/json

{
  "username": "ranjith",
  "email": "sairanjith101@gmail.com",
  "password": "Prime@2001Strong",
  "first_name": "Ranjith",
  "last_name": "Kumar",
  "phone": "8220410326",
  "address": "Bengaluru",
  "role": "CUSTOMER"
}


# 2. **Login (JWT)**


# POST http://127.0.0.1:8000/api/auth/login/
# Content-Type: application/json

{
  "username": "ranjith",
  "password": "Prime@2001Strong"
}


# Response will include:


{ "refresh": "...", "access": "..." }


# 3. **My Profile (get/update)**


# GET http://127.0.0.1:8000/api/auth/me/
# Authorization: Bearer <access_token>



# PUT http://127.0.0.1:8000/api/auth/me/
# Authorization: Bearer <access_token>
# Content-Type: application/json

{
  "first_name": "Ranjith",
  "last_name": "Kumar",
  "phone": "9999999999",
  "address": "Bengaluru - Updated"
}




## What you have now

# * Custom **User** model with **roles** (Admin/Seller/Customer).
# * **JWT auth** (login/refresh).
# * **Register** + **My Profile** (secure).
# * **MySQL** wired up using **PyMySQL** (no native compiler headaches).



