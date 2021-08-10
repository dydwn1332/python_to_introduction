#3.3.1 if~ 구문의 기본 구조

age = int(input("나이를 입력하세요 :"))
if age >= 65:
    ticket = 0
else:
    ticket = 2000

print("나이 : %d세" %age)
print("입장료 : %d원" %ticket)
#3.3.2 배수 판별하기

num = int(input("양의 정수를 입력하세요 :"))
if num % 3 == 0:
    print("3의 배수이다.")
    if num % 4 == 0:
        print("3의 배수이면서 4의 배수이다.")
if num % 4 == 0:
    print("4의 배수이다.")

#3.3.3 영어 단어 퀴즈 만들기

question1 = input("'사자'를 영어로 작성하시오. :")
if question1 == "lion":
    print("정답")
else:
    print("땡")

question2 = input("'오렌지'를 영어로 작성하시오. :")
if question2 == "orange":
    print("정답")
else:
    print("땡")

question3 = input("'기차'를 영어로 작성하시오. :")
if question3 == "train":
    print("정답")
else:
    print("땡")

#C3-1
start = int(input("시작 수는? "))
end = int(input("끝 수는? "))
num = int(input("정수를 입력하시오 : "))

if num >= start and num <= end:
    print(("%d은(는) %d ~ %d 사이에 있다.") %(num, start, end))
else:
    print(("%d은(는) %d ~ %d 사이에 없다.") %(num, start, end))


#C3-2
month = int(input("월을 숫자로 입력하시오 : "))

if month == 3 or month == 4 or month == 5:
    print("봄")
if month == 6 or month == 7 or month == 8:
    print("여름")
if month == 9 or month == 10 or month == 11:
    print("가을")
if month == 12 or month == 1 or month == 2:
    print("겨울")

#C3-3

a = int(input("주민번호 뒷자리 첫 번째 숫자를 입력하시오 : "))

if a == 1 or a == 3:
    print("남자입니다")
if a == 2 or a == 4:
    print("여자입니다")
