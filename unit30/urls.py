from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('', views.now),
  path('admin/', admin.site.urls),
]

# 檔名: urls.py
# 作者: Kaiching Chang
# 時間: June, 2018
