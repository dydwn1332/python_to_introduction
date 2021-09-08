#6.3.1 딕셔너리에 요소 추가하기
scores = {"Kor": "90", "eng": "89", "math": "98"}
print(scores)

scores["music"] = ("100")
print(scores)

#6.3.2 딕셔너리 요소 수정하기
words = {"door": "문", "chair": "의자", ".table": "책상", "house": "집"}
print(words)

words[".table"] = "테이블"
print(words)

words["house"] = ("하우스")
print(words)

#6.3.3 딕셔너리 요소 삭제하기
x = words.pop(".table")

print(x)

print(words)

words.clear()

print(words)
