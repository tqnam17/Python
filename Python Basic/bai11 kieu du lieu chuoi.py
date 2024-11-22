# tách các phần tử từ khoảng trắng\
    #trả về 1 list
a = "how KTeam free education"
print(a.split(" "))
print(a.split(" ", 2))
print(a.rsplit(" ", 2))
print(a.split("e"))
# trả về 1 tuple với 3 phần tử
print(a.partition("k"))
print(a.rpartition("y"))
print(a.count("e"))
print(a.count("e",0,10))
#
print(a.startswith("how"))
print(a.startswith("k",5))
print(a.endswith("n"))
# vị trí đầu tiên nó tìm thấy chuỗi
print(a.find("kteam")) # không ra quăng ra -1
print(a.rfind("t"))
print(a.index("o")) # không ra sẽ quăng lỗi
# kiểm tra có phải biết thường hay hoa
print(a.islower())
print(a.isupper())
#kiểm tra có phải toàn số hay không
print(a.isdigit())
# có phải toàn là khoẳng trắng không
print(a.isspace())

