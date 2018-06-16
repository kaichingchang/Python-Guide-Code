from random import shuffle
 
class GuessGame:
   def __init__(self, digit=None):
      if digit == None or digit < 3 or digit > 6:
         self.length = 4;
      else:
         self.length = digit;
 
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
 
   def find_number(self, array):
      for i in array:
         if array.count(i) > 1:
            return True      
 
      return False
          
   def ab_counter(self, guess):
      self.a = 0
      self.b = 0
      for i in guess:
         if i in self.answer:
            if guess.index(i) == self.answer.index(i):
               self.a += 1
            else:
               self.b += 1
 
   def run(self):
      self.times = 0
      while True:
         self.times += 1
         guess = list(input(": "))
         if len(guess) != self.length:
            print("Wrong length!!")
            continue
         if self.find_number(guess):
            print("Repeating digits!!")
            continue
         self.ab_counter(guess)
         if self.a == self.length:
            print("Congratulation!!")
            break
         else:
            print(str(self.a) + "A" + str(self.b) + "B")
 
      print("You guess " + str(self.times) + " times.")
       
 
if __name__ == "__main__":  
   g = GuessGame()
   g.run()
  
# 檔名: guessgame.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
