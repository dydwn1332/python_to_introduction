#5.3.1 리스트 요소 수정하기

flowers = ["목련", "벚꽃", "장미", "백일홍"]

print(flowers)

flowers[1] = "무궁화"
print(flowers)

#5.3.2 리스트 요소 추가하기
 
#arr = [5, 1, 2, 3, 4]
#print(arr)

#arr.append(10)
#print(arr)

#scores = []

#while true:
#    score = int(input("성적을 입력하시오(종료 : -1) : "))

#    if score == -1:
#        break
#    else:
#        scores.append(score)

#print(scores)

#5.3.3 리스트 요소 삽입하기

fruits = ["apple", "orange", "banan", "cherry"]
print(fruits)

fruits.insert(1, "melon")
print(fruits)

fruits.insert(2, "strawberry")
print(fruits)

#5.3.4 리스트 요소 위치 찾기

number = [1, 2, 3, 4, 5, 6, 7]
print(number)

idx = number.index(5)
print(idx)

#5.3.5 리스트 요소 삭제하기

member = ["홍지웅", 20, "경기도", "김포시", "dydwn1332@naver.com"]
print(member)

member.remove("홍지웅")
print(member)

data = [10, 20, 30, 40, 50, 60]
print(data)

x = data.pop(1)
print(x)
print(data)

data.clear()
print(data)

#C5-1 1~20의 양의 정수 리스트를 생성하라!

data = list(range(1, 21))

print(data)

for i in range(0, len(data)):
    print("%d" %data[i], end=" ")
   
#5-2 짝수 번쨰 요소를 출력하라!

print()
for i in range(1, len(data) + 1):
    if i % 2 == 0:
        print(i, end=" ")

    i = i + 1

print()
for i in range(1, len(data) + 1):
    if i % 2 != 0:
        print(i, end=" ")

    i = i + 1

#C5-4

data = []

for i in range(10, 21):
    data.append(i)

print(data)