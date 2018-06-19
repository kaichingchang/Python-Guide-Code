from tkinter import *

# Hello 的 View 類別
class HelloView(Frame):
  # 設定初值
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.winfo_toplevel().title("Hello")
    self.grid()
    self.createWidgets()

  # 建立視窗元件
  def createWidgets(self):
    self.text = Label(self)
    self.text["text"] = "請輸入暱稱："
    self.text["width"] = "30"
    self.text["height"] = "1"
    self.text.grid(row=0, column=0)

    self.name = Entry(self)
    self.name["width"] = "30"
    self.name.grid(row=1, column=0)

    self.button = Button(self)
    self.button["text"] = "執行"
    self.button.grid(row=2, column=0)

    self.result = Label(self)
    self.result["text"] = ""
    self.result["width"] = "30"
    self.result["height"] = "1"
    self.result.grid(row=3, column=0)

# GUI 執行部分
if __name__ == '__main__':
  root = Tk()
  app = HelloView(master=root)
  root.mainloop()

# 檔名: hello_view2.py
# 作者: Kaiching Chang
# 時間: May, 2018
