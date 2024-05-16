from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        T, points = 0, 0

        # Setup window
        for i in range(k):
            T += calories[i]

        if T < lower:
            points -= 1
        if T > upper:
            points += 1

        # Slide window
        for i in range(k, len(calories)):
            T += calories[i] - calories[i - k]
            if T < lower:
                points -= 1
            if T > upper:
                points += 1
        return points


s = Solution()
cals = [1, 1, 2, 3, 4, 5, 1, 2, 1, 3, 2, 0, 0]
print(s.dietPlanPerformance(cals, 3, 5, 6))
