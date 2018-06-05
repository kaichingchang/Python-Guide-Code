from tkinter import Tk
from encrypt import Encrypt
from encrypt_view import EncryptView

# Encrypt 的 Controller 類別
class EncryptController:
  # 設定初值
  def __init__(self):
    self.e = None
    self.userinput = ""
    self.result = ""

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
    self.e = Encrypt()
    self.app.dt["text"] = self.e

  # 按下載入按鈕的事件
  def lm(self):
    self.app.dt["text"] = "觸發載入按鈕的事件。"

  # 按下儲存按鈕的事件
  def sm(self):
    self.app.dt["text"] = "觸發儲存按鈕的事件。"

  # 按下編碼按鈕的事件
  def em(self):
    # 取得使用者輸入
    self.userinput = self.app.ifd.get()

    # 先測試使用者是否有輸入
    if self.userinput == "":
      m = "沒有輸入！"
      self.app.dt["text"] = m
    else:
      # 再測試是否有按過新建按鈕
      if self.e == None:
        m = "沒有密碼物件！"
        self.app.dt["text"] = m
      else:
        # 使用者有輸入
        # 並且有按過新建按鈕
        s = self.userinput
        r = self.e.toEncode(s)
        self.result = r
        self.app.ofd.delete(0, 200)
        self.app.ofd.insert(0, r)
        m = "編碼成功！"
        self.app.dt["text"] = m

  # 按下解碼按鈕的事件
  def dm(self):
    # 取得使用者輸入
    self.userinput = self.app.ifd.get()

    # 先測試使用者是否有輸入
    if self.userinput == "":
      m = "沒有輸入！"
      self.app.dt["text"] = m
    else:
      # 再測試是否有按過新建按鈕
      if self.e == None:
        m = "沒有密碼物件！"
        self.app.dt["text"] = m
      else:
        # 使用者有輸入
        # 並且有按過新建按鈕
        s = self.userinput
        r = self.e.toDecode(s)
        self.result = r
        self.app.ofd.delete(0, 200)
        self.app.ofd.insert(0, r)
        m = "解碼成功！"
        self.app.dt["text"] = m

  # 按下清除按鈕的事件
  def cm(self):
    self.app.dt["text"] = "觸發清除按鈕的事件。"

  # 按下拷貝按鈕的事件
  def cm2(self):
    self.app.dt["text"] = "觸發拷貝按鈕的事件。"

# 執行部分
if __name__ == '__main__':
  app = EncryptController()

# 檔名: encrypt_controller.py
# 作者: Kaiching Chang
# 時間: May, 2018
