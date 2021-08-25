#5.4.1 리스트 병합하기

person1 = [1, 2, 3]
person2 = [4, 5, 6]

person = person1 + person2

print(person)

#5.4.2 리스트 합계 구하기

score = [80, 90, 95, 100]

sm = sum(score)
avg = sm / len(score)

print("합계 : %d" %sm)
print("평균 : %d" %avg)

#5.4.3 리스트 순서 반대로 하기

#리스트에서 요소들의 순서를 반대로 할 때에는 리스트위 reverse() 메소드를 이용한다.

data = [10, 20, 30, 40, 50]
print(data)

data.reverse()
print(data)
#data.reverse()는 실행 결과에 나타난 것과 같이 리스트 요소들의 순서를 거꾸로 만든다.

#5.4.4 리스트 복사하기

fruits = ["apple", "banana", "orange"]
print(fruits)

x = fruits.copy()
print(x)

b = fruits
print(b)

#5.4.5 리스트 정렬하기

data = [1, 3, 5, 2, 4, 6, -1, -3]
print(data)

data.sort()
print(data)

data.sort(reverse=True)
print(data)