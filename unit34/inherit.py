# 父類別
class SuperClass:
  def __init__(self):
    print("superclass")

  def supermethod(self):
    print("supermethod")

# 子類別
class SubClass(SuperClass):
  def __init__(self):
    super().__init__()
    print("subclass")

  def submethod(self):
    print("submethod")

if __name__ == "__main__":
  demo = SubClass()
  demo.supermethod()
  demo.submethod()

# 檔名: inherit.py
# 作者: Kaiching Chang
# 時間: June, 2018
