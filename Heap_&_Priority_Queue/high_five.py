from typing import List
from collections import defaultdict
import heapq


class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Dictionary to store all scores for each student
        scores = defaultdict(list)

        # Populate the dictionary with the scores
        for ID, score in items:
            heapq.heappush(scores[ID], score)
            if len(scores[ID]) > 5:
                heapq.heappop(scores[ID])

        result = []

        # Calculate the top five average for each student
        for ID in sorted(scores.keys()):
            top_five_scores = scores[ID]
            average = sum(top_five_scores) // 5
            result.append([ID, average])

        return result


# Test cases
test_cases = [
    [
        [1, 91],
        [1, 92],
        [2, 93],
        [2, 97],
        [1, 60],
        [2, 77],
        [1, 65],
        [1, 87],
        [1, 100],
        [2, 100],
        [2, 76],
    ],
    [
        [1, 100],
        [7, 100],
        [1, 100],
        [7, 100],
        [1, 100],
        [7, 100],
        [1, 100],
        [7, 100],
        [1, 100],
        [7, 100],
    ],
]

# Initialize Solution object
solution = Solution()

# Run test cases
for i, test_case in enumerate(test_cases):
    result = solution.highFive(test_case)
    print(f"Test Case {i+1}: {result}")
