#2.3.1 문자열의 추출
s = '안녕하세요. 반갑습니다.'
print(s[0])

print (s[1])

print(s[3:10])

#2.3.2 문자열 연결 연산자
name = "김정수"
hello = "안녕하세요!"
print(name + "님" + hello)

score = 80
# print("성적: " + score)

print("성적: " + str(score))

#2.3.3문자열 반복 연산자
x = "토끼" * 10
print(x)

date = "20220301"
year = date[0:4]
month = date[4:6]
day = date[6:]
date2 = year + "-" + month + "-" + day
print(date2)

#2.3.4 문자열 길이 구하기
x = "가는 말이 고와야 오는 말이 곱다."
n = len(x)
print("문자열의 길이: " + str(n))

x = "말 한마디로 천냥 빚을 갚는다."
print(len(x))

x = "-" * 10
y = '거북이'
print(len(x + y))

x = "apple" + str(123)
y = "-" * 10 + "=" * 20
print(len(x + y))

#2.3.5 문자열 포맷팅

animal = "고양이"
x = "나는 %s를 좋아합니다." %animal
print(x)

age = 25
print("내 나이는 %d살 입니다." % age)

kor = 88
eng = 95
math = 97
sum = kor + eng + math
avg = sum/3
print("합계: %d, 평균: %.2f" %(sum, avg))
