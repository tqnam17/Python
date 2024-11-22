# Dict là một unhashable object 
# Dict Comprehension
dic = {key: value for key, value\
       in [("name", "kteam"),("aa", "bb")]}
print(dic)
# khởi tạo bằng iterable
iter_ = [('name', 'kteam'), ('mem', 69)]
dic = dict(iter_)
print(dic)
dic1 = dict(name = 'kteam', member = 69)
print(dic1)
inter1 = ('name', 69 ,True)
dic2 = dict.fromkeys(inter1, "howk")
print(dic2)
# cách lấy giá trị từ key
print(dic2['name'])
dic2["name"] = "free edu"
print(dic2['name'])
dic1["member"] = dic1["member"] + 1
print(dic1)
