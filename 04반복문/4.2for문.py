#4.2.1 for문의 기본 구조

sum = 0

for i in range(1, 11):
    sum = sum + i
    print("i의 값 : %d => 합계 : %d" %(i, sum))

#4.2.2 range() 함수

for i in range(10):
    print(i, end =" ")
