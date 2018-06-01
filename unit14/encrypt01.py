# 定義 Encrypt 類別
class Encrypt:
  def __init__(self):
    self.setcode()

  def setcode(self):
    self.code = "code"

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

# 檔名: encrypt01.py 
# 作者: Kaiching Chang
# 時間: July, 2014
