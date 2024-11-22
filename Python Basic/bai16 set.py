# trong set không thể chứa lish
# ví dụ: set1 = {[1,2],[3,4]}  
# set không thể chứa set, các unhashable
# set không phải là 1 hash object 
print(set((1,2,3)))
print(set("kteame"))
set1 = set([1,5,8,3,1,6])
print(set1)
print({1,2} in {1,2,3})
print((1,2) in {(1,2),3})
print({1,2,3} - {1,2})
print({2,3} - {2,3,4,5})
print({2,3} & {2,3,4,5})
print({2,3} | {2,3,4,5})
# lấy | trừ &  
print({2,3} ^ {2,3,4,5})
# indexing và cắt trong set không hỗ trợ
print(set1.pop())
set1.remove(8)
print(set1)
set1.discard(99) # sẽ không báo lỗi
print(set1)
set1.add(44)
print(set1)
