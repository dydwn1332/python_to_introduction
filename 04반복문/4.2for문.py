##4.2.1 for문의 기본 구조

#sum = 0

#for i in range(1, 11):
#    sum = sum + i
#    print("i의 값 : %d => 합계 : %d" %(i, sum))

##4.2.2 range() 함수

#for i in range(10):
#    print(i, end =" ")
#print()
#for i in range(1, 11):
#    print(i, end = " ")
#print()
#for i in range(1, 20, 2):
#    print(i, end = " ")
#print()
#for i in range(20, 0, -2):
#    print(i, end = " ")

##4.2.3 5의 배수 합계 구하기

#sum = 0
#for i in range(100, 201, 5):
#    sum = sum + i
#print()
#print("5의 배수의 합계 : %d" %sum)

#sum = 0
#for i in range(100, 201):
#    if i%5 == 0:
#        sum = sum + i
#print()
#print("5의 배수의 합계 : %d" %sum)

##4.2.4 for문에서 문자열 다루기

#word = input("문자를 입력하시오 : ")

#for x in word:
#    print(x)

#phone = input("하이픈(-)을 포함한 휴대폰 번호를 입력하시오 : ")

#for x in phone:
#    if x != "-":
#        print("%s" %x, end ="")

##4.2.5 온도 환산표 만들기

#print("화씨 섭씨 온도 환산기@@")
#print("1.화씨 -> 섭씨")
#print("2.섭씨 -> 화씨")
#choice = float(input("환산할 것을 선택하시오(1/2) : "))

#if choice == 1:
#    fahrenheit = float(input("화씨 온도를 입력하시오 : "))
#    celsius = (fahrenheit - 32) * 5/9
#    print("화씨%d 에서 섭씨%d로 변환되었습니다." %(fahrenheit, celsius))
#else:
#    celsius = float(input("섭씨 온도를 입력하시오 : "))
#    fahrenheit = celsius *9/5 + 32
#    print("섭씨%d 에서 화씨%d로 변환되었습니다." %(celsius, fahrenheit))

#C4-1 for문으로 5의 배수가 아닌 수를 출력하라!
count = 0

for i in range(200, 800):
    if i % 5 != 0:
        print(i, end =" ")
        count = count + 1
        if count % 10 == 0:
            print()

#C4-2 for문으로 길이 환산표를 만들어라!

print("-" * 40)
print("\tcm\tmm\tm\tinch")
print("-" * 40)

for cm in range(101):
    mm = cm * 10.0
    m = cm * 0.01
    inch = cm * 0.3937
    print("\t%.2f\t%.2f\t%.2f\t%.2f" %(cm, mm, m, inch))

#4-3 for문으로 별표트리를 만들어라

for i in range(1, 10):
    print("%d" %i * i)
    print()

for i in range(9, 0, -1):
    print("%d" %i * i)
    print()