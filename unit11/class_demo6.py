class Demo:
  def __init__(self, v1=11, v2=22):
    self.__a = v1
    self.__b = v2

  def do_something(self):
    return self.__a + self.__b

d = Demo(12, 34)
print(d.do_something())

# 檔名: class_demo6.py 
# 作者: Kaiching Chang
# 時間: July, 2014
