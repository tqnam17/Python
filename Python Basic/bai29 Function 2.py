#Positional và keyword argument
print(sorted([3, 4, 1], reverse=True))
def Teo(a, b=2, c=3, d=4):
    f = (a + d) * (b + c)
    print(f)
Teo(1, d=5)
def kteam(aa, *, bb =1 , cc =2):
    print(aa)
    print(bb)
    print(cc)
kteam(1)
