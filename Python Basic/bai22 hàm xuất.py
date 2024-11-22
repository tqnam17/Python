print("Kteam  ", "Python", "couse")
print("Kteam  ", "Python", "couse", sep ="----")
print("Kteam  ", "Python", "couse", sep ="")
print("tran quang ", end = "--")
# nhập hàm sleep từ thư viện time
from time import sleep
print("star....")
sleep(3)
print("end...")
print("star....", end ="")
sleep(3)
print("end...")
with open("printext.txt", "w") as f:
    print("transsss", file=f)
your_name = "Herry"
your_great = "Hello, My name is"
for c in your_great+your_name:
    print(c, end="", flush=True)
    sleep(0.1)
print()
