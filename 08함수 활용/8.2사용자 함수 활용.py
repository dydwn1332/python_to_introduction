#8.2.1 소수 여부 판별하기
def is_prime(n):
    prime = True
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                prime = False

    return prime

number = int(input("수를 입력하시오 : "))

if is_prime(number):
    print("소수이다")
else:
    print("소수가 아니다")

#8.2.2 세제곱 합계 구하기

def Three_squares(a):
    sum = 0
    for i in range(1, a + 1):
        b = i * i * i
        sum = sum + b
        print("%d의 3제곱의 합 : %d, 총합계 : %d" %(i, b, sum))
    return sum

print(Three_squares(5))

#C8-2 1~N 홀수의 세제곱 합을 구하라
sum = 0
a = 10
for i in range(1, a + 1):
    if i % 2 != 0:
        b = i * i * i
        sum = sum + b
        print("%d의 3제곱의 합 : %d, 총합계 : %d" %(i, b, sum))

#8.2.3 회문인지 판별하기

def is_palindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True

s = "rotatorr"
for i in range(0, -6, -1):
    print(s[i])
if is_palindrome(s):
    print("%s : 회문" %s)
else:
    print("%s : 회문아님" %s)

#8.2.4 문장 단어 반대로 하기

def reverse_sentence(s):
    words = s.split(" ")
    result = ""
    for word in words:
        result = word + " " + result

    return result

sentence = "nice to meet you"

print(reverse_sentence(sentence))

#8.2.5 문자열 존재여부 판별하기

def string_find(a, b):
    c = 0
    words = a.split(" ")
    for word in words:
        if word == b:
            c = c + 1
    print("찾는 문장 : %s" %a)
    print("찾는 단어 : %s" %b)
    if c == 0:
        print("찾지못했습니다.")
    else:
        print("%s를 %d건 찾았습니다." %(b, c))

a = input("문장을 입력하시오 : ")
b = input('찾을 단어를 입력하시오 : ')
string_find(a, b)

#8.2.6 다수의 문자열 치환하기
def replace_word(string, word_list, word):
    arr = string.split(" ")
    new_arr = list()
    for x in arr:
        if x in word_list:
            new_arr.append(word)
        else:
            new_arr.append(x)

    result = " ".join(new_arr)
    return result

string = "python java php apple orange banana"
word_list = list(["apple", "orange", "banana"])
word = "fruit"
print("문자열 : ", string)
print("단어 리스트 : ", word_list)
print("치환할 단어 : ", word)

new_str = replace_word(string, word_list, word)
print(new_str)

#8.2.7 문자열 위치 이동시키기


def string_move(string, away, movement):
    if away == "left":
        string1 = string[movement:]
        string2 = string[0:movement]
    else:
        string1 = string[len(string) - movement:len(string)]
        string2 = string[movement:]

    result = string1 + string2
    return result

string = "helloworld"
away = "left"
movement = 3
print(string_move(string, away, movement))

#hel loworld