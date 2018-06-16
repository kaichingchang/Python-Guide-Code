class FactorialDemo:
   def set_value(self, n):
      i = 1
      p = 1
      while i <= n:
         p *= i
         i += 1
 
      self.__value = p
 
   def get_value(self):
      return self.__value
 
i = FactorialDemo()
i.set_value(int(input("n: ")))
print(i.get_value())
  
# 檔名: exercise1002.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
