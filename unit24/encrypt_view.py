from tkinter import *
from tkinter.ttk import *

# Encrypt 的 View 類別
class EncryptView(Frame):
  # 設定初值
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.winfo_toplevel().title("編密碼小工具")
    self.grid()
    self.createWidgets()

  # 建立所有視窗元件
  def createWidgets(self):
    self.it = Label(self)
    self.it["text"] = "輸入："
    self.it.grid(row=0, column=0,
                 sticky=N+E)
    self.ifd = Entry(self)
    self.ifd["width"] = 60
    self.ifd.grid(row=0, column=1,
                  columnspan=6,
                  sticky=N+W)

    self.ot = Label(self)
    self.ot["text"] = "輸出："
    self.ot.grid(row=1, column=0,
                 sticky=N+E)
    self.ofd = Entry(self)
    self.ofd["width"] = 60
    self.ofd.grid(row=1, column=1,
                  columnspan=6,
                  sticky=N+W)

    self.nb = Button(self)
    self.nb["text"] = "新建"
    self.nb.grid(row=2, column=0,
                 sticky=N+W)
    self.lb = Button(self)
    self.lb["text"] = "載入"
    self.lb.grid(row=2, column=1,
                 sticky=N+W)
    self.sb = Button(self)
    self.sb["text"] = "存檔"
    self.sb.grid(row=2, column=2,
                 sticky=N+W)
    self.eb = Button(self)
    self.eb["text"] = "編碼"
    self.eb.grid(row=2, column=3,
                 sticky=N+W)
    self.db = Button(self)
    self.db["text"] = "解碼"
    self.db.grid(row=2, column=4,
                 sticky=N+W)
    self.cb = Button(self)
    self.cb["text"] = "清除"
    self.cb.grid(row=2, column=5,
                 sticky=N+W)
    self.cb2 = Button(self)
    self.cb2["text"] = "拷貝"
    self.cb2.grid(row=2, column=6,
                  sticky=N+W)

    self.dt = Label(self)
    m = "訊息欄"
    self.dt["text"] = m
    self.dt.grid(row=3, column=0,
                 columnspan=7,
                 sticky=N)

# GUI 執行部分
if __name__ == '__main__':
  root = Tk()
  app = EncryptView(master=root)
  root.mainloop()

# 檔名: encrypt_view.py
# 作者: Kaiching Chang
# 時間: May, 2018
