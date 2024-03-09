import random as r

# Get the first digit
num = 32347
print(int(str(num)[0]))
print(num // 10000)

# Get the last digit
print(num % 10)


# Random nums
rand = r.random() * 1000000
print(rand)
print(int(rand))
