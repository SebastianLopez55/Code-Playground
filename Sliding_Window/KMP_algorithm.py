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

    # O(n) time
    # O(n) space


# KMP Algorithm
def occurrence_in_string(text: str, word: str):
    if not text or not word:
        return -1

    word_lps_table = longest_prefix_suffix(word)
    i, j = 0, 0
    while i < len(text):
        if text[i] == word[j]:
            i, j = i + 1, j + 1
        elif j == 0:
            i += 1
        else:
            j = word_lps_table[j - 1]

        if j == len(word):
            return i - len(word)
    return -1


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


def test_occurrence_in_string():
    # Test case 1: Word found at the beginning
    assert (
        occurrence_in_string("hello world", "hello") == 0
    ), "Test case 1 failed: Word 'hello' not found at the beginning."

    # Test case 2: Word found in the middle
    assert (
        occurrence_in_string("the quick brown fox", "quick") == 4
    ), "Test case 2 failed: Word 'quick' not found in the middle."

    # Test case 3: Word found at the end
    assert (
        occurrence_in_string("subscribe to pewdiepie", "pie") == 19
    ), "Test case 3 failed: Word 'pie' not found at the end."

    # Test case 4: Word not found
    assert (
        occurrence_in_string("hello world", "bye") == -1
    ), "Test case 4 failed: Word 'bye' incorrectly found."

    # Test case 5: Empty text string
    assert (
        occurrence_in_string("", "hello") == -1
    ), "Test case 5 failed: Non-empty word found in empty text."

    # Test case 6: Empty word string (depending on your definition, might always return 0 or -1)
    assert (
        occurrence_in_string("hello world", "") == -1
    ), "Test case 6 failed: Empty word should return -1."

    # Test case 7: Word is longer than text
    assert (
        occurrence_in_string("hi", "hello") == -1
    ), "Test case 7 failed: Longer word found in shorter text."

    # Test case 8: Exact match
    assert (
        occurrence_in_string("hello", "hello") == 0
    ), "Test case 8 failed: Exact word not matched exactly."

    # Test case 9: Repeated patterns
    assert (
        occurrence_in_string("abababab", "abab") == 0
    ), "Test case 9 failed: Repeated pattern 'abab' not found at start."

    # Test case 10: Special characters
    assert (
        occurrence_in_string("fun&!!fun&!!", "&!!") == 3
    ), "Test case 10 failed: Special characters '&!!' not found."

    print("All test cases passed!")


test_longest_prefix_suffix()
test_occurrence_in_string()
