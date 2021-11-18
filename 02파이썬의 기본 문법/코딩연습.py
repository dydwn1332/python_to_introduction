#2-1연월일 사이에 '.'를 삽입하라.

year = input("년은?")
month = input("월은?")
day = input("일은?")

print(year, month, day, sep=".")

#2-2사각형 둘레와 면적을 계산하라.

a = int(input("사각형의 너비는? "))
b = int(input("사각형의 높이는? "))
print("사각형의 너비: %dcm" %a)
print("사각형의 높이: %dcm" %b)
c = a * 2 + b * 2
print("둘레 길이: ", "%dcm" %c)
d = a * b
print("면적 : " "%dcm2" %d)

#2-3 원의 둘레와 면적을 구하라.

Radius = float(input("반지름은?"))
print("반지름 : %.2f cm" %Radius)
Circle_circumference = Radius * 2 * 3.14
print("원의 둘레 : %.2fcm" %Circle_circumference)
Circle_area = Radius * Radius * 3.14
print("원의 면적 : %.2fcm2" %Circle_area)

#2-4 인치를 센티미터로 환산하라.

inch = float(input("인치는? "))
cm = inch * 2.54
print("%.1f inch => %.1f cm" %(inch, cm))

#2-5 온라인 서점의 책 결제 금액을 계산하라.

Book_price = int(input("책 값은? "))
discount = int(input("할인율은? "))
delivery = int(input("배송료는? "))

pay = Book_price - (Book_price * (discount/100)) + delivery

print("책 값: %d원" %Book_price)
print("할인율: %d" %discount)
print("배송료: %d원" %delivery)
print("결제 금액: %d원" %pay)