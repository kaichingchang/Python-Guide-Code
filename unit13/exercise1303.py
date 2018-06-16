"""模組文件字串"""

class FibonacciDemo:
   """類別文件字串"""

   def __init__(self, n):
      """方法文件字串"""
   
      self.set_value(n)
 
   def set_value(self, n):
      """方法文件字串"""
   
      n1 = 0
      n2 = 1
      i = 3
      while i <= n:
         n3 = n1 + n2
         n1 = n2
         n2 = n3
         i += 1
 
      self.__value = n3
 
   def get_value(self):
      """方法文件字串"""
   
      return self.__value
 
if __name__ == "__main__":
   i = FibonacciDemo(int(input("n: ")))
   print(i.get_value())
  
# 檔名: exercise1303.py 
# 作者: Kaiching Chang 
# 時間: June, 2018
