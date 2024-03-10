def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        last_digit = n % 10
        digit_sum += last_digit
        n = n // 10
    return digit_sum


n = 1234
print(sum_of_digits(n))
n2 = 12
print(sum_of_digits(n2))
