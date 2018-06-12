# 建立 HTML 文件
from django.http import HttpResponse

# 取得現在時間
from datetime import datetime

now = datetime.now()
hour = str(now.hour)
minute = str(now.minute)
second = str(now.second)
now_str = hour + ":" + minute + ":" + second

# 顯示首頁內容
def now(request):
  return HttpResponse("現在時間是 " + now_str)

# 檔名: views.py
# 作者: Kaiching Chang
# 時間: June, 2018
