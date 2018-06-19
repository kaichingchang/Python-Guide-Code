from tkinter import *

root = Tk()
root.title("Hello")
text = Label(root, text="請輸入暱稱：",
             width="30", height="2")
text.pack()
name = Entry(root, width="30")
name.pack()
button = Button(root, text="執行")
button.pack()
result = Label(root, text="",
             width="30", height="2")
result.pack()
root.mainloop()

# 檔名: hello_demo.py
# 作者: Kaiching Chang
# 時間: June, 2018
