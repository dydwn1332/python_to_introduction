#5.5.1 문자열 찾기

string1 = "Python is fun!"
print(string1)

x = string1.find("fun")
print(x)

#5.5.2 문자열 치환하기

string = "사과는 맛있다. 나는 사과를 좋아한다"
print(string)

string.replace("사과", "바나나")
print(string)

phone1 = "010-6295-3150"
print(phone1)

phone2 = phone1.replace("-", "")
print(phone2)