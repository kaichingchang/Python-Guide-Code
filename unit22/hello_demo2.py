from tkinter import *

root = Tk()
root.title("Hello")
root.geometry("276x116")
text = Label(root, text="請輸入暱稱：",
             width="30", height="2")
text.place(x=0, y=0)
name = Entry(root, width="30")
name.place(x=0, y=36)
button = Button(root, text="執行")
button.place(x=0, y=66)
result = Label(root, text="",
             width="30", height="2")
result.place(x=0, y=86)
root.mainloop()

# 檔名: hello_demo2.py
# 作者: Kaiching Chang
# 時間: June, 2018
