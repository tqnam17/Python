

itera = [x for x in range(3)]
print(itera)
itera1 = (x for x in range(3))
print(itera1)
print(next(itera1))
print(next(itera1))
itera2 = (x for x in range(3))
print(sum(itera2,2))
itera2 = (x for x in range(3))
print(max(itera2))
print(max([], default="kteam"))
print(max(1,3,2, 5,9))
print(min(1, 2, 5,9))
a = [1,3,2,5,9]
print(sorted(a, reverse= True))



