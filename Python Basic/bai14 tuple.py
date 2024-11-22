# tuple có thể chứa mọi giá trị
# tốc độ truy xuất tuple nhanh hơn list
# bảo vệ dữ liệu không bị thay đổi
# không cho phép sữa chữa nội 
# tuple có thể chứa chính nó
a = (1,1,(2,5,6),"kteam")
print(a)
# 1 đơn vị sẽ không còn là tuple, thành int
b = (1)
print(b)
c = tuple([1,2,3])
print(c)
d = tuple("kteam")
print(d)
tup= (i for i in range(10) if i%2==0)
aa = tuple(tup)
print(aa)
# truy xuất vẫn dùng ngoặc []
bb = aa[1]
print(bb)
# đếm xem có bao nhiêu phần tử
print(len(aa))
print(aa[::-1])

