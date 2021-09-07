numbers = [[10, 20, 30,], [40, 50, 60, 70, 80]]

print(numbers[0][0]) #3차원 안됨 해봤음
print(numbers[0][1])
print(numbers[0][2])
print(numbers[1][0])
print(numbers[1][1])
print(numbers[1][2])
print(numbers[1][3])
print(numbers[1][4])

#5.6.2 2차원 리시트와 이중 for문

data = [[10, 20], [20, 30], [40, 50], [60, 70]]
print(type(data[0][0]))

for i in range(len(data)):
    for j in range(len(data[0])):
        print("data[%d][%d] = %d" %(i, j, data[i][j]))

#5.6.3 2차원 리스트로 합계와 평균 구하기

grade = [[60, 70, 80], [10, 20, 30], [40, 50, 50], [80, 90, 100], [10, 5, 10]]
x = 0
q = 0
for i in range(len(grade)):
    for j in range(len(grade[i])):
        x = x + grade[i][j]
        q = x / len(grade[i])
    print("성적합계 : %.2f 평균 : %.2f" %(x, q))
    x = 0

#5.6.4 2차원 리시트로 문자열 다루기

strings = [["원두커피", "라떼", "콜라"], ["우동", "국수", "피자", "파스타"]]

for i in range(len(strings)):
    for j in range(len(strings[i])):
        print(strings[i][j])

#C5-5 리시트로 영어 스펠링 퀴즈를 만들어라

# questions = ["s_hool", "compu_er", "deco_ation", "windo_", "hi_tory"]
# answers = ["c", "t", "r", "w", "s"]
#
# for i in range(len(questions)):
#     answer = input("%s : 밑 줄에 들어갈 알파벳은? " %questions[i])
#     if answer == answers[i]:
#         print("정답입니다")
#     else:
#         print("오답입니다")

#C5-6 리스트로 성적 합계와 평균을 구하라

sum = 0
while True:

    grade = int(input("성적을 입력하시오(-1입력시 종료) : "))
    if grade == -1:
        break
    sum = sum + grade
    i = i + 1

avg = sum / i
print("합계 : %d, 평균 : %d" %(sum, avg))

#5-7