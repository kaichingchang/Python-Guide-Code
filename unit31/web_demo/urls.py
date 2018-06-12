from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.now),
    path('encode/', include('encode.urls')),
    path('admin/', admin.site.urls),
]

# 檔名: web_demo/urls.py
# 作者: Kaiching Chang
# 時間: June, 2018
