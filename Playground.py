import heapq

ls1 = [1, 234, 3241, 23, 2]
for i in range(len(ls1)):
    ls1[i] = -ls1[i]
heapq.heapify(ls1)
print(ls1)
max1, max2 = -heapq.heappop(ls1), -heapq.heappop(ls1)
print(ls1)
print(f"This is the first max {max1} and this is the second max {max2}.")
