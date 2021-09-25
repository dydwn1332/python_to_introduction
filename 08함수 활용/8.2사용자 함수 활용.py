#8.2.1 소수 여부 판별하기
def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime = False

    return prime

number = int(input("수를 입력하시오 : "))

if is_prime(number):
    print("소수이다")
else:
    print("소수가 아니다")

#8.2.2 세제곱 합계 구하기

def Three_squares(a):
    sum = 0
    for i in range(1, a + 1):
        b = i * i * i
        sum = sum + b
        print("%d의 3제곱의 합 : %d, 총합계 : %d" %(i, b, sum))
    return sum

print(Three_squares(5))

#C8-2 1~N 홀수의 세제곱 합을 구하라
sum = 0
a = 10
for i in range(1, a + 1):
    if i % 2 != 0:
        b = i * i * i
        sum = sum + b
        print("%d의 3제곱의 합 : %d, 총합계 : %d" %(i, b, sum))
