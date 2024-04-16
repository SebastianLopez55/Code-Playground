n = 5
visited = [False] * n

print(any(visited))

for i in range(n):
    if i % 2 == 0:
        visited[i] = True


print(any(visited))


print(visited)

gen = (not i for i in visited)

for el in gen:
    print(el)
