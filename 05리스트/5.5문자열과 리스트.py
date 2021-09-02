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

phone2 = phone1.replace("-", "")    #phone1에 replace메소드를 사용하여 "-"(하이픈)을 ""(NULL)로
print(phone2)                       #변경 phone2는 하이픈이 없는 숫자만을 가지는 문자열이됨.

#5.5.3 문자열 쪼개기

hello = "have a nice day"
print(hello)

list1 = hello.split(" ")
print(list1)
print(type(list1))

for i in range(0, len(list1)):
    print("list1[%d] : %s" %(i, list1[i]))

#5.5.4 리스트 문자열로 변환하기

name = ["황예린", "홍지수", "안지영"]
print(name)
print(type(name))

x =" ".join(name)
print(x)
print(type(x))

phone1 = ["010", "6295", "3150"]
print(phone1)

phone2 = "".join(phone1)
print(phone2)

phone3 = int(phone2)
print(phone3)

#5.5.5 리스트 문자열에서 하이픈 삭제하기

phone_list1 = ["010-1234-1234", "010-4321-4321", "010-6295-3150"]
print(phone_list1)

phone_list2 = []
for i in phone_list1:
    x = i.replace("-", "")

    phone_list2.append(x)

print(phone_list2)

#5.5.6 리스트에서 문자열 치환하기

sentence = ["Love me, love my dog", "No news is good news.",
            "Blood is thicker than water"]
print(sentence)
# x = sentence.replace(" ", "")
# print(x)

for sentences in sentence:
    x = sentences.replace(" ", "_")
    print(x)