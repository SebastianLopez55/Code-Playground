class Solution:
    # Solve "fourSum"
    def fourSum(self, nums, target):
        return self.kSum(4, nums, target)

    # Solve "twoSum II"
    def twoSum(self, k, start, target, nums, q_plets, curr_kSum):
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

    # Solve kSum, generic approach.
    def kSum(self, k, nums, target):
        nums.sort()
        q_plets, curr_kSum = [], []

        def kSum_helper(k, start, target):
            # Base case: two sum II
            if k == 2:
                return self.twoSum(k, start, target, nums, q_plets, curr_kSum)

            # Recursive case for k > 2
            for i in range(start, len(nums) - k + 1):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                curr_kSum.append(nums[i])
                kSum_helper(k - 1, i + 1, target - nums[i])
                curr_kSum.pop()

        kSum_helper(k, 0, target)
        return q_plets

    # O(n^k-1) time
    # O(n) space


# Tests
nums = [1, 0, -1, 0, -2, 2]
target = 0

s1 = Solution()
assert s1.kSum(2, nums, target) == [[-2, 2], [-1, 1], [0, 0]], "failed 2Sum test one."
assert s1.kSum(3, nums, target) == [[-2, 0, 2], [-1, 0, 1]], "failed 3Sum test one."
assert s1.kSum(4, nums, target) == [
    [-2, -1, 1, 2],
    [-2, 0, 0, 2],
    [-1, 0, 0, 1],
], "failed 4Sum test one."
