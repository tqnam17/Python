length = 3
iter_ = (x for x in range(length))
c = 0
while c < length:
    print(next(iter_))
    c += 1 
iter_1 = (x for x in range(length))
while 1:
    try:
        print(next(iter_1))
    except StopIteration:
        break
# vòng lặp for
# từng phần tử thực thi đoạn code
iter_2 =(x for x in range(length))
for value in iter_2:
    print("->", value)
#xử lí các iterator và Dict
howktean = {"name" :"kteam", "kter" : 69}
list_values = list(howktean.items())
print(list_values[0])
for key, value in howktean.items():
    print(key, "->" , value)
#Câu lệnh break, continue
s = "How Kteam"
for ch in s:
    if ch == " ":
        break
    else:
        print(ch)
for ch in s:
    if ch == " ":
        continue
    else:
        print(ch)
# sau khi kết thúc for thì thực hiện else
for k in (1,2,3):
    print(k)
else:
    print("Done!")


