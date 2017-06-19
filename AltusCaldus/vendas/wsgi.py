# import os
# from dj_static import Cling
# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vendas.settings")

# application = Cling(get_wsgi_application())

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vendas.settings")

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)