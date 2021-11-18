#클래스 속성은 말 그대로 클래스에 소속되어 있기 때문에 해당 클래스에서 파생된 하위 객
#체들에서 속성 값이 공유된다는 점을 꼭 기억하자.
class Student:
    pet = []
    def push_pet(self, x):
        self.pet.append(x)

john = Student()
john.push_pet("고양이")
print(john.pet)

sally = Student()
sally.push_pet("개")
print(sally.pet)

#11.3.2 인스턴스 속성
#인스턴스 속성은 해당 클래스에 의해 생성된 인스턴스에서만 유효한 값을 가진다.
#인스턴스 속성은 객체마다 속성 값이 다르다.
class Student2:
    def __init__(self): #생성자
        self.pet = []

    def push_pet(self, x):
        self.pet.append(x)

john = Student2()
john.push_pet("고양이2")
print(john.pet)

sally = Student2()
sally.push_pet("개2")
print(sally.pet)
