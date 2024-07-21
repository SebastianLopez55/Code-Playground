count = {}

for i in range(10):
    count[i] = count.get(i, 0) + 1

print(list(count.values()))
