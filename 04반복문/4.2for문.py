#4.2.1 for문의 기본 구조

sum = 0

for i in range(1, 11):
    sum = sum + i
    print("i의 값 : %d => 합계 : %d" %(i, sum))

#4.2.2 range() 함수

for i in range(10):
    print(i, end =" ")
print()
for i in range(1, 11):
    print(i, end = " ")
print()
for i in range(1, 20, 2):
    print(i, end = " ")
print()
for i in range(20, 0, -2):
    print(i, end = " ")

#4.2.3 5의 배수 합계 구하기

sum = 0
for i in range(100, 201, 5):
    sum = sum + i
print()
print("5의 배수의 합계 : %d" %sum)

sum = 0
for i in range(100, 201):
    if i%5 == 0:
        sum = sum + i
print()
print("5의 배수의 합계 : %d" %sum)

#4.2.4 for문에서 문자열 다루기

word = input("문자를 입력하시오 : ")

for x in word:
    print(x)