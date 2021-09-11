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

even_odd(int(input("숫자를 입력하시오 : ")))

#7.2.4 매개변수 *args

