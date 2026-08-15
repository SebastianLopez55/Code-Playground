num = 12345

print("right", num % 10)
print("left", num // 10000)
print()
num = num % 10000
print(num)
num = num // 10
print(num)


num = 2734
print(f"Input number: {num}")
print(f"Get the last digit: num % 10 = {num % 10}")
print(f"Get the first digit: num // 1000 = {num // 1000}")
print(f"Everything but the last digit: num // 10 = {num // 10} -> Floor Div")
print(f"Everything but the first digit: num % 1000 = {num % 1000}")
