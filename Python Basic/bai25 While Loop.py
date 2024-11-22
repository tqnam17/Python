k = 5
while k>0:
    print("k= ", k)
    k -=1
# xử lí chuỗi, list, tuple
s = "How Kteam"
idx = 0
length = len(s)
while idx < length:
    print(idx, " stands for" , s[idx])
    idx +=1
#Câu lệnh break dùng để kết thúc vòng lặp chứa nó
five_numbers = []
k_number = 1
while True:
    if k_number % 2 ==0:
        five_numbers.append(k_number)
    if len(five_numbers) >=5:
        break
    k_number +=1
print(five_numbers)
print(k_number)
#continue sẽ tiếp tục vòng lặp, 
#không quan tâm những câu lệnh ở dưới continue
x_number = 0
while x_number < 10:
    x_number +=1
    if x_number % 2 ==0:
        continue
    print(x_number, "is oldd number")
print(x_number)
#vòng lặp while kết thúc
# thì khối lệnh else-block sẽ được thực hiện.
while k < 3:
    print('value of k is', k)
    k += 1
else:
    print('k is not less than 3 anymore')
    