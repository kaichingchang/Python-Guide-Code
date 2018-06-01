class Demo:
  def __init__(self, v1=11, v2=None):
    if v2 is None:
      self.__b = v1
      self.__a = v1
    else:
      self.__a = v1
      self.__b = v2

  def do_something(self):
    return self.__a + self.__b

d1 = Demo()
print(d1.do_something())
d2 = Demo(13, 12)
print(d2.do_something())

# 檔名: class_demo8.py
# 作者: Kaiching Chang
# 時間: July, 2014
