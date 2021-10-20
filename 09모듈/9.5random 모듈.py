#random.random() 함수 0 ~ 1사이에 있는 임의의 실수를 반환하다.
import random

# while True:

print("random() : ", random.random())
print("random() : ", random.random())

#random.uniform() 함수 주어진 두 수 사이의 임의의 실수 값을 반환한다.
print("uniform(1, 10) :", random.uniform(1, 10))
print("uniform(1, 10) :", random.uniform(1, 10))

#random.randint() 함수 두 수 사이에 있는 임의의 정수를 반환한다.

print("randint(1, 6) : ", random.randint(1, 6))
print("randint(1, 6) : ", random.randint(1, 6))

#random.choice() 함수 리스트, 튜플, 문자열의 요소 중 임의의 요소 값을 반환한다.

a = [1, 2, 3, 4, 5, 6]
b = "python"
print("random.choice : ", random.choice(a))
print("random.choice : ", random.choice(b))

#random.shuffle() 함수 리스트 요소들의 순서를 임의로 섞는다.
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("원래 리스트 : ", list)
random.shuffle(list)
print("바뀐 리스트 : ", list)