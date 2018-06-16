class IntegerDemo:
   def set_value(self, v):
      self.value = v
 
   def add(self, p):
      self.value += p
    
   def subtract(self, p):
      self.value -= p
 
i = IntegerDemo()
i.set_value(int(input("v: ")))
i.add(int(input("+: ")))
i.subtract(int(input("-: ")))
print(i.value)
  
# 檔名: exercise0903.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
