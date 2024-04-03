def kSum(k, nums, target):
    nums.sort()
    q_plets, curr_kSum = [], []

    def kSum(k, start, target):
        if k != 2:
            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr_kSum.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])

                curr_kSum.pop()
            return

        # base case, two sum II
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                q_plets.append(curr_kSum + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1

    kSum(k, 0, target)
    return q_plets


nums = [1, 0, -1, 0, -2, 2]
target = 0

# First understand how the function works with k = 4
# print(kSum(1, nums, target))

# assert kSum(1, nums, target) == [], "failed 1Sum test one."

assert kSum(2, nums, target) == [[-2, 2], [-1, 1], [0, 0]], "failed 2Sum test one."

assert kSum(4, nums, target) == [
    [-2, -1, 1, 2],
    [-2, 0, 0, 2],
    [-1, 0, 0, 1],
], "failed 4Sum test one."
