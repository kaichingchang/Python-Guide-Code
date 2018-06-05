# 引入 Kivy 並指定版本
import kivy
kivy.require('1.10.0')

# 引入必要的類別
from kivy.app import App
from kivy.uix.label import Label

# 指定視窗大小
from kivy.core.window import Window
Window.size = (300, 100)

# App 類別
class HelloApp(App):
  def build(self):
    return Label(text='Hello World!', font_size='30sp')

# 執行部分
if __name__ == '__main__':
  HelloApp().run()

# 檔名: hellokivy.py
# 作者: Kaiching Chang
# 時間: June, 2018
