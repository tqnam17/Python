file_object = open("kteam.txt")
data = file_object.read(2222)
file_object.close()
file_object = open("kteam.txt")
data2 = file_object.read(3)
data3 = file_object.read(5)
print(data)
print(data2)
print(data3)
# đọc từng dòng
print(file_object.readline())
file_object.close()
file_object = open("kteam.txt")
# đọc toàn bộ file, cho vào 1 list
print(file_object.readlines())
file_object.close()
file_object = open("kteam.txt")
print(list(file_object)) # giống cách trên
file_object.close()
file_object = open("kteam.txt", mode= "a+")
data4 = file_object.write("\nl88")
file_object.close()
print(data4)
# kiểm soát con trỏ file
file_object = open("kteam.txt", mode= "r")
data5 = file_object.read()
file_object.seek(20)
data6= file_object.read()
print(data5)
print(data6)



