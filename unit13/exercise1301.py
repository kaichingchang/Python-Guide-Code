"""模組文件字串"""

class IntegerDemo:
   """類別文件字串"""

   def __init__(self, v):
      """方法文件字串"""
      
      self.__value = v
 
   def set_value(self, v):
      """方法文件字串"""
   
      self.__value = v
 
   def get_value(self):
      """方法文件字串"""
   
      return self.__value
 
   def add(self, p):
      """方法文件字串"""
   
      self.__value += p
    
   def subtract(self, p):
      """方法文件字串"""
   
      self.__value -= p
 
   def multiply(self, p):
      """方法文件字串"""
   
      self.__value *= p
 
   def divide(self, p):
      """方法文件字串"""
   
      self.__value /= p
 
if __name__ == "__main__":
   i = IntegerDemo(int(input("v: ")))
   i.add(int(input("+: ")))
   i.subtract(int(input("-: ")))
   i.multiply(int(input("*: ")))
   i.divide(int(input("/: ")))
   print(i.get_value())
  
# 檔名: exercise1301.py 
# 作者: Kaiching Chang 
# 時間: June, 2018
