from collections import Counter


def count_palindromic_subsequence(s: str) -> int:
    res = set()  # (middle, outer), at most 26^2 palindromes
    left = set()
    right = Counter(s)

    for i in range(len(s)):
        right[s[i]] -= 1
        if right[s[i]] == 0:
            right.pop(s[i])

        for j in range(26):
            c = chr(ord("a") + j)
            if c in left and c in right:
                res.add((s[i], c))

        left.add(s[i])

    return len(res)


# Example of calling the function
result = count_palindromic_subsequence("aabca")
print(result)  # Output the result of the example
