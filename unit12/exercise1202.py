class FactorialDemo:
   def __init__(self, n):
      self.set_value(n)
 
   def set_value(self, n):
      i = 1
      p = 1
      while i <= n:
         p *= i
         i += 1
 
      self.__value = p
 
   def get_value(self):
      return self.__value
 
if __name__ == "__main__":
   i = FactorialDemo(int(input("n: ")))
   print(i.get_value())
  
# 檔名: exercise1202.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
