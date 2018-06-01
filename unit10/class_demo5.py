class Demo:
  def set_att(self, a=22, b=33):
    self.__a = a
    self.__b = b

  def do_something(self):
    return self.__a + self.__b

d = Demo()
d.set_att()
print(d.do_something())
d.__a = 5
print(d.__a)
print(d.do_something())

# 檔名: class_demo5.py 
# 作者: Kaiching Chang
# 時間: July, 2014
