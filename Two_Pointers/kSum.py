def kSum(k, nums, target):
    nums.sort()
    q_plets, curr_kSum = [], []

    def kSum_helper(k, start, target):
        # New structure: Check for the base case at the beginning
        if k == 2:  # Base case: two sum II
            l, r = start, len(nums) - 1
            while l < r:
                current_sum = nums[l] + nums[r]
                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    q_plets.append(curr_kSum + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
            return

        # Recursive case for k > 2
        for i in range(start, len(nums) - k + 1):
            if i > start and nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            curr_kSum.append(nums[i])
            kSum_helper(k - 1, i + 1, target - nums[i])
            curr_kSum.pop()

    kSum_helper(k, 0, target)
    return q_plets


# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(kSum(4, nums, target))


nums = [1, 0, -1, 0, -2, 2]
target = 0

# First understand how the function works with k = 4
# print(kSum(1, nums, target))

# assert kSum(1, nums, target) == [], "failed 1Sum test one."

# assert kSum(2, nums, target) == [[-2, 2], [-1, 1], [0, 0]], "failed 2Sum test one."

assert kSum(4, nums, target) == [
    [-2, -1, 1, 2],
    [-2, 0, 0, 2],
    [-1, 0, 0, 1],
], "failed 4Sum test one."
