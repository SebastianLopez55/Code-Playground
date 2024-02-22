def transpose(matrix):
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def rotate(matrix):
    transpose(matrix)
    for row in matrix:
        row.reverse()


def findRotation(mat, target):
    for _ in range(4):
        if mat == target:
            return True
        rotate(mat)
    return False


# Driver
m = [[1, 2], [0, 1]]
t = [[2, 1], [1, 0]]

print(findRotation(m, t))

# O(n^2) time
# O(1) space
