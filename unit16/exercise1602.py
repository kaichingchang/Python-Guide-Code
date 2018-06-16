answer = "1234"
 
def ab_counter(answer, guess, ab):
   a = 0
   b = 0
   for i in guess:
      if i in answer:
         if guess.index(i) == answer.index(i):
            a += 1
         else:
            b += 1
 
   ab[0] = a
   ab[1] = b
 
if __name__ == "__main__":
   guess = input(": ")
   abcounter = [0, 0]
   ab_counter(answer, guess, abcounter)
   if abcounter[0] == 4:
      print("Right!!")
   else:
      print(str(abcounter[0]) + "A" + str(abcounter[1]) + "B")
  
# 檔名: exercise1602.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
