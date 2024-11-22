



# list có thể bao gồm chính nó
a= [[[1,2],["nam"]],[4],["a"]]
print(a)
b =[i for i in range(5)]
print(b)
c = [[n, n*1,n*2] for n in range(1,4)]
print(c)
print(list("cccc"))
#toán tử
d = [1,2]
d += ["one", "two"]
print(d)
print(d*2)
print(1 in d)
ee= [1,2,"a","b",[3,4]]
print(ee[4][0])
print(ee[1:4])
print(ee[:2])
print(ee[2:])
print(ee[::-1])
print(ee[::])
ee[1] = "kteam"
print(ee)
aa= [1,2,3]
bb = list(aa)
bb[0] = "kteam"
print(bb)
print(aa)
