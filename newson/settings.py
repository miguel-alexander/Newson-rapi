"""
Django settings for newson project.

Generated by 'django-admin startproject' using Django 3.2.11.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
from datetime import timedelta
from selenium import webdriver


load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG")

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split()

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "accounts.apps.AccountsConfig",
    "main.apps.MainConfig",
    "corsheaders",
    "rest_framework",
    "rest_framework_simplejwt",
    "django_filters",
    "base",
    "multiselectfield",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "newson.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "newson.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if os.getenv("USING_DB").lower() == "sql":

    # SQLITE DB
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("SQL_ENGINE"),
            'NAME': str(os.path.join(BASE_DIR, os.getenv("SQL_DATABASE"))),
        }
    }
else:

    # POSTGRESQL DB
    DATABASES = {
        'default': {
            'ENGINE': os.getenv("PSQL_ENGINE"),
            'NAME': os.getenv("PSQL_DATABASE"),
            'USER': os.getenv("PSQL_USER"),
            'PASSWORD': os.getenv("PSQL_PASSWORD"),
            'HOST': os.getenv("PSQL_HOST"),
            'PORT': os.getenv("PSQL_PORT"),
        }
    }


# DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/api/static/"
MEDIA_URL = "/api/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "mediafiles")
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
COOKIES_FOLDER = "cookies"
COOKIES_ROOT = os.path.join(MEDIA_ROOT, COOKIES_FOLDER)

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

CORS_ALLOW_ALL_ORIGINS = True

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(minutes=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

BROKER_URL = os.getenv("BROKER_URL", "redis://localhost:6379")
CELERY_RESULT_BACKEND = os.getenv(
    "CELERY_RESULT_BACKEND", "redis://localhost:6379")
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = os.getenv("CELERY_TIMEZONE")

### CUSTOM CONFIG ###
TIMEOUT = 10
DAILY_PAGES_TO_CRAWL = 10
TOTAL_CONNECTION_REQUESTS_PER_DAY = 45
TOTAL_ACTION_WITH_PROSPECTS_PER_DAY = 45
FULLY_CRAWL_PERFORM_ACTION_LIMIT = 5
TOTAL_RETRIES = 3

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000

GOOGLE_OAUTH2_CLIENT_ID = os.getenv("GOOGLE_OAUTH2_CLIENT_ID")
GOOGLE_OAUTH2_CLIENT_SECRET = os.getenv("GOOGLE_OAUTH2_CLIENT_SECRET")


PROXY_USERNAME = os.getenv("PROXY_USERNAME")
PROXY_PASSWORD = os.getenv("PROXY_PASSWORD")


PROXY_CURL_API_KEY = os.getenv("PROXY_CURL_API_KEY")

FE_HOST = os.getenv("FE_HOST")
APP_SUMO_BACKEND_HOST = os.getenv("APP_SUMO_BACKEND_HOST")
BACKEND_HOST = os.getenv("BACKEND_HOST")
ZALENIUM_HOST = os.getenv("ZALENIUM_HOST", None)
KAMELEO_HOST = os.getenv("KAMELEO_HOST", "http://localhost:5050")


DRIVER_OPTIONS = webdriver.ChromeOptions()
DRIVER_OPTIONS.add_argument('--disable-extensions')
DRIVER_OPTIONS.add_argument("--disable-plugins-discovery")
DRIVER_OPTIONS.add_argument("--start-maximized")
DRIVER_OPTIONS.add_argument("--log-level=3")
DRIVER_OPTIONS.add_argument('--headless')
DRIVER_OPTIONS.add_argument('--ignore-certificate-errors-spki-list')
DRIVER_OPTIONS.add_argument('--ignore-ssl-errors')
DRIVER_OPTIONS.add_argument('--no-sandbox')
DRIVER_OPTIONS.add_argument('--disable-dev-shm-usage')
DRIVER_OPTIONS.add_argument("--window-size=1325x744")
# DRIVER_OPTIONS.add_argument('--blink-settings=imagesEnabled=false')
DRIVER_OPTIONS.add_experimental_option("excludeSwitches", ["ignore-certificate-errors", "safebrowsing-disable-download-protection", "safebrowsing-disable-auto-update", "disable-client-side-phishing-detection", "enable-automation"])
DRIVER_OPTIONS.add_experimental_option('useAutomationExtension', False)


ALL_TIMEZONES = (
    ('America/El_Salvador', 'America/El_Salvador'),
    ('Australia/Darwin', 'Australia/Darwin'),
    ('Japan', 'Japan'),
    ('Africa/Gaborone', 'Africa/Gaborone'),
    ('America/Montreal', 'America/Montreal'),
    ('NZ', 'NZ'),
    ('Africa/Nouakchott', 'Africa/Nouakchott'),
    ('Portugal', 'Portugal'),
    ('America/Anguilla', 'America/Anguilla'),
    ('ROC', 'ROC'),
    ('Europe/Ljubljana', 'Europe/Ljubljana'),
    ('Europe/Vienna', 'Europe/Vienna'),
    ('Africa/Abidjan', 'Africa/Abidjan'),
    ('Africa/Asmera', 'Africa/Asmera'),
    ('Antarctica/Macquarie', 'Antarctica/Macquarie'),
    ('Europe/Gibraltar', 'Europe/Gibraltar'),
    ('Asia/Vladivostok', 'Asia/Vladivostok'),
    ('US/Michigan', 'US/Michigan'),
    ('America/Guadeloupe', 'America/Guadeloupe'),
    ('CET', 'CET'),
    ('Africa/Libreville', 'Africa/Libreville'),
    ('America/St_Barthelemy', 'America/St_Barthelemy'),
    ('Australia/Brisbane', 'Australia/Brisbane'),
    ('America/Argentina/Salta', 'America/Argentina/Salta'),
    ('America/North_Dakota/New_Salem', 'America/North_Dakota/New_Salem'),
    ('Europe/Luxembourg', 'Europe/Luxembourg'),
    ('America/Santarem', 'America/Santarem'),
    ('Etc/Zulu', 'Etc/Zulu'),
    ('America/Regina', 'America/Regina'),
    ('Asia/Aqtau', 'Asia/Aqtau'),
    ('Africa/Accra', 'Africa/Accra'),
    ('Africa/Freetown', 'Africa/Freetown'),
    ('America/Belem', 'America/Belem'),
    ('Australia/LHI', 'Australia/LHI'),
    ('Pacific/Majuro', 'Pacific/Majuro'),
    ('Jamaica', 'Jamaica'),
    ('Africa/Windhoek', 'Africa/Windhoek'),
    ('Africa/Khartoum', 'Africa/Khartoum'),
    ('Asia/Yerevan', 'Asia/Yerevan'),
    ('Pacific/Saipan', 'Pacific/Saipan'),
    ('GMT-0', 'GMT-0'),
    ('Pacific/Honolulu', 'Pacific/Honolulu'),
    ('America/Swift_Current', 'America/Swift_Current'),
    ('Atlantic/St_Helena', 'Atlantic/St_Helena'),
    ('Chile/Continental', 'Chile/Continental'),
    ('Africa/Lome', 'Africa/Lome'),
    ('Pacific/Wake', 'Pacific/Wake'),
    ('Pacific/Truk', 'Pacific/Truk'),
    ('Atlantic/Faroe', 'Atlantic/Faroe'),
    ('Etc/GMT+5', 'Etc/GMT+5'),
    ('Pacific/Midway', 'Pacific/Midway'),
    ('Africa/Maputo', 'Africa/Maputo'),
    ('MST7MDT', 'MST7MDT'),
    ('America/Porto_Acre', 'America/Porto_Acre'),
    ('EST5EDT', 'EST5EDT'),
    ('Europe/Tiraspol', 'Europe/Tiraspol'),
    ('Europe/Uzhgorod', 'Europe/Uzhgorod'),
    ('Asia/Ulan_Bator', 'Asia/Ulan_Bator'),
    ('Europe/Oslo', 'Europe/Oslo'),
    ('America/Los_Angeles', 'America/Los_Angeles'),
    ('EST', 'EST'),
    ('Asia/Ashkhabad', 'Asia/Ashkhabad'),
    ('Australia/ACT', 'Australia/ACT'),
    ('Africa/Bamako', 'Africa/Bamako'),
    ('Indian/Comoro', 'Indian/Comoro'),
    ('America/Santo_Domingo', 'America/Santo_Domingo'),
    ('America/Chihuahua', 'America/Chihuahua'),
    ('Egypt', 'Egypt'),
    ('Europe/Isle_of_Man', 'Europe/Isle_of_Man'),
    ('Asia/Bangkok', 'Asia/Bangkok'),
    ('Asia/Aden', 'Asia/Aden'),
    ('Antarctica/Mawson', 'Antarctica/Mawson'),
    ('America/Indiana/Tell_City', 'America/Indiana/Tell_City'),
    ('Etc/GMT-5', 'Etc/GMT-5'),
    ('America/Scoresbysund', 'America/Scoresbysund'),
    ('Europe/Sofia', 'Europe/Sofia'),
    ('Australia/Adelaide', 'Australia/Adelaide'),
    ('America/Yakutat', 'America/Yakutat'),
    ('WET', 'WET'),
    ('GMT', 'GMT'),
    ('America/Sitka', 'America/Sitka'),
    ('Etc/GMT-11', 'Etc/GMT-11'),
    ('America/Hermosillo', 'America/Hermosillo'),
    ('Asia/Thimphu', 'Asia/Thimphu'),
    ('America/Cordoba', 'America/Cordoba'),
    ('America/St_Lucia', 'America/St_Lucia'),
    ('Asia/Irkutsk', 'Asia/Irkutsk'),
    ('Atlantic/Faeroe', 'Atlantic/Faeroe'),
    ('America/Knox_IN', 'America/Knox_IN'),
    ('Indian/Antananarivo', 'Indian/Antananarivo'),
    ('Asia/Kuala_Lumpur', 'Asia/Kuala_Lumpur'),
    ('Australia/Lindeman', 'Australia/Lindeman'),
    ('America/Guatemala', 'America/Guatemala'),
    ('Cuba', 'Cuba'),
    ('Europe/Vaduz', 'Europe/Vaduz'),
    ('America/Lower_Princes', 'America/Lower_Princes'),
    ('Europe/Vatican', 'Europe/Vatican'),
    ('MET', 'MET'),
    ('Etc/GMT+9', 'Etc/GMT+9'),
    ('Europe/Prague', 'Europe/Prague'),
    ('Asia/Barnaul', 'Asia/Barnaul'),
    ('GMT0', 'GMT0'),
    ('Pacific/Wallis', 'Pacific/Wallis'),
    ('Pacific/Chuuk', 'Pacific/Chuuk'),
    ('America/Belize', 'America/Belize'),
    ('America/St_Kitts', 'America/St_Kitts'),
    ('Antarctica/McMurdo', 'Antarctica/McMurdo'),
    ('America/Tegucigalpa', 'America/Tegucigalpa'),
    ('America/Santa_Isabel', 'America/Santa_Isabel'),
    ('America/North_Dakota/Beulah', 'America/North_Dakota/Beulah'),
    ('Africa/Niamey', 'Africa/Niamey'),
    ('America/Bahia_Banderas', 'America/Bahia_Banderas'),
    ('Asia/Tbilisi', 'Asia/Tbilisi'),
    ('Pacific/Galapagos', 'Pacific/Galapagos'),
    ('Asia/Taipei', 'Asia/Taipei'),
    ('Zulu', 'Zulu'),
    ('America/Indiana/Petersburg', 'America/Indiana/Petersburg'),
    ('Antarctica/South_Pole', 'Antarctica/South_Pole'),
    ('Etc/GMT+1', 'Etc/GMT+1'),
    ('America/Kentucky/Louisville', 'America/Kentucky/Louisville'),
    ('PRC', 'PRC'),
    ('Australia/Yancowinna', 'Australia/Yancowinna'),
    ('MST', 'MST'),
    ('Etc/GMT-6', 'Etc/GMT-6'),
    ('Africa/Conakry', 'Africa/Conakry'),
    ('America/Sao_Paulo', 'America/Sao_Paulo'),
    ('America/Indiana/Vevay', 'America/Indiana/Vevay'),
    ('Africa/Lagos', 'Africa/Lagos'),
    ('America/Detroit', 'America/Detroit'),
    ('Asia/Novokuznetsk', 'Asia/Novokuznetsk'),
    ('Etc/GMT-1', 'Etc/GMT-1'),
    ('America/Indiana/Winamac', 'America/Indiana/Winamac'),
    ('Pacific/Kwajalein', 'Pacific/Kwajalein'),
    ('Asia/Kathmandu', 'Asia/Kathmandu'),
    ('Pacific/Samoa', 'Pacific/Samoa'),
    ('Africa/Harare', 'Africa/Harare'),
    ('America/Whitehorse', 'America/Whitehorse'),
    ('America/Glace_Bay', 'America/Glace_Bay'),
    ('America/Asuncion', 'America/Asuncion'),
    ('Europe/Jersey', 'Europe/Jersey'),
    ('America/Halifax', 'America/Halifax'),
    ('America/Cuiaba', 'America/Cuiaba'),
    ('Asia/Makassar', 'Asia/Makassar'),
    ('Etc/UTC', 'Etc/UTC'),
    ('Brazil/East', 'Brazil/East'),
    ('US/Samoa', 'US/Samoa'),
    ('America/Boise', 'America/Boise'),
    ('Asia/Khandyga', 'Asia/Khandyga'),
    ('Australia/Queensland', 'Australia/Queensland'),
    ('Etc/GMT+2', 'Etc/GMT+2'),
    ('Europe/Dublin', 'Europe/Dublin'),
    ('America/Fort_Nelson', 'America/Fort_Nelson'),
    ('Etc/GMT+4', 'Etc/GMT+4'),
    ('Indian/Kerguelen', 'Indian/Kerguelen'),
    ('Etc/GMT+0', 'Etc/GMT+0'),
    ('Asia/Ust-Nera', 'Asia/Ust-Nera'),
    ('Etc/GMT-9', 'Etc/GMT-9'),
    ('Australia/West', 'Australia/West'),
    ('America/Blanc-Sablon', 'America/Blanc-Sablon'),
    ('America/Atka', 'America/Atka'),
    ('Atlantic/Canary', 'Atlantic/Canary'),
    ('Iran', 'Iran'),
    ('Africa/Dakar', 'Africa/Dakar'),
    ('America/Nipigon', 'America/Nipigon'),
    ('CST6CDT', 'CST6CDT'),
    ('Etc/GMT+11', 'Etc/GMT+11'),
    ('Asia/Amman', 'Asia/Amman'),
    ('Australia/Perth', 'Australia/Perth'),
    ('America/Mazatlan', 'America/Mazatlan'),
    ('Asia/Qostanay', 'Asia/Qostanay'),
    ('America/Metlakatla', 'America/Metlakatla'),
    ('US/Mountain', 'US/Mountain'),
    ('America/Thule', 'America/Thule'),
    ('America/Atikokan', 'America/Atikokan'),
    ('Asia/Atyrau', 'Asia/Atyrau'),
    ('Asia/Yangon', 'Asia/Yangon'),
    ('Europe/Saratov', 'Europe/Saratov'),
    ('Europe/Kaliningrad', 'Europe/Kaliningrad'),
    ('Etc/GMT+3', 'Etc/GMT+3'),
    ('Eire', 'Eire'),
    ('Africa/Johannesburg', 'Africa/Johannesburg'),
    ('Asia/Tashkent', 'Asia/Tashkent'),
    ('Africa/Lusaka', 'Africa/Lusaka'),
    ('America/Nassau', 'America/Nassau'),
    ('Asia/Kuwait', 'Asia/Kuwait'),
    ('Pacific/Rarotonga', 'Pacific/Rarotonga'),
    ('Pacific/Kosrae', 'Pacific/Kosrae'),
    ('Asia/Tel_Aviv', 'Asia/Tel_Aviv'),
    ('Europe/Ulyanovsk', 'Europe/Ulyanovsk'),
    ('Poland', 'Poland'),
    ('Asia/Qyzylorda', 'Asia/Qyzylorda'),
    ('Asia/Damascus', 'Asia/Damascus'),
    ('Pacific/Palau', 'Pacific/Palau'),
    ('America/Creston', 'America/Creston'),
    ('Australia/Lord_Howe', 'Australia/Lord_Howe'),
    ('Asia/Pyongyang', 'Asia/Pyongyang'),
    ('America/Jamaica', 'America/Jamaica'),
    ('Europe/Kiev', 'Europe/Kiev'),
    ('Antarctica/Rothera', 'Antarctica/Rothera'),
    ('UTC', 'UTC'),
    ('Atlantic/Azores', 'Atlantic/Azores'),
    ('Asia/Sakhalin', 'Asia/Sakhalin'),
    ('America/Inuvik', 'America/Inuvik'),
    ('America/Monterrey', 'America/Monterrey'),
    ('Asia/Urumqi', 'Asia/Urumqi'),
    ('America/Argentina/Catamarca', 'America/Argentina/Catamarca'),
    ('America/Dominica', 'America/Dominica'),
    ('ROK', 'ROK'),
    ('US/Indiana-Starke', 'US/Indiana-Starke'),
    ('Pacific/Tahiti', 'Pacific/Tahiti'),
    ('America/Araguaina', 'America/Araguaina'),
    ('Africa/Bangui', 'Africa/Bangui'),
    ('America/St_Johns', 'America/St_Johns'),
    ('Atlantic/Bermuda', 'Atlantic/Bermuda'),
    ('Antarctica/DumontDUrville', 'Antarctica/DumontDUrville'),
    ('Asia/Nicosia', 'Asia/Nicosia'),
    ('Pacific/Port_Moresby', 'Pacific/Port_Moresby'),
    ('Asia/Baghdad', 'Asia/Baghdad'),
    ('Europe/Belgrade', 'Europe/Belgrade'),
    ('America/Menominee', 'America/Menominee'),
    ('Etc/GMT-8', 'Etc/GMT-8'),
    ('America/Eirunepe', 'America/Eirunepe'),
    ('Europe/Skopje', 'Europe/Skopje'),
    ('Africa/Mogadishu', 'Africa/Mogadishu'),
    ('Europe/Amsterdam', 'Europe/Amsterdam'),
    ('Antarctica/Troll', 'Antarctica/Troll'),
    ('Africa/Algiers', 'Africa/Algiers'),
    ('Pacific/Pago_Pago', 'Pacific/Pago_Pago'),
    ('America/Indiana/Vincennes', 'America/Indiana/Vincennes'),
    ('Africa/Luanda', 'Africa/Luanda'),
    ('Africa/Kampala', 'Africa/Kampala'),
    ('Europe/San_Marino', 'Europe/San_Marino'),
    ('America/Porto_Velho', 'America/Porto_Velho'),
    ('Navajo', 'Navajo'),
    ('America/Ojinaga', 'America/Ojinaga'),
    ('Pacific/Easter', 'Pacific/Easter'),
    ('Africa/Juba', 'Africa/Juba'),
    ('Etc/GMT+7', 'Etc/GMT+7'),
    ('America/Cambridge_Bay', 'America/Cambridge_Bay'),
    ('Europe/Bucharest', 'Europe/Bucharest'),
    ('US/East-Indiana', 'US/East-Indiana'),
    ('Pacific/Niue', 'Pacific/Niue'),
    ('Pacific/Tongatapu', 'Pacific/Tongatapu'),
    ('America/Argentina/Buenos_Aires', 'America/Argentina/Buenos_Aires'),
    ('Israel', 'Israel'),
    ('Pacific/Tarawa', 'Pacific/Tarawa'),
    ('America/Caracas', 'America/Caracas'),
    ('Asia/Bishkek', 'Asia/Bishkek'),
    ('America/Matamoros', 'America/Matamoros'),
    ('Africa/Mbabane', 'Africa/Mbabane'),
    ('America/Manaus', 'America/Manaus'),
    ('America/Aruba', 'America/Aruba'),
    ('America/La_Paz', 'America/La_Paz'),
    ('America/Indiana/Knox', 'America/Indiana/Knox'),
    ('Canada/Pacific', 'Canada/Pacific'),
    ('Africa/Porto-Novo', 'Africa/Porto-Novo'),
    ('Antarctica/Vostok', 'Antarctica/Vostok'),
    ('America/Jujuy', 'America/Jujuy'),
    ('America/Maceio', 'America/Maceio'),
    ('Asia/Srednekolymsk', 'Asia/Srednekolymsk'),
    ('America/Rio_Branco', 'America/Rio_Branco'),
    ('America/Mexico_City', 'America/Mexico_City'),
    ('Iceland', 'Iceland'),
    ('America/Argentina/Jujuy', 'America/Argentina/Jujuy'),
    ('Turkey', 'Turkey'),
    ('Atlantic/Reykjavik', 'Atlantic/Reykjavik'),
    ('Asia/Qatar', 'Asia/Qatar'),
    ('Pacific/Pohnpei', 'Pacific/Pohnpei'),
    ('Asia/Dhaka', 'Asia/Dhaka'),
    ('America/Port_of_Spain', 'America/Port_of_Spain'),
    ('Etc/GMT-2', 'Etc/GMT-2'),
    ('America/Miquelon', 'America/Miquelon'),
    ('US/Aleutian', 'US/Aleutian'),
    ('America/Marigot', 'America/Marigot'),
    ('PST8PDT', 'PST8PDT'),
    ('Asia/Kuching', 'Asia/Kuching'),
    ('Africa/Ndjamena', 'Africa/Ndjamena'),
    ('America/Antigua', 'America/Antigua'),
    ('Asia/Tehran', 'Asia/Tehran'),
    ('Pacific/Marquesas', 'Pacific/Marquesas'),
    ('Brazil/DeNoronha', 'Brazil/DeNoronha'),
    ('Canada/Mountain', 'Canada/Mountain'),
    ('America/Montevideo', 'America/Montevideo'),
    ('America/New_York', 'America/New_York'),
    ('US/Central', 'US/Central'),
    ('Asia/Chita', 'Asia/Chita'),
    ('Indian/Chagos', 'Indian/Chagos'),
    ('Asia/Istanbul', 'Asia/Istanbul'),
    ('Pacific/Auckland', 'Pacific/Auckland'),
    ('America/Bahia', 'America/Bahia'),
    ('Greenwich', 'Greenwich'),
    ('Kwajalein', 'Kwajalein'),
    ('America/Grenada', 'America/Grenada'),
    ('Mexico/General', 'Mexico/General'),
    ('America/Argentina/Tucuman', 'America/Argentina/Tucuman'),
    ('Europe/Paris', 'Europe/Paris'),
    ('Europe/Budapest', 'Europe/Budapest'),
    ('America/Boa_Vista', 'America/Boa_Vista'),
    ('Mexico/BajaSur', 'Mexico/BajaSur'),
    ('Africa/Douala', 'Africa/Douala'),
    ('Etc/GMT-14', 'Etc/GMT-14'),
    ('Africa/Dar_es_Salaam', 'Africa/Dar_es_Salaam'),
    ('America/Virgin', 'America/Virgin'),
    ('Etc/GMT+10', 'Etc/GMT+10'),
    ('Chile/EasterIsland', 'Chile/EasterIsland'),
    ('Australia/NSW', 'Australia/NSW'),
    ('Africa/Sao_Tome', 'Africa/Sao_Tome'),
    ('Africa/Tunis', 'Africa/Tunis'),
    ('Europe/Moscow', 'Europe/Moscow'),
    ('America/Rainy_River', 'America/Rainy_River'),
    ('America/Guayaquil', 'America/Guayaquil'),
    ('America/Kentucky/Monticello', 'America/Kentucky/Monticello'),
    ('America/Managua', 'America/Managua'),
    ('America/Lima', 'America/Lima'),
    ('America/Resolute', 'America/Resolute'),
    ('Africa/Timbuktu', 'Africa/Timbuktu'),
    ('Etc/GMT-12', 'Etc/GMT-12'),
    ('Asia/Yakutsk', 'Asia/Yakutsk'),
    ('Europe/Madrid', 'Europe/Madrid'),
    ('Indian/Mayotte', 'Indian/Mayotte'),
    ('Pacific/Apia', 'Pacific/Apia'),
    ('Asia/Tomsk', 'Asia/Tomsk'),
    ('America/Phoenix', 'America/Phoenix'),
    ('Africa/Bissau', 'Africa/Bissau'),
    ('America/Vancouver', 'America/Vancouver'),
    ('Asia/Ujung_Pandang', 'Asia/Ujung_Pandang'),
    ('America/Martinique', 'America/Martinique'),
    ('Asia/Kolkata', 'Asia/Kolkata'),
    ('Africa/Cairo', 'Africa/Cairo'),
    ('Indian/Reunion', 'Indian/Reunion'),
    ('America/Godthab', 'America/Godthab'),
    ('America/Juneau', 'America/Juneau'),
    ('Australia/Victoria', 'Australia/Victoria'),
    ('America/Chicago', 'America/Chicago'),
    ('Europe/Rome', 'Europe/Rome'),
    ('Asia/Jakarta', 'Asia/Jakarta'),
    ('Asia/Brunei', 'Asia/Brunei'),
    ('Pacific/Kiritimati', 'Pacific/Kiritimati'),
    ('America/Tijuana', 'America/Tijuana'),
    ('Pacific/Kanton', 'Pacific/Kanton'),
    ('America/North_Dakota/Center', 'America/North_Dakota/Center'),
    ('America/Rankin_Inlet', 'America/Rankin_Inlet'),
    ('Europe/Kirov', 'Europe/Kirov'),
    ('US/Hawaii', 'US/Hawaii'),
    ('Etc/GMT+8', 'Etc/GMT+8'),
    ('Singapore', 'Singapore'),
    ('Europe/Guernsey', 'Europe/Guernsey'),
    ('Canada/Saskatchewan', 'Canada/Saskatchewan'),
    ('America/Buenos_Aires', 'America/Buenos_Aires'),
    ('Europe/Helsinki', 'Europe/Helsinki'),
    ('Africa/Kigali', 'Africa/Kigali'),
    ('Africa/Blantyre', 'Africa/Blantyre'),
    ('Antarctica/Palmer', 'Antarctica/Palmer'),
    ('Asia/Samarkand', 'Asia/Samarkand'),
    ('Antarctica/Casey', 'Antarctica/Casey'),
    ('Europe/Istanbul', 'Europe/Istanbul'),
    ('America/Curacao', 'America/Curacao'),
    ('America/Cancun', 'America/Cancun'),
    ('America/Argentina/Cordoba', 'America/Argentina/Cordoba'),
    ('America/Rosario', 'America/Rosario'),
    ('America/Indiana/Marengo', 'America/Indiana/Marengo'),
    ('Canada/Eastern', 'Canada/Eastern'),
    ('America/Indianapolis', 'America/Indianapolis'),
    ('Asia/Chungking', 'Asia/Chungking'),
    ('US/Arizona', 'US/Arizona'),
    ('Asia/Gaza', 'Asia/Gaza'),
    ('Asia/Pontianak', 'Asia/Pontianak'),
    ('America/Argentina/Rio_Gallegos', 'America/Argentina/Rio_Gallegos'),
    ('Pacific/Yap', 'Pacific/Yap'),
    ('Canada/Central', 'Canada/Central'),
    ('Pacific/Gambier', 'Pacific/Gambier'),
    ('Asia/Hebron', 'Asia/Hebron'),
    ('Asia/Macao', 'Asia/Macao'),
    ('Asia/Magadan', 'Asia/Magadan'),
    ('Indian/Maldives', 'Indian/Maldives'),
    ('Atlantic/Stanley', 'Atlantic/Stanley'),
    ('Indian/Mahe', 'Indian/Mahe'),
    ('Pacific/Fiji', 'Pacific/Fiji'),
    ('Universal', 'Universal'),
    ('Asia/Riyadh', 'Asia/Riyadh'),
    ('Arctic/Longyearbyen', 'Arctic/Longyearbyen'),
    ('Pacific/Chatham', 'Pacific/Chatham'),
    ('America/Argentina/La_Rioja', 'America/Argentina/La_Rioja'),
    ('America/Argentina/Ushuaia', 'America/Argentina/Ushuaia'),
    ('Etc/GMT0', 'Etc/GMT0'),
    ('Asia/Shanghai', 'Asia/Shanghai'),
    ('Pacific/Guadalcanal', 'Pacific/Guadalcanal'),
    ('Pacific/Guam', 'Pacific/Guam'),
    ('W-SU', 'W-SU'),
    ('America/Fortaleza', 'America/Fortaleza'),
    ('Asia/Ho_Chi_Minh', 'Asia/Ho_Chi_Minh'),
    ('Asia/Omsk', 'Asia/Omsk'),
    ('America/Danmarkshavn', 'America/Danmarkshavn'),
    ('Africa/Maseru', 'Africa/Maseru'),
    ('Asia/Macau', 'Asia/Macau'),
    ('Pacific/Enderbury', 'Pacific/Enderbury'),
    ('Europe/Berlin', 'Europe/Berlin'),
    ('Etc/GMT-0', 'Etc/GMT-0'),
    ('Pacific/Efate', 'Pacific/Efate'),
    ('America/Denver', 'America/Denver'),
    ('Australia/Sydney', 'Australia/Sydney'),
    ('America/Costa_Rica', 'America/Costa_Rica'),
    ('Australia/Eucla', 'Australia/Eucla'),
    ('Asia/Singapore', 'Asia/Singapore'),
    ('America/Anchorage', 'America/Anchorage'),
    ('GMT+0', 'GMT+0'),
    ('America/Moncton', 'America/Moncton'),
    ('America/Ensenada', 'America/Ensenada'),
    ('Brazil/Acre', 'Brazil/Acre'),
    ('America/Recife', 'America/Recife'),
    ('Asia/Vientiane', 'Asia/Vientiane'),
    ('Europe/Samara', 'Europe/Samara'),
    ('Europe/Zurich', 'Europe/Zurich'),
    ('Africa/Djibouti', 'Africa/Djibouti'),
    ('America/Merida', 'America/Merida'),
    ('Australia/Hobart', 'Australia/Hobart'),
    ('Asia/Muscat', 'Asia/Muscat'),
    ('US/Eastern', 'US/Eastern'),
    ('Asia/Kabul', 'Asia/Kabul'),
    ('Europe/Nicosia', 'Europe/Nicosia'),
    ('Asia/Dubai', 'Asia/Dubai'),
    ('Asia/Famagusta', 'Asia/Famagusta'),
    ('Etc/GMT-13', 'Etc/GMT-13'),
    ('Africa/El_Aaiun', 'Africa/El_Aaiun'),
    ('Pacific/Fakaofo', 'Pacific/Fakaofo'),
    ('Asia/Calcutta', 'Asia/Calcutta'),
    ('Europe/Belfast', 'Europe/Belfast'),
    ('Libya', 'Libya'),
    ('UCT', 'UCT'),
    ('Africa/Lubumbashi', 'Africa/Lubumbashi'),
    ('America/Winnipeg', 'America/Winnipeg'),
    ('America/Cayenne', 'America/Cayenne'),
    ('Australia/Tasmania', 'Australia/Tasmania'),
    ('Europe/Tallinn', 'Europe/Tallinn'),
    ('Asia/Phnom_Penh', 'Asia/Phnom_Penh'),
    ('Asia/Hong_Kong', 'Asia/Hong_Kong'),
    ('Europe/Athens', 'Europe/Athens'),
    ('Australia/South', 'Australia/South'),
    ('Africa/Monrovia', 'Africa/Monrovia'),
    ('America/Cayman', 'America/Cayman'),
    ('Pacific/Norfolk', 'Pacific/Norfolk'),
    ('Asia/Yekaterinburg', 'Asia/Yekaterinburg'),
    ('HST', 'HST'),
    ('Europe/Simferopol', 'Europe/Simferopol'),
    ('Europe/Podgorica', 'Europe/Podgorica'),
    ('America/Port-au-Prince', 'America/Port-au-Prince'),
    ('Africa/Addis_Ababa', 'Africa/Addis_Ababa'),
    ('Hongkong', 'Hongkong'),
    ('Africa/Nairobi', 'Africa/Nairobi'),
    ('Asia/Katmandu', 'Asia/Katmandu'),
    ('Asia/Colombo', 'Asia/Colombo'),
    ('America/Montserrat', 'America/Montserrat'),
    ('Africa/Kinshasa', 'Africa/Kinshasa'),
    ('America/Fort_Wayne', 'America/Fort_Wayne'),
    ('GB-Eire', 'GB-Eire'),
    ('Africa/Banjul', 'Africa/Banjul'),
    ('Africa/Ceuta', 'Africa/Ceuta'),
    ('Europe/Bratislava', 'Europe/Bratislava'),
    ('Europe/Riga', 'Europe/Riga'),
    ('America/Dawson_Creek', 'America/Dawson_Creek'),
    ('America/Yellowknife', 'America/Yellowknife'),
    ('Asia/Beirut', 'Asia/Beirut'),
    ('Europe/Monaco', 'Europe/Monaco'),
    ('Africa/Bujumbura', 'Africa/Bujumbura'),
    ('America/Puerto_Rico', 'America/Puerto_Rico'),
    ('Africa/Ouagadougou', 'Africa/Ouagadougou'),
    ('America/Indiana/Indianapolis', 'America/Indiana/Indianapolis'),
    ('Asia/Thimbu', 'Asia/Thimbu'),
    ('Europe/Sarajevo', 'Europe/Sarajevo'),
    ('Etc/GMT+12', 'Etc/GMT+12'),
    ('Etc/GMT-10', 'Etc/GMT-10'),
    ('Asia/Manila', 'Asia/Manila'),
    ('America/Shiprock', 'America/Shiprock'),
    ('Australia/Currie', 'Australia/Currie'),
    ('Asia/Novosibirsk', 'Asia/Novosibirsk'),
    ('Australia/Melbourne', 'Australia/Melbourne'),
    ('Europe/Vilnius', 'Europe/Vilnius'),
    ('Pacific/Noumea', 'Pacific/Noumea'),
    ('Atlantic/South_Georgia', 'Atlantic/South_Georgia'),
    ('Europe/London', 'Europe/London'),
    ('America/Argentina/San_Luis', 'America/Argentina/San_Luis'),
    ('America/Dawson', 'America/Dawson'),
    ('Europe/Lisbon', 'Europe/Lisbon'),
    ('America/St_Vincent', 'America/St_Vincent'),
    ('Canada/Atlantic', 'Canada/Atlantic'),
    ('Europe/Brussels', 'Europe/Brussels'),
    ('America/Panama', 'America/Panama'),
    ('Asia/Dacca', 'Asia/Dacca'),
    ('Asia/Dushanbe', 'Asia/Dushanbe'),
    ('Indian/Christmas', 'Indian/Christmas'),
    ('Etc/Universal', 'Etc/Universal'),
    ('Asia/Hovd', 'Asia/Hovd'),
    ('Europe/Copenhagen', 'Europe/Copenhagen'),
    ('EET', 'EET'),
    ('America/Barbados', 'America/Barbados'),
    ('Asia/Kamchatka', 'Asia/Kamchatka'),
    ('Asia/Seoul', 'Asia/Seoul'),
    ('Pacific/Pitcairn', 'Pacific/Pitcairn'),
    ('Europe/Zaporozhye', 'Europe/Zaporozhye'),
    ('Asia/Dili', 'Asia/Dili'),
    ('Asia/Jayapura', 'Asia/Jayapura'),
    ('Etc/GMT', 'Etc/GMT'),
    ('America/Noronha', 'America/Noronha'),
    ('Asia/Anadyr', 'Asia/Anadyr'),
    ('America/Havana', 'America/Havana'),
    ('America/Punta_Arenas', 'America/Punta_Arenas'),
    ('Etc/GMT-4', 'Etc/GMT-4'),
    ('Asia/Aqtobe', 'Asia/Aqtobe'),
    ('America/Louisville', 'America/Louisville'),
    ('America/Adak', 'America/Adak'),
    ('America/Iqaluit', 'America/Iqaluit'),
    ('Asia/Kashgar', 'Asia/Kashgar'),
    ('US/Pacific', 'US/Pacific'),
    ('GB', 'GB'),
    ('America/Santiago', 'America/Santiago'),
    ('Antarctica/Davis', 'Antarctica/Davis'),
    ('Australia/Broken_Hill', 'Australia/Broken_Hill'),
    ('Pacific/Johnston', 'Pacific/Johnston'),
    ('Asia/Oral', 'Asia/Oral'),
    ('America/Mendoza', 'America/Mendoza'),
    ('Etc/GMT+6', 'Etc/GMT+6'),
    ('America/Argentina/ComodRivadavia', 'America/Argentina/ComodRivadavia'),
    ('America/Argentina/Mendoza', 'America/Argentina/Mendoza'),
    ('America/Bogota', 'America/Bogota'),
    ('America/Edmonton', 'America/Edmonton'),
    ('Etc/GMT-7', 'Etc/GMT-7'),
    ('Africa/Malabo', 'Africa/Malabo'),
    ('Asia/Tokyo', 'Asia/Tokyo'),
    ('America/Goose_Bay', 'America/Goose_Bay'),
    ('Atlantic/Cape_Verde', 'Atlantic/Cape_Verde'),
    ('Brazil/West', 'Brazil/West'),
    ('Pacific/Bougainville', 'Pacific/Bougainville'),
    ('Europe/Malta', 'Europe/Malta'),
    ('America/Argentina/San_Juan', 'America/Argentina/San_Juan'),
    ('Europe/Chisinau', 'Europe/Chisinau'),
    ('Pacific/Funafuti', 'Pacific/Funafuti'),
    ('Atlantic/Madeira', 'Atlantic/Madeira'),
    ('Europe/Tirane', 'Europe/Tirane'),
    ('Europe/Mariehamn', 'Europe/Mariehamn'),
    ('America/Coral_Harbour', 'America/Coral_Harbour'),
    ('Australia/Canberra', 'Australia/Canberra'),
    ('Africa/Asmara', 'Africa/Asmara'),
    ('America/St_Thomas', 'America/St_Thomas'),
    ('Asia/Almaty', 'Asia/Almaty'),
    ('Europe/Zagreb', 'Europe/Zagreb'),
    ('America/Guyana', 'America/Guyana'),
    ('Indian/Cocos', 'Indian/Cocos'),
    ('Antarctica/Syowa', 'Antarctica/Syowa'),
    ('Australia/North', 'Australia/North'),
    ('Etc/Greenwich', 'Etc/Greenwich'),
    ('Asia/Baku', 'Asia/Baku'),
    ('Europe/Stockholm', 'Europe/Stockholm'),
    ('Africa/Casablanca', 'Africa/Casablanca'),
    ('America/Toronto', 'America/Toronto'),
    ('America/Tortola', 'America/Tortola'),
    ('Europe/Warsaw', 'Europe/Warsaw'),
    ('Indian/Mauritius', 'Indian/Mauritius'),
    ('Etc/GMT-3', 'Etc/GMT-3'),
    ('America/Kralendijk', 'America/Kralendijk'),
    ('Pacific/Nauru', 'Pacific/Nauru'),
    ('Asia/Saigon', 'Asia/Saigon'),
    ('Asia/Ulaanbaatar', 'Asia/Ulaanbaatar'),
    ('America/Paramaribo', 'America/Paramaribo'),
    ('Europe/Volgograd', 'Europe/Volgograd'),
    ('Atlantic/Jan_Mayen', 'Atlantic/Jan_Mayen'),
    ('Asia/Choibalsan', 'Asia/Choibalsan'),
    ('Asia/Ashgabat', 'Asia/Ashgabat'),
    ('Etc/UCT', 'Etc/UCT'),
    ('Asia/Harbin', 'Asia/Harbin'),
    ('Mexico/BajaNorte', 'Mexico/BajaNorte'),
    ('Europe/Minsk', 'Europe/Minsk'),
    ('Pacific/Ponape', 'Pacific/Ponape'),
    ('NZ-CHAT', 'NZ-CHAT'),
    ('America/Nuuk', 'America/Nuuk'),
    ('Asia/Chongqing', 'Asia/Chongqing'),
    ('US/Alaska', 'US/Alaska'),
    ('America/Pangnirtung', 'America/Pangnirtung'),
    ('Asia/Bahrain', 'Asia/Bahrain'),
    ('Asia/Jerusalem', 'Asia/Jerusalem'),
    ('Asia/Rangoon', 'Asia/Rangoon'),
    ('Europe/Andorra', 'Europe/Andorra'),
    ('America/Campo_Grande', 'America/Campo_Grande'),
    ('America/Grand_Turk', 'America/Grand_Turk'),
    ('Europe/Busingen', 'Europe/Busingen'),
    ('Canada/Newfoundland', 'Canada/Newfoundland'),
    ('Canada/Yukon', 'Canada/Yukon'),
    ('America/Thunder_Bay', 'America/Thunder_Bay'),
    ('Africa/Brazzaville', 'Africa/Brazzaville'),
    ('Asia/Karachi', 'Asia/Karachi'),
    ('Europe/Astrakhan', 'Europe/Astrakhan'),
    ('Africa/Tripoli', 'Africa/Tripoli'),
    ('America/Nome', 'America/Nome'),
    ('Asia/Krasnoyarsk', 'Asia/Krasnoyarsk'),
    ('America/Catamarca', 'America/Catamarca')
)