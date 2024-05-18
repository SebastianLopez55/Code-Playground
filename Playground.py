from itertools import accumulate


for i in range(1, -2, -1):
    print(i)


lst = [1, 2, 3, 4]

prefix_sum = list(accumulate(lst, initial=0))

print(prefix_sum)
