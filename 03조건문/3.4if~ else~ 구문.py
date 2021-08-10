# x = int(input("숫자를 입력하시오 : "))
#
# if x%2 == 0:
#     print("양수입니다")
# else:
#     print("음수입니다")
#
# #3.4.1 자격증 시험 합격/불합격 판정하기
#
# pilgi = int(input("필기점수를 입력하시오 : "))
# silgi = int(input("실기점수를 입력하시오 : "))
#
# if pilgi >= 60 and silgi >= 60:
#     result = "합격"
# else:
#     result = "불합격"
#
# print("-필기시험 점수 : %d" %pilgi)
# print("-실기시험 점수 : %d" %silgi)
# print("판정 : %s" %result)
#
# #3.4.2 영어 소문자 자음/모음 판별하기
#
# char = input("영어 소문자를 입력하시오 : ")
#
# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("%s 은(는)모음이다 ." %char)
# else:
#     print("%s 은(는)자음이다." %char)
#
# #C3-4
# a = "apple"
# b = a.upper()
# print(b)

#C3-5다이어트 필요성을 판정하라!

tall = int(input("키를 입력하시오 : "))
weight = int(input("몸무게를 입력하시오 : "))

tall2 = tall / 100

tall3 = tall2 * tall2

BMI = weight / tall3

print(tall)
print(weight)

if BMI < 18.5:
    print("BMI:%.2f 저체중" %BMI)
elif BMI > 18.5 and BMI < 23:
    print("BMI:%.2f 정상" %BMI)
elif BMI > 23 and BMI < 25:
    print("BMI:%.2f 과체중" %BMI)
else:
    print("BMI:%.2f 비만" %BMI)

#C3-6아르바이트 급여를 계산하라!

Hourly_wage = int(input("시급을 입력하시오. : "))
hour = int(input("일한시간을 입력하시오. : "))
night = int(input("일한시간에서 야간시간이 있다면 입력하시오(없으면 0). : "))

Day_wage = Hourly_wage * hour + (Hourly_wage * 0.5 * night)

print("시급: %d." %Hourly_wage)
print("일한시간: %d." %hour)
print("일급: %d." %Day_wage)

