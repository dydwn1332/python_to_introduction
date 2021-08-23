#5.3.1 리스트 요소 수정하기

flowers = ["목련", "벚꽃", "장미", "백일홍"]

print(flowers)

flowers[1] = "무궁화"
print(flowers)

#5.3.2 리스트 요소 추가하기
 
arr = [5, 1, 2, 3, 4]
print(arr)

arr.append(10)
print(arr)

scores = []

while True:
    score = int(input("성적을 입력하시오(종료 : -1) : "))

    if score == -1:
        break
    else:
        scores.append(score)

print(scores)

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
