def is_prime(n):
    """Helper function to determine if n is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


for i in range(-10, 100):
    if is_prime(i):
        print(f"Is prime: {i}")
