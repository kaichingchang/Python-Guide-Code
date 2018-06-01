class Demo:
  def set_att(self, a=22, b=33):
    self.a = a
    self.b = b

  def do_something(self):
    return self.a + self.b

d = Demo()
d.set_att()
print(d.do_something())
d.a = 5
print(d.do_something())

# 檔名: class_demo4.py 
# 作者: Kaiching Chang
# 時間: July, 2014
