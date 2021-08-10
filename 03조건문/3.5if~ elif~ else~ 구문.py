#3.5.1 점수에 따라 등급 판정하기

score = int(input("점수는? : "))

if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
elif score >= 60:
	grade = "D"
else:
	grade = "F"

print("등급 : %s." %grade)

#3.5.2 간단 계산기 만들기

print("기능 선택")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기\n\n")

Select_function = int(input("계산기 기능을 선택하시오.(1/2/3/4) : "))

num1 = int(input("첫번째 숫자를 입력하시오. : "))
num2 = int(input("두번째 숫자를 입력하시오. : "))

if Select_function == 1:
	print("%d + %d = %d" %(num1, num2, num1 + num2))
elif Select_function == 2:
	print("%d - %d = %d" %(num1, num2, num1 - num2))
elif Select_function == 3:
	print("%d * %d = %d" %(num1, num2, num1 * num2))
elif Select_function == 4:
	print("%d / %d = %.2f" %(num1, num2, num1 / num2))
else:
	print("잘못입력되었습니다.")
