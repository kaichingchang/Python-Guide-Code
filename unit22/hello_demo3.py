from tkinter import *

root = Tk()
root.title("Hello")
text = Label(root, text="請輸入暱稱：",
             width="30", height="1")
text.grid(row=0, column=0)
name = Entry(root, width="30")
name.grid(row=1, column=0)
button = Button(root, text="執行")
button.grid(row=2, column=0)
result = Label(root, text="",
               width="30", height="1")
result.grid(row=3, column=0)
root.mainloop()

# 檔名: hello_demo3.py
# 作者: Kaiching Chang
# 時間: June, 2018
