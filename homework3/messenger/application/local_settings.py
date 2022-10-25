from pickle import TRUE


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
SECRET_KEY = 'django-insecure-fvbv@#(#2)_q&wl89o66qcxf%p#_*)b*z^2i&86hjg#_$)y=gt'