answer = "1234"
 
def test(p1, p2):
   if p1 == p2:
      return True
   else:
      return False
 
if __name__ == "__main__":
   guess = input(": ")
   if test(guess, answer):
      print("Right!!")
   else:
      print("Wrong!!")
  
# 檔名: exercise1601.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
