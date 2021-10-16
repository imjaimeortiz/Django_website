"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ["DJANGO_SETTINGS_MODULE"] = "website.settings"

'''activator = '/home/imjaimeortiz/myvenv/bin/activate'  
with open(activator) as f:
    exec(f.read(), {'__file__': activator})
'''
application = get_wsgi_application()

    