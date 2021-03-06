SECRET_KEY = "123"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'test',                      # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'lot',
]

ROOT_URLCONF = 'tests.urls'

ALLOWED_HOSTS = ['testserver',]

BACKEND_SESSION_KEY = "test"

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'lot.middleware.LOTMiddleware',
)

AUTHENTICATION_BACKENDS = ['lot.auth_backend.LOTBackend']

LOT_MIDDLEWARE_PARAM_NAME = 'uuid-login'
