def kteam(k, t, e, r):
    print(k)
    print(t, e)
    print('end', r)
lst = ['123', 'Kteam', 69.96]
#kteam(lst[0], lst[1], lst[2], lst[3])
kteam(*lst,"kter")
#
def kteam1(k, t, e,*, r="kter"):
    print(k)
    print(t, e)
    print('end', r)
lst1 = ['123', 'Kteam', 69.96]
#kteam(lst[0], lst[1], lst[2], lst[3])
kteam1(*lst1,r="k9")
#
def kteam2(*kwargs):
    print(kwargs)
    print(type(kwargs))
kteam2('Kteam',69.69, "hery")
kteam2(*(x for x in range(7)))
#
def kte3(name, mem):
    print("1: ", name)
    print("2: ", mem)
dic = {"name": "kteam", "mem":69}
kte3(**dic)
#
def kteam(**kwargs):
    for key, value in kwargs.items():
        print(key, '=>', value)
kteam(name = "kteam", member= 69)