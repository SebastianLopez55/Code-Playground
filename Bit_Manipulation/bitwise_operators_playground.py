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
inverted = 5 ^ 0b1111
print("Binary 5 Inverted: ", bin(inverted))
print("Two's Complement (Negative Representation: ", bin(inverted + 1))

print(bin(~5))
print(~5)

print(bin(~13))
print(~13)

print("== Left and Right Shift ==")
print(bin(0b1010 << 1) == str(bin(0b10100)))
print(bin(0b1010 >> 1) == str(bin(0b0101)))
