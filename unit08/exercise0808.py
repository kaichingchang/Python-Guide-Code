def fibonacci(n):
   n1 = 0
   n2 = 1
   i = 3
   while i <= n:
      n3 = n1 + n2
      n1 = n2
      n2 = n3
      i += 1
 
   return n3
 
n = int(input("n: "))
print(fibonacci(n))
   
# 檔名: exercise0808.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
