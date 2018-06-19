from tkinter import *

root = Tk()
root.title("猜數字遊戲")
text = Label(root, text="輸入：")
text.grid(row=0, column=0)
name = Entry(root, width="10")
name.grid(row=0, column=1)
button = Button(root, text="猜測")
button.grid(row=0, column=2)
result = Label(root, text="", width="10")
result.grid(row=1, column=0, columnspan=3)
root.mainloop()

# 檔名: game_demo.py
# 作者: Kaiching Chang
# 時間: June, 2018
