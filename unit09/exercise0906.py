class FactorialDemo:
   def set_value(self, n):
      i = 1
      p = 1
      while i <= n:
         p *= i
         i += 1
 
      self.value = p
 
i = FactorialDemo()
i.set_value(int(input("n: ")))
print(i.value)
  
# 檔名: exercise0906.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
