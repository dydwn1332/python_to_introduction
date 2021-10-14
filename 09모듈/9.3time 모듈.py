#time.time() UTC 표준시를 기준으로 한 현재 시간 구함
#time.gmtime() UTC 초 단위의 시간을 struct_time 구조로 반환함
#time.localtime() 현재 시간(Local Time)을 구함
#time.ctime() UTC 초 단위의 시간을 문자열로 변환함
#time.strftime() 일시를 포맷 기호를 이용하여 특정 포맷으로 변환함
#time.sleep() 일정 시간만큼 지연시킴

#9.3.1 현재 시간 구하기
import time

seconds = time.time()

print(seconds)

print(time.gmtime(seconds))

a = time.gmtime(seconds)
b = time.localtime(seconds)

print(a.tm_year)
print(a.tm_mon)
print(a.tm_mday)
print(a.tm_hour)
print(a.tm_min)
print(a.tm_sec)

print(b.tm_year)
print(b.tm_mon)
print(b.tm_mday)
print(b.tm_hour)
print(b.tm_min)
print(b.tm_sec)

#9.3.2 타임스탬프를 문자열로 변환하기
string = time.ctime(time.time())
print(string)

#9.3.3 시간을 특정 포맷으로 변환하기
tm = time.localtime(time.time())
string = time.strftime("%Y-%m-%d %I:%M:%S %p", tm)
print(string)

#9.3.4 시간 지연시키기
print("시작?")
# time.sleep(5)
print("5초 후에 나타남")

#9.3.5 프로그램 실행 시간 측정하기
def func():
    sum = 0
    for i in range(1, 10000000):
        sum = sum + i
        # print(sum)
start = time.time()
func()
end = time.time()

print("소요시간 :", end - start)