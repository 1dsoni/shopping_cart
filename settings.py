from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'django-insecure-71gxu*i=we0#9m2t1!bi2w!kzh%cy+0bb!d13^xo(z!*9ha5@v'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "user.apps.UserConfig",
    "web_auth.apps.WebAuthConfig",
    "product.apps.ProductConfig",
    "inventory.apps.InventoryConfig",
    "cart.apps.CartConfig",
]

MIDDLEWARE = [
]

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "web_auth.auth_backend.JwtAuthBackend",
    ),
    "UNAUTHENTICATED_USER": "user.models.User",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,  # the size of one page
}
