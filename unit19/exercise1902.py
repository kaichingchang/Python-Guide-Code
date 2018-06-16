from random import shuffle
 
class GuessGame:
   def __init__(self):
      self.set_game();
 
   def set_game(self):
      while True:
         self.answer = [chr(i) for i in range(48, 58)]
         shuffle(self.answer)
         self.answer = self.answer[0:4]
         if self.answer[0] != "0":
            break
       
      self.times = 0
      self.a = 0
      self.b = 0
 
if __name__ == "__main__":  
   g = GuessGame()
   print(g.answer)
  
# 檔名: exercise1902.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
