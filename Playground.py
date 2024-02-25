def findSingleNumber(nums):
    unique = 0
    for num in nums:
        unique = unique ^ num
    return unique


# Example usage
nums = [4, 1, 2, 1, 2]
print(findSingleNumber(nums))
