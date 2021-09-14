#7.2.1 매개변수란?
def say_hello(name):
    print("%s님 안녕하세요" %name)

say_hello("김지윤")

#7.2.2 매개변수와 인수

def print_name(first_name, last_name):
    name = first_name + last_name
    print("이름 : %s" %name)

print_name("정", "용주")

#7.2.3 매개변수의 유효 범위
def even_odd(n):
    if n % 2 == 0:
        print("%d는 짝수이다" %n)
    else:
        print("%d는 홀수이다" %n)

# even_odd(int(input("숫자를 입력하시오 : ")))

#7.2.4 매개변수 *args

def average(*args):
    num = len(args)
    sum = 0
    for i in range(num):
        sum = sum + args[i]
    avg = sum / num
    print("합계 : %d" %sum)
    print("평균 : %d" %avg)

average(10, 20, 30)

#7.2.5매개변수에 리스트 전달하기

def fruitss(food):
    for i in food:
        print(i)


fruit = ["바나나", "딸기", "사과"]
fruitss(fruit)


def foodadd(food):
    food.append("멜론")
    food.append("수박")

print(fruit)
foodadd(fruit)
print(fruit)

#C7-1 두수의 합
def add(a, b):
    c = a + b
    print("%d + %d = %d" %(a, b, c))

add(10, 20)
add(123, 412)

#C7-2 두 정수 사이의 모든 수 합

def alladd(first, last):
    sum = 0
    for i in range(first, last + 1):
        sum = sum + i

    print("%d ~ %d 의 합계 : %d" %(first, last, sum))

alladd(1, 50)
alladd(20, 50)

#7-4 리스트값을 곱한 후 저장
# def listsave(list1, a):
#     list2 = list()
#     for i in list1:
#         b = i * a
#         list2.append(b)
#     list1 = list2

def listsave(list1, a):
    for i in range(len(list1)):
        list1[i] = list1[i] * a

result = [10, 20, 30, 40]
listsave(result, 10)
print(result)


