from tkinter import Tk
from hello_view2 import HelloView

# HelloView 的 Controller 類別
class HelloController:
  # 設定初值
  def __init__(self):
    self.app = HelloView(master=Tk())
    self.app.button["command"] = self.action
    self.app.mainloop()

  # 按下按鈕的事件
  def action(self):
    self.app.result["text"] = "按鈕被按"

# GUI 執行部分
if __name__ == '__main__':
  app = HelloController()

# 檔名: hello_controller.py
# 作者: Kaiching Chang
# 時間: June, 2018
