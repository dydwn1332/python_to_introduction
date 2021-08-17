a = 2
for b in range(1, 10):
    print("%d x %d = %d" %(a, b, a*b))


print("-" * 50)

for a in range(1, 10):
    for b in range(1, 10):
        print("%d x %d = %d" %(a, b, a*b))
    print("-" * 50)

#C4-7 이중 for문으로 사각형 형태를 만들어라.

for i in range(0, 11):
    for j in range(0, 11):
        print("ㅁ", end=" ")
    print()

#C4-8 이중 for문으로 역삼각형 형태의 숫자를 만들어라!

for i in range(10, 0, -1):
    for h in range(i):
        print("%d" %i, end=" ")
    print()
