# tạo ra 1 bản sao hoàn toàn mới
d = {"team":"kteam", (1,2):69}
print(d)
d2 = d.copy()
print(d2)
print(d.get("team"))
# nếu không tìm thấy key thì thay thế value 
print(d.get("aaa"," free edu"))
# trả ra 1 tuple
print(d.items())
value = list(d.items())
print(value[0])
# lấy ra danh sách các key, value riêng 
print(d.keys())
print(d.values())
value1 = d.pop("team")
print(value1)
print(d)
# pop ngẫu nhiên  1 thằng 
d1 = {"team":"kteam", (1,2):69}
print(d1.popitem())
d1.setdefault("wttt")
print(d1)
d1.update(team = "free")
print(d1)
