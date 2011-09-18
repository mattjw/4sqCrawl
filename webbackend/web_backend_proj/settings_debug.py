# Deployment plan:
#     Find '#~' in this file and update lines as appropriate.
#     Run python2.7 manage.py syncdb
#     Check the pythonpath in .wsgi file. Should include django root and django apps.


# Django settings for web_backend_proj project.

DEBUG = True  #~
__DJANGO_PATH = "/Users/matthew/Code/Projects/4sqCrawl/4sqCrawl/webbackend/web_backend_proj/"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': __DJANGO_PATH+'backend_db',                      # Or path to database file if using sqlite3.   #~
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    __DJANGO_PATH+"frontendapp/templates/",
)

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    __DJANGO_PATH+"frontendapp/static/",
)


