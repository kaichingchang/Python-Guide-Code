class FibonacciDemo:
   def set_value(self, n):
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
      return self.__value
 
i = FibonacciDemo()
i.set_value(int(input("n: ")))
print(i.get_value())
  
# 檔名: exercise1003.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
