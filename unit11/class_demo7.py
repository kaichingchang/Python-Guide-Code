class Demo:
  def __init__(self, v1=11, v2=22):
    self.__a = v1
    self.__b = v2

  def get_a(self):
    return self.__a

  def get_b(self):
    return self.__b

  def set_a(self, value):
    self.__a = value

  def set_b(self, value):
     self.__b = value

  def do_something(self):
    return self.__a + self.__b

d = Demo(11)
print(d.do_something())
d.set_a(5)
print(d.do_something())

# 檔名: class_demo7.py
# 作者: Kaiching Chang
# 時間: July, 2014
