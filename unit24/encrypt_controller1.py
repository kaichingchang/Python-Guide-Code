from tkinter import Tk
from encrypt_view import EncryptView

# Encrypt 的 Controller 類別
class EncryptController:
  # 設定初值
  def __init__(self):
    self.app = EncryptView(master=Tk())
    self.app.nb["command"] = self.nm
    self.app.lb["command"] = self.lm
    self.app.sb["command"] = self.sm
    self.app.eb["command"] = self.em
    self.app.db["command"] = self.dm
    self.app.cb["command"] = self.cm
    self.app.cb2["command"] = self.cm2
    self.app.mainloop()

  # 按下新建按鈕的事件
  def nm(self):
    self.app.dt["text"] = "觸發新建按鈕的事件。"

  # 按下載入按鈕的事件
  def lm(self):
    self.app.dt["text"] = "觸發載入按鈕的事件。"

  # 按下儲存按鈕的事件
  def sm(self):
    self.app.dt["text"] = "觸發儲存按鈕的事件。"

  # 按下編碼按鈕的事件
  def em(self):
    self.app.dt["text"] = "觸發編碼按鈕的事件。"

  # 按下解碼按鈕的事件
  def dm(self):
    self.app.dt["text"] = "觸發解碼按鈕的事件。"

  # 按下清除按鈕的事件
  def cm(self):
    self.app.dt["text"] = "觸發清除按鈕的事件。"

  # 按下拷貝按鈕的事件
  def cm2(self):
    self.app.dt["text"] = "觸發拷貝按鈕的事件。"

# GUI 執行部分
if __name__ == '__main__':
  app = EncryptController()

# 檔名: encrypt_controller1.py
# 作者: Kaiching Chang
# 時間: May, 2018
