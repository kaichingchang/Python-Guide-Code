from tkinter import *

# Hello 的 View 類別
class HelloView(Frame):
  # 設定初值
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.winfo_toplevel().title("Hello World!")
    self.grid()
    self.createWidgets()

  # 建立視窗元件
  def createWidgets(self):
    self.text = Label(self)
    self.text["text"] = "Hello World!"
    self.text["width"] = "30"
    self.text["height"] = "5"
    self.text["bg"] = "black"
    self.text["fg"] = "white"
    self.text.grid(row=0, column=0)

# GUI 執行部分
if __name__ == '__main__':
  root = Tk()
  app = HelloView(master=root)
  root.mainloop()

# 檔名: hello_view.py
# 作者: Kaiching Chang
# 時間: May, 2018
