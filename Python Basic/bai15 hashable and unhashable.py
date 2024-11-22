#a = id("kteam")
b = 'Kteam'
a = id(b)
c = id('Kteam')
print(a)
print(c)
n = 69
print(n + 1)
print(n.__add__(1))
print(n.__sub__(1))
print(n.__mul__(2))
print(n.__radd__(2))
print(n.__neg__())
# toán tử hashable ví dụ như chuỗi, tuple
s1 = "tran"
s2 = "quang"
s1 = s1 + "aa"
s2 += "bb"
print(id(s1))
print(id(s2))
# unhashable ví dụ như list, thay đổi được nội dung 
s3 =[1,2]
print(id(s3))
s3.__add__([3,4])
print(id(s3))






