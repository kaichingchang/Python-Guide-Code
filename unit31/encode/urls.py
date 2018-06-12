from django.urls import path

from . import views

app_name = 'encode'
urlpatterns = [
    path('', views.result, name='result'),
]

# 檔名: encode/urls.py
# 作者: Kaiching Chang
# 時間: June, 2018
