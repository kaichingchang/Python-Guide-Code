from tkinter import *

# Hello 的 View 類別
class GameView(Frame):
  # 設定初值
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.winfo_toplevel().title("猜數字遊戲")
    self.grid()
    self.createWidgets()

  # 建立視窗元件
  def createWidgets(self):
    self.text = Label(self)
    self.text["text"] = "輸入："
    self.text.grid(row=0, column=0)

    self.name = Entry(self)
    self.name["width"] = "10"
    self.name.grid(row=0, column=1)

    self.button = Button(self)
    self.button["text"] = "猜測"
    self.button.grid(row=0, column=2)

    self.result = Label(self)
    self.result["text"] = ""
    self.result["width"] = "10"
    self.result["height"] = "1"
    self.result.grid(row=3, column=0, columnspan=3)

# GUI 執行部分
if __name__ == '__main__':
  root = Tk()
  app = GameView(master=root)
  root.mainloop()

# 檔名: game_view.py
# 作者: Kaiching Chang
# 時間: May, 2018
