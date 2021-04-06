"""
WSGI config for PaperReader project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import sys

sys.path.append('/home/ubuntu/my_pro/env_PaperReader/lib/python3.6/site-packages')  # 指向虚拟环境

import os
os.chdir('/home/ubuntu/my_pro/PaperReader')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PaperReader.settings')

application = get_wsgi_application()
