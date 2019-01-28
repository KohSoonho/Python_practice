# 10-1
import datetime
with open("today.txt", "w") as file :
    today = datetime.date.today()
    file.write(today.isoformat())

# 10-2
with open("today.txt", "r") as file :
    today_string = file.read()

print(today_string)

# 10-3
import time
format = "%Y-%m-%d"

print(time.strptime(today_string, format))

# 10-4
import os
print(os.listdir("."))

# 10-5
print(os.listdir(".."))

# 10-6
# write in multi_times.py

# 10-7
my_day = datetime.date(1988, 12, 11)
print(my_day)

# 10-8
print(my_day.weekday())      # 0 == Monday
print(my_day.isoweekday())   # 1 == Monday, 7 == Sunday

# 10-9
party_day = my_day + datetime.timedelta(days = 10000)
print(party_day)
