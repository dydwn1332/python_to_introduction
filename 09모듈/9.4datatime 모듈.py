#9.4.1 날짜와 시간에 대한 산술 연산
import datetime
time1 = datetime.timedelta(days= 3, hours= 3, minutes= 30, seconds= 30)
time2 = datetime.timedelta(days= 5, hours= 5, minutes= 40, seconds= 50)
print(time2 - time1)

# 9.4.2 오늘의 날짜 구하기
today = datetime.date.today()
print(today)

# 9.4.3 일주일 후의 날짜 구하기
today = datetime.date.today()
week = datetime.timedelta(weeks= 1)

next_Week = today + week
print(next_Week)

#9.4.4 현재의 날짜와 시간 구하기
from datetime import datetime
a = datetime.now()

print("%s" %today.year)
print("%s" %today.month)
print("%s" %today.day)
# print("%s" %today.hour)
# print("%s" %today.minute)
# print("%s" %today.second)
