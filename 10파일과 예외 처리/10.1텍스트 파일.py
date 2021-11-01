#10.1.1 텍스트 파일 쓰기
#파일 객체 = open(파일명, 파일모드, 인코딩)
#("r", 읽기모드) ("w" 쓰기모드) ("a" 추가모드)
f = open("new_file.txt", "w", encoding="utf-8")
names = ["홍지수", "안지영", "김연수", "김예린", "한정연"]

for name in names:
    f.write(name)
    f.write("안녕하세요 반갑습니다. \n")

print("파일 쓰기 완료!")
f.close()

f = open("new_file.txt", "a", encoding="utf-8")
names = ["손영만", "임기석"]

for name in names:
    f.write(name + "\n")

f.close()

#10.1.2 텍스트 파일 읽기
f = open("new_file.txt", "r", encoding="utf-8")
lines = f.readlines()

print(lines)


f.close()

print(type(lines))

for line in lines:
    a = line.replace(" ", "\n")
    print(a)

