def gridGame(grid):
    n = len(grid[0])
    points_top = sum(grid[0])
    curr_points_bottom = 0
    points_bottom = 0
    points_bot2 = float("inf")

    for i in range(n):
        curr_points_top = grid[0][i]
        points_top -= curr_points_top
        potential_bot2_points = max(points_top, points_bottom)
        points_bot2 = min(points_bot2, potential_bot2_points)
        points_bottom += grid[1][i]

    return points_bot2


# Driver
grid1 = [[2, 5, 4], [1, 5, 1]]
print(gridGame(grid1))

# O(n) time
# O(1) space
