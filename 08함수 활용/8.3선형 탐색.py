data = [-5, -1, 2, 6, 8, 12, 29]

def find_max(data):
    max = data[0]
    for i in range(1, len(data)):
        if data[0] < data[i]:
            max = data[i]

    return max

print(find_max(data))

a = input("숫자를 입력하시오 : (공백으로 구분함)")
b = a.split(" ")

#C8-6 선형 탐색으로 최솟값을 찾아라!

def find_min(a):
    result = a[0]
    for i in range(0, len(a)):
        if result > a[i]:
            result = a[i]

    return result

data = [19, 12, 9, 6, 4, 1, -1, -5, -18]

print(find_min(data))