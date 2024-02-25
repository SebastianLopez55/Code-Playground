# Playing with Bitwise operators

integer = 8
binary = 0b1000
print(bin(integer)[2:])
print(binary)

print("== TESTING THE 'AND' OPERATOR ==")
print(8 & 0b0001)
print(8 & 0b1000)
print(bin(8 & 0b1000))
i = 1
num = 0b1111
print(bin(num & ~(1 << i)))

print("== TESTING THE 'OR' OPERATOR ==")
print(0b0101 | 0b1010)
print(0b1111)
print((0b0101 | 0b1010) == (0b1111))

print("== TESTING THE 'XOR' OPERATOR ==")
print(0b0000 ^ 0b1111)
print(bin(0b0000 ^ 0b1111))
# Other operations
print(7 ^ 7 == 0)
print(7 ^ 0 == 7)


print("== TESTING THE 'NOT' OPERATOR ==")
print(0b0101 == 5)

# Manual Two's Complement of Decimal 5
print(bin((5 ^ 0b1111) + 1))

# Using NOT to get Two's complement
print(bin(~5))

print("== LEVERAGING BITWISE OPERATORS ==")
