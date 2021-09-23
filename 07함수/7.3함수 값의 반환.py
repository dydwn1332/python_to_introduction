def fun123(a): #보이는 것과 같이 x값을 리턴하면 파라미터에 어떠한 값을 전달해도 x값을 출력함.
    x = 5
    return x

a = fun123(123)
print(a)

def inch_to_cm(inch):
    cm = inch * 2.54
    return cm

a = inch_to_cm(float(input("몇인치인가요? : ")))
print("%.2f cm입니다." %a)

#C7-5 삼각형의 면적을 계산하라.
def trianglearea(width, height):
    x = width * height * 0.5
    return x

width = float(input("너비를 입력하시오 : "))
height = float(input("높이를 입력하시오 : "))
a = trianglearea(width, height)
print("-삼각형의 너비 : %f\n삼각형의 높이 : %f\n삼각형의 넓이 : %f" %(width, height, a))

a = "python is very easy"
for i in a:
    print(i)
    print()

#7-6함수로 배수의 합계를 구하라
def sum(a):
    sum1 = 0
    for i in range(1, 101):
        if i % a == 0:
            # print("현재값 : %d" %sum1)
            sum1 = sum1 + i
            print("추가된 값 : %d, 합계 : %d" %(i, sum1))

    print("총합 : %d" %sum1)

sum(7)