

a = " My team is %s"  %("Kteam")
print(a)
b = " My team is %s yeahs old"  %("1")
print(b)
c = " My team is %s %s yeahs old"  %("1", "2")
print(c)
s = "%s %s"
resukr = s %("1","2")
print(resukr)
n = "%d" %(3.9) # chỉ lấy phần nguyên
print(n)
d = "%.2f" %(3.56854)
print(d)
# định dạng bằng chuỗi f (f-string)
name= "Kteam"
address = "da lat"
phone = "0123"
result = f"student: {{name}}\nAddress: {address}\nPHone: {phone}"
print(result)
# căn lề format
r = "{:^10}".format("Kteam")
print(r)
bb = "How {:*^10} Free Edu".format("Kteam")
print(bb)
row_1 = "+ {:-<6} + {:-^15} + {:->10} + ".format("","","")
row_2 = "| {:-<6} | {:-^15} | {:->10} | ".format("ID","Hovaten","Noisinh") 
row_3 = "+ {:-<6} + {:-^15} + {:->10} + ".format("","","")
print(row_1)
print(row_2)
print(row_3)