data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

x = 15
a = int(len(data)/2)
for i in range(0, len(data)):
    a = int(a)
    if x == data[a]:
        print("찾으시는 숫자는 %d번 요소입니다. " %a)
        break
    elif x > data[a]:
        a = (a + len(data)) / 2
    else:
        a /= 2

#E8-1 키보르로 입력 받은 수가 짝수인지 홀수인지를 판별하는 프로그램을 작성하시오.
def dis_number(a):
    if a % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")

dis_number(15)

#S8-1 선형 탐색을 이용하여 다음의 리스트에서 키보드가 입력 받은 수가 존재하는지를 판별
data = [1,2,3,4,5,6,7,8,9,10]

def panqwe(x):
    a = 0
    for i in range(0, len(data)):
        if x == data[i]:
            print("%d는 %d번 요소에 존재합니다." %(x, i))
            a = 1
    if a == 0:
        print("%d는 존재하지 않습니다." %x)
i = 0
while i < 100:
    panqwe(i)
    i += 1