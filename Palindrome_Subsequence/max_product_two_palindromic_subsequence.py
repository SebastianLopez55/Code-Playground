# 2002. Maximum Product of the Length of Two Palindromic Subsequences


def maxProduct(s: str) -> int:
    N, pali = len(s), {}  # bitmask : length

    iterable = range(1, 1 << N)

    for mask in iterable:  # 1 << N == 2 ** N
        subseq = ""
        for i in range(N):
            if mask & (1 << i):
                curr = s[i]
                subseq += curr
        if subseq == subseq[::-1]:
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

s = "bb"
print(maxProduct(s))
