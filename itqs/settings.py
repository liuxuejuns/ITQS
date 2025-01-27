"""
Django settings for itqs project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'umwv&naa(vasyo9@(sfg&t5$ro52-9^=zo0^n!47$&gyk_-sx$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    #'database.apps.DatabaseConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'database',
    'website',
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

ROOT_URLCONF = 'itqs.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'itqs.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'itqs',
        'USER': 'postgres',
        'PASSWORD': '1234qwer!@#$QWER',
        'HOST': 'postgres',  # 服务器上
        'PORT': '5432',
        # 'HOST': '10.41.95.85',  # windows本地
        # 'PORT': '8101',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

ATQS_MEDIA_BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ATQS_MEDIA_BASE_DIR, 'media')

# log to file
LOG_BASE_DIR = os.path.join(BASE_DIR.parent.parent, 'logs/django')
if not os.path.exists(LOG_BASE_DIR):
    os.makedirs(LOG_BASE_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d]  \
                        [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',  # 要打印系统运行信息是设为'DEBUG'
            'filename': os.path.join(LOG_BASE_DIR, 'logging.log'),  # log file name
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 50,  # 日誌文件大小
            'backupCount': 5,
            'formatter': 'simple',
        },
        'error': {
            'level': 'ERROR',
            'filename': os.path.join(LOG_BASE_DIR, 'error.log'),  # log file name
            'class': 'logging.FileHandler',  # FileHandler: 處理類 輸出到磁盤文件
            'formatter': 'standard',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',  # 使用哪種 formatters 日誌格式
        },
        # 专门定义一个收集特定信息的日志(暂时没用)
        'collect': {
            'level': 'INFO',
            'class': 'logging.FileHandler',  # FileHandler: 處理類 輸出到磁盤文件
            'filename': os.path.join(LOG_BASE_DIR, 'collect.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': False,  # propagate 向不向更高級別的 loggers 傳遞
        },
        'collect': {  # (暂时没用)
            'handlers': ['collect', 'console'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
