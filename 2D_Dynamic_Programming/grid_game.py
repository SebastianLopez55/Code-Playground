def gridGame(grid):
    n = len(grid[0])
    # Calculate prefix sums for top and bottom rows.
    prefix_top = [0] * (n + 1)
    prefix_bottom = [0] * (n + 1)
    for i in range(n):
        prefix_top[i + 1] = prefix_top[i] + grid[0][i]
        prefix_bottom[i + 1] = prefix_bottom[i] + grid[1][i]

    # Initialize the minimum score that the second robot can achieve to infinity.
    min_second_robot_score = float("inf")

    # Iterate through each column as a potential descent point for the first robot.
    for i in range(1, n + 1):
        # Score if the second robot goes all the way on top row until i then switches to the bottom row
        score_top = prefix_top[n] - prefix_top[i]
        # Score if the second robot starts on the bottom row and goes up at point i
        score_bottom = prefix_bottom[i - 1]
        # The second robot will choose the path with the maximum score.
        max_score = max(score_top, score_bottom)
        # The first robot wants to minimize this maximum score.
        min_second_robot_score = min(min_second_robot_score, max_score)

    return min_second_robot_score


# Test the function with the provided examples
grid1 = [[2, 5, 4], [1, 5, 1]]
grid2 = [[3, 3, 1], [8, 5, 2]]
grid3 = [[1, 3, 1, 15], [1, 3, 3, 1]]

# Output the results for each grid
print(gridGame(grid1))
print(gridGame(grid2))
print(gridGame(grid3))


# O(n) time
# O(n) space
