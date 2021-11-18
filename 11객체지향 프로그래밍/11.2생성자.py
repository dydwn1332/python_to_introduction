#생성자(Constructor)는 __init__()메소드를 의미하는데 이것은 객체를 생성할 때 자동으
#로 호출되어 객체를 초기화하는 데 사용된다.
class Members:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("이름 :", self.name)
        print("나이 :", self.age)
        print(type(self.name))
        print(type(self.age))

member1 = Members("정용주", 22)
member1.show_info()

# print(type(member1.show_info(name)))

#C11-1객체지향으로 원의 면적을 구하라!
import math

class Circle:
    def radius(self, r):
        self.r = r

    def get_area(self):
        result = math.pi * self.r * self.r
        return result

    # def Print(self):
    #     print("반지름 : %f", %self.r)
radius1 = float(input("반지름을 입력하시오 : "))

circle1 = Circle()

circle1.radius(radius1)

print("반지름 : %f" %radius1)
print("원의 면적 : %f" %circle1.get_area())

#C11-2객체지향으로 성적의 평균을 구하라!

class Scores:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def get_avg(self):
        sm = self.kor + self.eng + self.math
        avg = sm / 3.0
        return avg

s1 = Scores("정용주", 80, 70, 90)

print("이름 : %s" %s1.name)
print("국어 : %d, 영어 : %d, 수학 : %d" %(s1.kor, s1.eng, s1.math))
print("평균 : %.2f" %s1.get_avg())
