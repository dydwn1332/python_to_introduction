area_code = {"서울": "1", "부산": "2", "대구": "3", "광주": "4"}

for i in area_code:
    print("%s의 지역번호 : %s" %(i, area_code[i]))
    print(area_code.keys())

#6-2 딕셔너리로 성적 평균을 구하라
sum = 0
score = {"김": "50", "병": "20", "갑": "40", "을": "80", "정": "90"}
for i in score:
    print("%s의 성적 : %s" %(i, score[i]))
    sum = sum + int(score[i])

x = len(score)
avg = sum / x
print("합계 : %d, 평균 : %d" %(sum, avg))

#6-3딕셔너리로 정보 접근을 제어하라
while True:
    admin_info = {"adress": "dydwn1332", "password": "qprk1332"}

    adress = input("아이디를 입력하시오 : ")
    password = input("비번을 입력하시오 : ")

    if admin_info["adress"] == adress and admin_info["password"] == password:
        print("아이디 또는 비번이 맞았습니다")
        break
    else:
        print("아이디 또는 비번이 틀렸습니다")
