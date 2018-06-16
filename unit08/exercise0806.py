def factorial(n):
   i = 1
   p = 1
   while i <= n:
      p *= i
      i += 1 
    
   return p
 
n = int(input("n: "))
print(factorial(n))
  
# 檔名: exercise0806.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
