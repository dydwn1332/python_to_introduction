#9.6.1 게임 시작 시간 표시하기
import random
import time

current_time = time.time()
current_time2 = time.localtime(time.time())
current_time3 = time.localtime()

print(current_time)
print(current_time2)
print(current_time3)

print("게임 시작 시간 : ", time.strftime("%I:%M:%S %p", current_time3))
#9.6.2 주사위 던지기
print("본 게임은 주사위 던지기 게임입니다.")
input("다음으로 가려면 Enter를 입력하시오...")
print("게임방법은 플레이어와 컴퓨터가 임의의 주사위를 던져 숫자가 높은 쪽이 승리합니다.")
input("다음으로 가려면 Enter를 입력하시오...")
input("게임을 진행하려면 Enter를 입력하시오...")

A = "y"
while A == 'y':      
    print("주사위를 던지는 중...")
    time.sleep(random.random())
    print("주사위를 던지는 중...")
    time.sleep(random.random())
    print("주사위를 던지는 중...")
    time.sleep(random.random())

    me = random.randint(1, 6)
    computer = random.randint(1, 6)
    print("나의 주사위 : %d" %me)
    print("컴퓨터의 주사위 : %d" %computer)

    #9.6.3 승부 판정하기

    if me > computer:
        print("나의 승리")
    elif me < computer:
        print("컴퓨터의 승리")
    else:
        print("무승부")

    print("-" * 50)

    A = input("계속 하시겠습니까?(y/n) : ")
    if A != "y":
        break

print("게임이 종료되었습니다.")
