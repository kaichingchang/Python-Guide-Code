class IntegerDemo:
   def set_value(self, v):
      self.value = v
 
   def add(self, p):
      self.value += p
 
i = IntegerDemo()
i.set_value(25)
i.add(24)
print(i.value)
  
# 檔名: exercise0901.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
