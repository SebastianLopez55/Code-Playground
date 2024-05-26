import sys

print(sys.maxsize)
print(int(sys.maxsize) / 64)

large_int = 2**65
print(large_int * large_int)

print(float("inf") - float("inf"))
