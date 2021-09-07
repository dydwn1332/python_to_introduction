#6.1.1 튜플 생성하기

animals = ("토끼", "거북이", "사자", "여우")
print(animals)
print(type(animals))
numbers = tuple(range(10))
print(numbers)
print(type(numbers))

# animals[2] = "호랑이"
print(animals)

#6.1.2 튜플 요소 추출하기

n = tuple(range(10, 21))
print(n)

print(n[0])
print(n[2:5])
print(n[2:])
print(n[:5])
print(n[-2])
print(n[::-1])

#6.1.3 튜플 길이 구하기
tup1 = tuple(range(10, 51, 10))
print(tup1)

for i in range(len(tup1)):
    print(tup1[i])

#6.1.4 튜플 병합하기

tup1 = (10, 20, 30)
tup2 = (40, 50 ,60)
tup3 = tup1 + tup2
print(tup3)

#6.1.5 튜플에 관리자 정보 저장하기

admin = ("admin", 12345, "webmaster@google.com")

print("관리자 정보")
print("아이디 : %s" %admin[0])
print("비번 : %s" %admin[1])

i = 100
print("%s" %i)

Multiplication_table = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in Multiplication_table:
    print("\n")
    print("-" * 40)
    for j in Multiplication_table:
        print("%d X %d = %d" %(i, j, i * j))