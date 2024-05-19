import math


class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        def number_of_digits(n):
            if n == 0:
                return 1
            return int(math.log10(abs(n))) + 1

        k_beauty = 0
        num_copy = num
        num_digits = number_of_digits(num)

        while num_digits >= k:
            # Get the first k digits of num.
            first_k = num_copy // (10 ** (num_digits - k))

            # Check for k_beauty
            if first_k != 0 and num % first_k == 0:
                k_beauty += 1

            # Remove first digit:
            num_copy = num_copy % (10 ** (num_digits - 1))
            num_digits -= 1

        return k_beauty


# Test cases
solution = Solution()
print(solution.divisorSubstrings(240, 2))  # Expected: 2
print(solution.divisorSubstrings(430043, 2))  # Expected: 2
print(solution.divisorSubstrings(81, 2))  # Expected: 1
