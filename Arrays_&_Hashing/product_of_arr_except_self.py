# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


def naive_except_self(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            if i != j:
                product *= lst[j]
        res.append(product)
    return res

    # O(n^2) time.
    # O(n) space.


# TEST CASES:
case_num = 1
lst = [1, 2, 3]
expected = [6, 3, 2]
assert (
    naive_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


# TEST CASES:
case_num = 2
lst = [1, 0, 3]
expected = [0, 3, 0]
assert (
    naive_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


# TEST CASES:
case_num = 3
lst = [0, 0, 0]
expected = [0, 0, 0]
assert (
    naive_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


"""
nums = [2, 3, 2] -> [6, 4, 6]

left =  [1, 2, 6]
right = [6, 2, 1]

res[i] = left[i] * right[i]
"""


def product_except_self(lst):
    n = len(lst)

    left = [1] * n
    right = [1] * n
    answer = [1] * n

    for i in range(1, n):
        left[i] = left[i - 1] * lst[i - 1]

    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] * lst[i + 1]

    for i in range(n):
        answer[i] = left[i] * right[i]

    return answer

    # O(n) time.
    # O(n) space.


# TEST CASES:
case_num = 1
lst = [1, 2, 3]
expected = [6, 3, 2]
assert (
    product_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


# TEST CASES:
case_num = 2
lst = [1, 0, 3]
expected = [0, 3, 0]
assert (
    product_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


# TEST CASES:
case_num = 3
lst = [0, 0, 0]
expected = [0, 0, 0]
assert (
    product_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"


# TEST CASES:
case_num = 4
lst = []
expected = []
assert (
    product_except_self(lst) == expected
), f"Test case {case_num} failed: product except self of {lst} not equal to {expected}"
