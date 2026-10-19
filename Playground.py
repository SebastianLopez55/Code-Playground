"""
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1


"""


def _ships_within_days(capacity: int, days: int, weights: list[int]) -> bool:

    n = len(weights)
    i, curr_days, weight = 0, 0, 0
    while i < n:
        i_before = i

        while i < n and capacity >= weight + weights[i]:
            weight += weights[i]
            i += 1

        if i == i_before:
            return False

        weight = 0
        curr_days += 1

    return days >= curr_days


days = 4
weights = [1, 2, 3, 1, 1]

for capacity in range(1, sum(weights) + 1):
    print(
        f"Ships in {days} days with ship of capacity {capacity}?: ",
        _ships_within_days(capacity, days, weights),
    )
