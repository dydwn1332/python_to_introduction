#9.1.1 모듈 생성하고 불러오기
import hello

hello.greet1("erun")
hello.greet2("erun")

#9.1.2 import ~ 구문
import calc

x = calc.add(10, 20)
print(x)

y = calc.sub(10, 20)
print(y)

#9.1.3 import ~ as ~ 구문
import calc as c

x = c.add(100, 10)
print(x)
y = c.sub(100, 10)
print(y)

#9.1.4 from ~ import ~ 구문
from calc import add, sub

x = add(100, 200)
print(x)

y = sub(100, 200)
print(y)
