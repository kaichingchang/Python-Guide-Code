from datetime import datetime

from django.shortcuts import render

def now(request):
  now = datetime.now()
  h = str(now.hour)
  if len(h) == 1:
    h = "0" + h
  m = str(now.minute)
  if len(m) == 1:
    m = "0" + m
  s = str(now.second)
  if len(s) == 1:
    s = "0" + s
  now_str = h + ":" + m + ":" + s

  return render(request, 'web_demo/home.html', {
    'current_time': now_str,
  })

# 檔名: views.py
# 作者: Kaiching Chang
# 時間: June, 2018
