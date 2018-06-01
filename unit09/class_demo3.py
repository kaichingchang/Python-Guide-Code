class Demo:
  a = 11
  b = 22

  @classmethod
  def do_something(cls):
    cls.a += 1
    cls.b += 1
    return cls.a + cls.b

print(Demo.do_something())

# 檔名: class_demo3.py
# 作者: Kaiching Chang
# 時間: July, 2014
