import re

str = "There is no spoon."

v1 = re.sub(r"a", "e", str)
v2 = re.sub(r"e", "i", v1)
v3 = re.sub(r"i", "o", v2)
v4 = re.sub(r"o", "u", v3)
v5 = re.sub(r"u", "a", v4)

print(v5)

# 檔名: library_demo2.py 
# 作者: Kaiching Chang
# 時間: July, 2014
