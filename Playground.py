num = 239
lst = [2, 3, 9]
lst1 = []

n1 = num % 100
print(n1)  # 39

n2 = num % 10
print(n2)  # 9

n3 = num // 100
print(n3)  # 2

n4 = num // 10
print(n4)  # 23

print(str(num)[0])


for i in range(len(lst)):
    lst1.append(int(str(num)[i]))


print(lst1)
