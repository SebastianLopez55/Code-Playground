# Implementation of the KMP algorithm: find word in text. Return index of first occurrence or -1 if not found.


def longest_prefix_suffix(s: str) -> list:
    if s == "":
        return []
    n = len(s)
    lps_table = [0] * n
    prev_lps, curr_char_idx = 0, 1

    while curr_char_idx < n:
        if s[prev_lps] == s[curr_char_idx]:
            prev_lps += 1
            lps_table[curr_char_idx] = prev_lps
            curr_char_idx += 1
        elif prev_lps == 0:
            lps_table[curr_char_idx] = 0
            curr_char_idx += 1
        else:
            prev_lps = lps_table[prev_lps - 1]
    return lps_table


def occurrence_in_string(text: str, word: str):
    pass


# TESTING


def test_longest_prefix_suffix():
    # Test case 1: General case with a repeating pattern
    assert longest_prefix_suffix("btab") == [0, 0, 0, 1], "Test case 1 failed: 'abtab'"

    # Test case 2: Empty string
    assert longest_prefix_suffix("") == [], "Test case 2 failed: Empty string"

    # Test case 3: No repeating pattern
    assert longest_prefix_suffix("abcd") == [0, 0, 0, 0], "Test case 3 failed: 'abcd'"

    # Test case 4: All characters are the same
    assert longest_prefix_suffix("aaaa") == [0, 1, 2, 3], "Test case 4 failed: 'aaaa'"

    # Test case 5: Single character string
    assert longest_prefix_suffix("a") == [0], "Test case 5 failed: 'a'"

    print("All test cases passed!")


test_longest_prefix_suffix()
