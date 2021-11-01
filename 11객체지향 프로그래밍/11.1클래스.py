#객체지향 프로그래밍(Object-Oriented Programming)은 클래스를 정의하고 클래스가 정의되면
#객체(Object)를 생성하고 이 객체를 이용하여 프로그램을 작성한다.

#11.1.1 클래스란?
#클래스는 속성(Attribute)과 메소드(Method)로 구성된다.
class print1:
    def print(self):
        print("안녕하시요")

a = print1()
a.print()

class Person:
    name = "김정연"
    def hello(self):
        print(Person.name + "님 안녕하세요")

person1 = Person()
person1.hello()

Person.name = "황서영"
person1.hello()

#클래스 : 속성과 메소드로 구성되는 객체 생성에 사용되는 틀이다.
#객체 : 클래스로부터 생성되어 해당 클래스의 속성과 메소드를 가진다.
#속성 : 클래스와 객체 내부에서 사용되는 변수를 의미한다.
#메소드 : 클래스와 객체 내부에서 사용되는 함수를 의미한다.

class Cat:
    kor_name = "야옹"
    eng_name = "miyaong"
    age = 2

    def sound(self):
        print("야옹~~")
    
    def speed(self):
        print("빠르다")

mycat = Cat()

mycat.sound()
print(mycat.kor_name)
print(mycat.eng_name)
print(mycat.age)
mycat.speed()

#11.1.2 매개변수 self
#클래스의 메소드에서 사용되는 매개변수 self는 객체에서 메소드를 호출할 때 해당 객체를
#전달받는 데 사용된다. 다음 예제를 통하여 매개변수 self의 사용법을 익혀보자.
class Members:
    def set_info(self, name):
        self.name = name

    def show_info(self):
        print("이름 : ", self.name)

member1 = Members()
member1.set_info("홍준표")
member1.show_info()