from django.urls import path, re_path
from django.contrib import admin
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('^api$', generatorAPI, name='api'),
    re_path('^api/$', generatorAPI, name='api'),

    re_path('^', redirectHandler, name="handler")
]
