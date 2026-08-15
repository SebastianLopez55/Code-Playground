from collections import defaultdict


def neighbors(matrix):
    m = len(matrix)
    n = len(matrix[0])
    neighbors_table = defaultdict(list)
    # Traverse matrix
    for r in range(m):
        for c in range(n):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    new_r = dr + r
                    new_c = dc + c
                    if (0 <= new_r < m) and (0 <= new_c < n) and (dr != 0 or dc != 0):
                        entry = (matrix[r][c], r, c)
                        neighbors_table[entry].append(matrix[new_r][new_c])

    return neighbors_table


def neighbors2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    neighbors_table = defaultdict(list)

    def is_valid(row, column):
        return (0 <= row < m) and (0 <= column < n)

    for r in range(m):
        for c in range(n):
            for dr in range(r - 1, r + 2):
                for dc in range(c - 1, c + 2):
                    if is_valid(dr, dc) and (dr != r or dc != c):
                        entry = (matrix[r][c], r, c)
                        neighbors_table[entry].append(matrix[dr][dc])
    return neighbors_table


# Driver
letters = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

for row in letters:
    print(row)

print()

for key, value in neighbors2(letters).items():
    print(key, value)

# O(m * n) time for both
# O(m * n) space for both
