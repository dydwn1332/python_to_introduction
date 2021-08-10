##만나이 계산기를 만들어야된다.

#Birth_day = str(input("생년월일을 8자리로 입력하시오. : "))
#Date_now = str(input("현재날짜를 8자리로 입력하시오. : "))

#Birth_day_year = int(Birth_day[0:4])
#Birth_day_month = int(Birth_day[4:6])
#Birth_day_day = int(Birth_day[6:8])
#print(Birth_day_year)
#print(Birth_day_month)
#print(Birth_day_day)

#Date_now_year = int(Date_now[0:4])
#Date_now_month = int(Date_now[4:6])
#Date_now_day = int(Date_now[6:8])
#print(Date_now_year)
#print(Date_now_month)
#print(Date_now_day)

#if Date_now_year > Birth_day_year:
#    if Date_now_month < Birth_day_month:
#        age = Date_now_year - Birth_day_year - 1
#    elif Date_now_month == Birth_day_month:
#        if Date_now_day > Birth_day_day:
#            age = Date_now_year - Birth_day_year - 1
#        elif Date_now_day <= Birth_day_day:
#            age = Date_now_year - Birth_day_year
#        else:
#            age = 0
#    else:
#        age = Date_now_year - Birth_day_year
#else:
#    age = 0

#print("생년월일 : %d/%d/%d." %(Birth_day_year, Birth_day_month, Birth_day_day))
#print("현재날짜 : %d/%d/%d." %(Date_now_year, Date_now_month, Date_now_day))

#print("만나이 : %d세" %age)

##C3-7할인율에 따라 지불 금액을 계산하라!

#pay = int(input("구매 금액은? : "))

#if pay < 10000:
#    rate = 0
#elif 10000 <= pay and pay < 50000:
#    rate = 5
#elif 50000 <= pay and pay <= 300000:
#    rate = 7.5
#else:
#    rate = 10

#discount = pay * rate / 100

#Discount_pay = pay - discount

#print("구매금액 : %d." %pay)
#print("할인율 : %d." %rate)
#print("할인금액 : %d." %discount)
#print("지불금액 : %d." %Discount_pay)

#C3-8서비스 만족도에 따라 팁을 계산하라!

print("서비스 만족도 :")
print("1.매우만족")
print("2.만족")
print("3.불만족")

Satisfaction = int(input("서비스 만족도는?(1/2/3) "))
pay = int(input("음식 값은? "))

if Satisfaction == 1:
    service = "매우만족"
    tip = pay * 0.2
elif Satisfaction == 2:
    service = "만족"
    tip = pay * 0.1
else:
    service = "불만족"
    tip = 0

print("서비스 만족도 : %s, 팁 : %d" %(service, tip))