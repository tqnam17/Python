a = [1,1,1,3,4,5]
print(a.count(1))
# đếm vị trí phần tử trong lish
print(a.index(3))
b = a.copy()
b[0] = "kteam"
print(a)
print(b)
# phương thức clear
aa = [50]
bb = aa
print(aa)
print(bb)
bb.clear()
print(aa)
print(bb)
a.append([6,7])
print(a)
a.extend([8,9,[11,22]])
print(a)
# thêm phần tử y vào vị trí x
a.insert(2, 33)
print(a)
# lấy ra phần tử vị trí x
a.pop(2)
print(a)
a.pop()
print(a)
#bỏ đi phần tử có giá trị x
a.remove(4)
print(a)
#đảo ngược list
a.reverse()
print(a)
# sắp xếp list từ nhỏ đến lớn,
 #phải cùng kiểu dữ liệu
cc = [9,5,4,3,8,8]
cc.sort()
print(cc)
cc.sort(reverse = True)
print(cc)

