from random import shuffle
 
class GuessGame:
   def __init__(self, digit=None):
      if digit == None or digit < 3 or digit > 6:
         self.length = 4
      else:
         self.length = digit
 
      self.set_game();
 
   def set_game(self):
      while True:
         self.answer = [chr(i) for i in range(48, 58)]
         shuffle(self.answer)
         self.answer = self.answer[0:self.length]
         if self.answer[0] != "0":
            break
       
      self.times = 0
      self.a = 0
      self.b = 0
 
if __name__ == "__main__":  
   g = GuessGame(6)
   print(g.answer)
   g = GuessGame(5)
   print(g.answer)
   g = GuessGame(4)
   print(g.answer)
   g = GuessGame(3)
   print(g.answer)
  
# 檔名: exercise2002.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
