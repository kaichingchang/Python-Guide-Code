from django.http import HttpResponse

from .encrypt import Encrypt
from .models import Sentence

def result(request):
  e = Encrypt()
  s1 = "There is no spoon."
  s2 = e.toEncode(s1)
  s = Sentence(original_text = s1, encoding_text = s2)
  s.save()
  return HttpResponse("編碼結果為 " + s2)

# 檔名: encode/views.py
# 作者: Kaiching Chang
# 時間: June, 2018
