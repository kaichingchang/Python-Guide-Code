class Demo:
  def set_att(self, a, b):
    self.a = a
    self.b = b

  def do_something(self):
    return self.a + self.b

d = Demo()
d.set_att(11, 22)
print(d.do_something())

# 檔名: class_demo.py 
# 作者: Kaiching Chang
# 時間: July, 2014
