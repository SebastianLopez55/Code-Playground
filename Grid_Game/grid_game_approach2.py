def gridGame(grid):
    n = len(grid[0])
    prefix_top = grid[0].copy()
    prefix_bottom = grid[1].copy()

    for i in range(1, n):
        prefix_top[i] += prefix_top[i - 1]
        prefix_bottom[i] += prefix_bottom[i - 1]

    total_points_top = prefix_top[-1]
    bot2_points = float("inf")
    for i in range(n):
        points_top = total_points_top - prefix_top[i]
        if i > 0:
            points_bottom = prefix_bottom[i - 1]
        else:
            points_bottom = 0
        possible_bot2_points = max(points_top, points_bottom)
        bot2_points = min(bot2_points, possible_bot2_points)
    return bot2_points


grid1 = [[2, 5, 4], [1, 5, 1]]

print(gridGame(grid1))

# O(n) time
# O(n) space
