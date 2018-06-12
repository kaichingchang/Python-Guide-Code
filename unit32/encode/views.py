from django.shortcuts import render

from .encrypt import Encrypt
from .models import Sentence

def input(request):
  return render(request, 'encode/input.html', {
  })

def result(request):
  e = Encrypt()
  s = Sentence()
  s.original_text = request.POST['original_text']
  s.encoding_text = e.toEncode(s.original_text)
  s.save()
  return render(request, 'encode/result.html', {
    'encoding_text': s.encoding_text,
  })

# 檔名: encode/views.py
# 作者: Kaiching Chang
# 時間: June, 2018
