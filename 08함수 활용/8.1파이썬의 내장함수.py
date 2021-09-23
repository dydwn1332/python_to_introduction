#8.1.1 아스키코드 구하기
x = '1'
print("1의 아스키코드 : ", ord(x))

#8.1.2 16진수 2진수로 변환하기 hex() bin()
a = ord(x)
print("%s의 아스키코드 : %d" %(x, a))
print("%s의 아스키코드16진수 : %s" %(x, hex(a)))
print("%s의 아스키코드2진수 : %s" %(x, bin(a)))

#8.1.3 반올림값 구하기 round()
x = round(12.987542)
print(x)
a = round(12.987542, 4)
print(a)

#8.1.4 최댓값 최솟값 구하기
asd = list([12,13,14,15,16])
a = max(asd)
b = min(asd)
print(a, b)