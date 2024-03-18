def longestSubstring(s: str) -> int:
    window = dict()  # char : index
    longest = ""

    L = 0
    for R in range(len(s)):
        curr_char = s[R]
        if curr_char in window:
            # If new idx inside window update left
            new_idx = window[curr_char] + 1
            if L < new_idx:
                L = new_idx
        window[curr_char] = R
        if (R - L + 1) > len(longest):
            longest = s[L : R + 1]
        # longest = max(longest, R - L + 1)
    return longest


# O(n) time
# O(min(m, n)) space. m := size of alphabet and n := size of string

assert longestSubstring("abcabcbb") == "abc"
assert longestSubstring("bbbbb") == "b"
assert longestSubstring("pwwkew") == "wke"
assert longestSubstring("12345%#@! snfugh") == "12345%#@! snfugh"

print(" All tests passed!! ")
