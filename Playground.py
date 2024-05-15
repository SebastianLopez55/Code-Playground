# PG

d = {}

for num in range(10, -1, -1):
    d[num] = d.get(num, 0) + 1

print(d)
