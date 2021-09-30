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

