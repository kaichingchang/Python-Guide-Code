# 使用 randint()
import random

# 定義 Encrypt 類別
class Encrypt:
  def __init__(self):
    self.setcode()

  def setcode(self):
    # 取得 a 、 b 值
    a = random.randint(0, 9)
    print(a) # 印出 a
    b = random.randint(0, 9)
    print(b) # 印出 b
    # 利用公式建立密碼表
    self.code = ""
    c = "a"
    i = 0
    while i < 26:
      x = c
      y = ord(x) * a + b
      m = y % 26
      self.code += chr(m + 97)
      c = chr(ord(c) + 1)
      i += 1

  def getcode(self):
    return self.code

  # 編碼的方法
  def toEncode(self, str):
    pass

  # 解碼的方法
  def toDecode(self, str):
    pass

# 測試部分
if __name__ == '__main__':
  e = Encrypt()
  print()
  print(e.getcode())
  print()

# 檔名: encrypt04.py
# 作者: Kaiching Chang
# 時間: July, 2014
