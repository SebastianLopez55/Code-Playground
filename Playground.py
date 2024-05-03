def sumTwo(y):
    global x
    x = 2

    return x + y


x = 1
print(x)
print(sumTwo(3))
print(x)
