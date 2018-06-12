from django.contrib import admin

from .models import Sentence

class SentenceAdmin(admin.ModelAdmin):
    fields = ['original_text', 'encoding_text']

admin.site.register(Sentence, SentenceAdmin)

# 檔名: admin.py
# 作者: Kaiching Chang
# 時間: June, 2018
