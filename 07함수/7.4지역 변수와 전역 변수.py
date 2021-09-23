#7.4.1 지역변수
def func():
    x = 100  #지역변수는 해당 지역, 즉 func()함수의 영역에서만 사용 가능하다.
    print(x)

func()
# print(x) #안됨.

#7.4.2 전역변수

def func2():
    print(x)

x = 100
func2()
print(x)

def func3():
    x = 200
    print(x)

func3()
print(x)

#7.4.3 키워드 global

def GloBal():
    global x
    x = 300
    print(x)

x = 100
print(x)
GloBal()
print(x)

def cir_area():
    global r
    result = r * r * 3.14
    return result

def cir_length():
    global r
    result = 2 * 3.14 * r
    return result

r = 10
area = cir_area()
length = cir_length()
print("면적 : %.2f, 원주의 길이 : %.2f" %(area, length))

# def wiw():
#     global a
#     a = 100
#
# wiw()
# print(a)

def prime_num(a, b):
    asdf = list()
    for j in range(a, b + 1):
        q = 0
        for i in range(2, j - 1):
            if j % i == 0:
                q = 1
        if q == 1:
            continue
        print(j, end=" ")
        asdf.append(j)
    print(asdf)
prime_num(10, 50)

#s7-2 딕셔너리를 이용해서 영어단어 맞추기 프로그램

eng_dict = {"house":"집", "paino":"피아노", "friend":"친구"}
for i in eng_dict:
    a = input("%s를 한글로 작성하시오 : " %i)
    if a == eng_dict[i]:
        print("정답")
    else:
        print("오답")

#s7-3 자연수를 입력받아 1부터 그자연수까지의 정수의 제곱을 구하라

sum1 = []
a = 10
for i in range(1, a + 1):
    j = i * i
    sum1.append(j)

print(sum1)

