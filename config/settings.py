from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ny2y&gx*7g7m1%h$rshf!bgp84*zhh8i9etxwxm$9=*$a8q143'

DEBUG = True

ALLOWED_HOSTS = []
# =========================
# JAZZMIN
# =========================

JAZZMIN_SETTINGS = {

    "site_title": "Eden Agro ERP",

    "site_header": "Eden Agro Business",

    "site_brand": "Eden Agro",

    "welcome_sign": "Bienvenue dans le système Eden Agro",

    "copyright": "Eden Agro Business",

    "site_logo": "images/logo.jpg",

    "login_logo": "images/logo.jpg",

    "site_icon": "images/logo.jpg",

    "navigation_expanded": True,

    "show_sidebar": True,

    "custom_css": "css/admin_custom.css",

    "icons": {

        "auth": "fas fa-users-cog",

        "auth.user": "fas fa-user",

        "auth.Group": "fas fa-users",

        "blog.Post": "fas fa-newspaper",

        "produits.Produit": "fas fa-seedling",

        "gallery.Media": "fas fa-image",

        "contact.Contact": "fas fa-envelope",

        "about.About": "fas fa-building",

        "commandes.Commande": "fas fa-shopping-cart",

        "paiements.Paiement": "fas fa-money-bill-wave",

        "stocks.Stock": "fas fa-boxes",

        "clients.Client": "fas fa-users",

    },

    "order_with_respect_to": [

        "blog",
        "gallery",
        "newsletter",

        "produits",
        "categories",
        "stocks",
        "commandes",
        "paiements",
        "factures",
        "livraisons",

    ],
}


# =========================
# APPLICATIONS
# =========================

INSTALLED_APPS = [
    'jazzmin',
    
    # DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # API
    'rest_framework',
    'rest_framework_simplejwt',

    # COMMUNICATION
    'home',
    'about',
    'blog',
    'gallery',
    'contact',
    'testimonials',
    'newsletter',

    # E-COMMERCE
    'produits',
    'categories',
    'ecommerce',
    'stocks',
    'panier',
    'commandes',
    'paiements',
    'factures',
    'livraisons',
    'clients',

    # USERS
    'comptes',
]


# =========================
# MIDDLEWARE
# =========================

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'config.urls'


# =========================
# TEMPLATES
# =========================

TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

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


WSGI_APPLICATION = 'config.wsgi.application'


# =========================
# DATABASE
# =========================

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',

    }
}


# =========================
# PASSWORDS
# =========================

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


# =========================
# LANGUE
# =========================

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Africa/Conakry'

USE_I18N = True

USE_TZ = True

# =========================
# STATIC SETTINGS
# =========================

STATICFILES_FINDERS = [

    'django.contrib.staticfiles.finders.FileSystemFinder',

    'django.contrib.staticfiles.finders.AppDirectoriesFinder',

]

# =========================
# STATIC
# =========================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# =========================
# MEDIA
# =========================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# La Securite

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:8000",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = "SAMEORIGIN"

# =========================
# USER MODEL
# =========================

AUTH_USER_MODEL = 'comptes.User'


# =========================
# EMAIL
# =========================

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = 'tonemail@gmail.com'

EMAIL_HOST_PASSWORD = 'mot_de_passe_application'


# =========================
# MOBILE MONEY
# =========================

ORANGE_MONEY_API_KEY = 'TON_API_KEY'

ORANGE_MONEY_SECRET = 'TON_SECRET'

MTN_API_KEY = 'TON_API_KEY'

MTN_SECRET = 'TON_SECRET'


# =========================
# JWT
# =========================

REST_FRAMEWORK = {

    
    'DEFAULT_AUTHENTICATION_CLASSES': (
        
        'rest_framework_simplejwt.authentication.JWTAuthentication',

    ),

}


