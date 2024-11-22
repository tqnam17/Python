# lấy toàn bộ nội dung thư viện decimal
# từ thư viện Decimal -> import mọi thứ vào 
from decimal import*
# lấy tối đa 30 chữ số phần nguyên và phần thập phân Decimal
getcontext().prec=3

a = 10/3
b = Decimal(10)/Decimal(3)
print(a)
print(type(a))
print(b)
print(type(b))
# chỉ cần 1 cái là 
print(Decimal(10)/3)

# tạo 1 phân số
from fractions import*
frac1 = Fraction(6,9)
frac2 = Fraction(5,10)
frac3 = frac1 + frac2
print(frac3)
print(type(frac3))
#  số phức gồm 2 phần nguyên và phần ảo
# trong đó j là đơn bị ảo trong toán học j^2= -1
c = complex(2,5)
print(c)
print(c.real)
print(c.imag)
#thư viện math trong python
import math
print(math.trunc(3.9))
print(math.fabs(-3))
print(math.sqrt(16))
print(math.gcd(6, 4))
print(math.lcm(4,5))
print(math.ceil(9.4))

