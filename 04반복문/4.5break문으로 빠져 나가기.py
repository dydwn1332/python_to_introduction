for i in range(1, 1001):
    print(i)

    if i == 10:
        break

#C4-9 while문으로 홀수의 누적 합계를 구하라.

a = 1
b = 0
c = 0

while a <= 100:
    if a % 2 != 0:
        b = b + a
        print("%4d" %b, end=" ") # %d사이에 숫자를 넣으면 출력할 때 그 숫자만큼 자리를 할당함.


    a = a + 1
    if b % 10 == 0:
        print()

#C4-11 while문으로 영어 문장을 역순으로 출력하라!

#sentense = input("문장을 입력 하시오 : ")

#print(sentense[2])

#i = len(sentense) - 1

#print(i)

#while i >= 0:
#    if sentense[i] == " ":
#        print("-", end="")
#    else:
#        print("%s" % sentense[i], end="")

#        i = i - 1

#심화문제
count = 0
i = 1
while i <= 1000:
    if i % 3 != 0:
        print("%3d" %i, end=" ")
        count = count + 1
    if count % 10 == 0:
        print()
    i = i + 1

print("\n\n")

count = 0
line = 0

startnum = int(input("시작 수를 입력하시오 : "))
endnum = int(input("끝 수를 입력하시오 : "))

for i in range(startnum, endnum):
    for nanu in range(1, i + 1):
        if i % nanu == 0:
            count = count + 1
    if count == 2:
        print("%4d" %i, end=" ")
        line = line + 1
        if line % 10 == 0:
          print()
    count = 0