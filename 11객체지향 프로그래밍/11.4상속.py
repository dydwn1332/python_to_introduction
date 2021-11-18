#11.4.1 상속의 개념
class Parent:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(self.name)

class Child(Parent):
    pass

class Child2(Child):
    pass

a = Child("홀리")
a.print()

b = Child2("몰리")
b.print()

#11.4.2 부모 클래스 생성자 호출

class Person:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)
    def print_age(self):
        print(self.age)

class Student(Person):
    def __init__(self, name, age):
        # super().__init__(name)
        self.name = name
        self.age = age

x = Student("정용주", 12)
x.print_age()
x.print_name()