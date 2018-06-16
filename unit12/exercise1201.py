class IntegerDemo:
   def __init__(self, v):
      self.__value = v
 
   def set_value(self, v):
      self.__value = v
 
   def get_value(self):
      return self.__value
 
   def add(self, p):
      self.__value += p
    
   def subtract(self, p):
      self.__value -= p
 
   def multiply(self, p):
      self.__value *= p
 
   def divide(self, p):
      self.__value /= p
 
if __name__ == "__main__":
   i = IntegerDemo(int(input("v: ")))
   i.add(int(input("+: ")))
   i.subtract(int(input("-: ")))
   i.multiply(int(input("*: ")))
   i.divide(int(input("/: ")))
   print(i.get_value())
  
# 檔名: exercise1201.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
