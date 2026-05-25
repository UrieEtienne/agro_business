from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY
SECRET_KEY = 'django-insecure-ny2y&gx*7g7m1%h$rshf!bgp84*zhh8i9etxwxm$9=*$a8q143'

DEBUG = True

ALLOWED_HOSTS = []

# PERSONNALISER LE DASHBOARD

JAZZMIN_SETTINGS = {

    # TITRE FENÊTRE
    "site_title": "Dashboard Eden Agro",

    # TITRE HEADER
    "site_header": "Eden Agro Business",

    # LOGO
    "site_logo": "images/logo.png",

    # LOGIN
    "login_logo": "images/logo.png",

    # NOM
    "site_brand": "Eden Agro",

    # BIENVENUE
    "welcome_sign": "Bienvenue dans Eden Agro Business",

    # COPYRIGHT
    "copyright": "Eden Agro Business",

    # RECHERCHE
    "search_model": [
        "blog.Post",
        "products.Product",
        "gallery.Media",
    ],
     # =========================
    # MENU TOP
    # =========================

    "topmenu_links": [

        # HOME SITE PUBLIC
        {
            "name": "Accueil",
            "url": "/",
            "new_window": False,
        },

    ],

    "custom_css": "css/admin.css",



    # ICÔNES
    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",

        "blog.Post": "fas fa-newspaper",

        "products.Product": "fas fa-seedling",

        "gallery.Media": "fas fa-image",

        "contact.Contact": "fas fa-envelope",

        "about.About": "fas fa-building",
    },

    # MENU LATÉRAL
    "navigation_expanded": True,

    # MASQUER HISTORIQUE
    "hide_apps": [],

    # ORDRE
    "order_with_respect_to": [
        "blog",
        "products",
        "gallery",
        "contact",
        "about",
    ],

    # UI MODERNE
    "show_sidebar": True,

    "custom_css": "css/admin.css",
}

# APPLICATIONS
INSTALLED_APPS = [
    'admin_interface',
    'colorfield',

    # Django Apps
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local Apps
    'home',
    'about',
    'products',
    'gallery',
    'blog',
    'contact',
    'testimonials',


]


# MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLS
ROOT_URLCONF = 'config.urls'


# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Global templates folder
        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [

                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = 'config.wsgi.application'


# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# PASSWORD VALIDATION
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


# INTERNATIONALIZATION
LANGUAGE_CODE = 'fr-en'

TIME_ZONE = 'Africa/Conakry'

USE_I18N = True

USE_TZ = True


# STATIC FILES
STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# MEDIA FILES
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# DEFAULT PRIMARY KEY
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'