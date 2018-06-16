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
 
      self.value = n3
 
i = FibonacciDemo()
i.set_value(int(input("n: ")))
print(i.value)
  
# 檔名: exercise0907.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
