# chỉ viết hoa chữ cái đầu, viết thường lại những chữ viết hoa
a = "buồn Có huw - FReeb"
b = a.capitalize()
print(b)
# viết hoa, viết thường tất cả các chữ
c = "how KTeam - FRee ed"
print(c.upper())
print(c.lower())
# thường thành hoa, hoa thành thường
print(c.swapcase())
# viết hoa các chữ cái 
print("1: " + c.title())
# nằm trong 30 ô hiển thị , fillchar chỉ 1 đơn vị
print(a.center(30))
print(a.center(30, "*"))
print(a.rjust(30, "+"))
print(a.ljust(30, "-"))
# mã hóa chuẩn
d = a.encode(encoding= "utf-8", errors="strict")
print(d)
# cộng đan xen
print(a.join(["1","2","3"]))
print(a.join(("1","2","3")))
# thay thế
print(a.replace("u", "oo88"))
print(a.replace("u", "oo88",1))
# xóa bỏ khoảng trắng hoặc cắt chữ đầu cuối
print(a.strip("b"))
print(a.lstrip("b"))
print(a.rstrip("b"))




