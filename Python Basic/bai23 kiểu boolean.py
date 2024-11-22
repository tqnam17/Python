print(3>1 & 1>3)
# so sánh bằng hàm ord
print(ord("A"))
print("aaa" < "aaAc")
print("aaa" < "aaaAc")
# ==  sẽ so sánh bằng giá trị của chúng. 
# is thì sẽ lấy giá trị của hàm id để so sánh.
lst = [1,2,3]
lst1 = [1,2,3]
print("1: ",lst == lst1)
print(lst is lst1)
lst2 = lst
print(lst2 is lst)
print(id(lst))
print(id(lst2))
print(id(lst1))
