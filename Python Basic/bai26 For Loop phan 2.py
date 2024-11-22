k = range(3)
print(k[1])
print(list(range(2,5)))
print(list(range(4, 1, -1)))
lst = [5, (1, 2, 3), {'abc', 'xyz'}]
for i in range(len(lst)):
    print(lst[i])
lst1 = [1, 2, 3]
for i in range(len(lst1)):
    lst1[i] += 1
print(lst1)
# Comprehension
list_ = ['--'.join((a.capitalize(), b.upper() + c.lower()))\
         for a, b, c in [('how', 'kte', 'EDUC'), \
                         ('chia', 'sẻ', 'FR')]]
print(list_)
#
lst = []
for a, b, c in [('how', 'kt', 'EDU'), ('chi', 'sẻ', 'FR')]:
    a = a.capitalize()
    b = b.upper()
    c = c.lower()
    lst.append('--'.join((a, b + c)))
print(lst)
#hàm enumerate
aa = ["nam", "li", "anh"]
for idx, student in enumerate(aa,1):
    print(idx, "=>", student)
    