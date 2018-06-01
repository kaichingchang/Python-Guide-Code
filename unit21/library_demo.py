import datetime

now = datetime.datetime.now()
year = datetime.date.today().strftime("%Y")
month = datetime.date.today().strftime("%B")
wday = datetime.date.today().strftime("%A")

print("Current date and time: ", now)
print("Current year: ", year)
print("Month of the year: ", month)
print("Day of the week: ", wday)

# 檔名: library_demo.py
# 作者: Kaiching Chang
# 時間: July, 2014
