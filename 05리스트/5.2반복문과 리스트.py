#5.2.1 for문에서 리스트 사용하기

colors = ["빨간색", "파랑색", "초록색", "노랑색", "주황색"]

for i in colors:
    print("나는 %s색을 좋아한다." %i)


n = len(colors)

for i in range(0, 5):
    print("나는 %s색을 좋아한다." %colors[i])

#5.2.2 while문에서 리스트 사용하기

animal = ["사자", "호랑이", "토끼" , "강아지", "고양이"]

i = 0

while i < len(animal):
    print(animal[i])

    i = i + 1

