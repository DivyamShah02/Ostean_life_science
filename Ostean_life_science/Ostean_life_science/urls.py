from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', coming_soon, name='coming_soom'),
]

handler404 = not_found
