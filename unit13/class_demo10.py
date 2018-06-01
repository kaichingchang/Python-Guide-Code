"""Demo 類別的範例。

這個模組示範文件字串的寫法。"""

#類別的註解。
class Demo:
  """類別的文件字串。"""

  # __init__() 的註解。
  def __init__(self, v1=11, v2=22):
    """ __init__() 的文件字串。"""
    self.__a = v1
    self.__b = v2

  # 方法的註解。
  def do_something(self):
    """方法的文件字串。"""
    return self.__a + self.__b

if __name__ == "__main__":
  d = Demo(12, 34)
  print(d.do_something())

# 檔名: class_demo10.py
# 作者: Kaiching Chang
# 時間: May, 2018
