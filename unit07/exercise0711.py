n1 = 0
n2 = 1
i = 3
end = int(input("f: "))
while i <= end:
   n3 = n1 + n2
   n1 = n2
   n2 = n3
   i += 1
print(n3)
  
# 檔名: exercise0711.py 
# 作者: Kaiching Chang 
# 時間: July, 2014
