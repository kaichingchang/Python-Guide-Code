from django.db import models

class Sentence(models.Model):
  original_text = models.CharField(max_length=200)
  encoding_text = models.CharField(max_length=200)

  def __str__(self):
    return self.encoding_text

# 檔名: encode/models.py
# 作者: Kaiching Chang
# 時間: June, 2018
