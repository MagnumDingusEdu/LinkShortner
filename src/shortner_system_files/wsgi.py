import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shortner_system_files.settings.prod_settings')

application = get_wsgi_application()
