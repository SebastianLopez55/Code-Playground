"""
Use constant space to perform image smoothing 

To encode two numbers, p and r, into one number Y using a constant X, we use the formula Y = p*X + r. To get p back, we divide Y by X, and to get r back, we find the remainder of Y divided by X.

Example:

If p = 5, r = 3, and X = 10, then Y = 5*10 + 3 = 53.

To decode:
- p is found by dividing Y by X: 53 / 10 = 5.
- r is the remainder of Y divided by X: 53 % 10 = 3.

So, Y = 53 encodes the numbers p = 5 and r = 3.

"""


def imageSmoother(img):
    m = len(img)
    n = len(img[0])
    for i in range(m):
        for j in range(n):
            sum = 0
            count = 0
            for x in (i - 1, i, i + 1):
                for y in (j - 1, j, j + 1):
                    if 0 <= x < m and 0 <= y < n:
                        sum += img[x][y] % 256
                        count += 1
            img[i][j] += (sum // count) * 256
    for i in range(m):
        for j in range(n):
            img[i][j] //= 256
    return img


# Driver code
img = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
for row in img:
    print(row)
smoothed_img = imageSmoother(img)
print("Smoothed Image:")
for row in smoothed_img:
    print(row)

# O(m * n) time
# O(1) space
