SECRET_KEY = 'django-insecure-)k_9xlf_+nid7-*(!6)2*ge!xjd-)p)wwho@4yr#+#s2gygqny'


DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'youtube_clone_database',
        'USER': 'root',
        'PASSWORD': 'IloveBeau123!',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'autocommit': True
        }
    }
    
}
