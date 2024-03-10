"""
sum_of_digits() complexity analysis:

Time Complexity: the time complexity of the algorithm depends on how many digits the number has.
    - The key operation is dividing the given integer by floor of 10. 
    - Thus, the time complexity is given by the number of operations which is in turn given my the number
    of times we need to divide the given number by floor of 10 till we arrive to zero digits. 

"""


def sum_of_digits(n):
    digit_sum = 0
    while n > 0:
        last_digit = n % 10
        digit_sum += last_digit
        n = n // 10
    return digit_sum


# O(log n) time
# O(1) space

n = 1234
print(sum_of_digits(n))
n2 = 12
print(sum_of_digits(n2))
