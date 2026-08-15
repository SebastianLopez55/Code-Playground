# 2002. Maximum Product of the Length of Two Palindromic Subsequences
def is_palindrome(s: str) -> bool:
    L, R = 0, len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True


def maxProduct(s: str) -> int:
    N, pali = len(s), {}  # bitmask : length

    # Generating every possible subsequence of the string
    for mask in range(1, 1 << N):  # 1 << N == 2 ** N
        subseq = ""
        for i in range(N):
            # Checking first character against LSB of mask.
            if mask & (1 << i):
                subseq += s[i]
        if is_palindrome(subseq):
            pali[mask] = len(subseq)

    res = 0
    for m1 in pali:
        for m2 in pali:
            if m1 & m2 == 0:  # disjoint
                res = max(res, pali[m1] * pali[m2])

    return res


# Driver
s = "leetcodecom"
print(maxProduct(s))

s = "abc"
print(maxProduct(s))

# O(4^n) time
# O(2^n) space
