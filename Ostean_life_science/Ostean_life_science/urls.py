from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('shop/', shop, name='shop'),
    path('product-detail/', product_detail, name='product-detail'),
]

handler404 = not_found
