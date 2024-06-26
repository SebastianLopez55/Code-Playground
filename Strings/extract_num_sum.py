def is_number(char_stg):
    return char_stg in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def extract_sum(string):
    nums = []
    n = len(string)
    i = 0

    while i < n:
        temp = ""
        curr_char = string[i]
        if string[i] == "-" and (i + 1) < n and is_number(string[i + 1]):
            curr_char = string[i]
            temp += string[i]
            temp += string[i + 1]
            i += 2

        while i < n and is_number(string[i]):
            curr_char = string[i]
            temp += string[i]
            i += 1

        if temp:
            nums.append(int(temp))
        else:
            curr_char = string[i]
            i += 1

    return sum(nums)


assert extract_sum("1a2b3c") == 6, "Fails test 1."
assert extract_sum("123ab!45c") == 168, "Fails test 2."
assert extract_sum("abcdef") == 0, "Fails test 3."
assert extract_sum("0123.4") == 127, "Fails test 4."
assert extract_sum("dFD$#23+++12@#T1234;/.,10") == 1279, "Fails test 5."
assert extract_sum("12a-10b") == 2, "Fails test 6."
assert extract_sum("12a-b10") == 22, "Fails test 7."
assert extract_sum("-1b-1") == -2, "Fails test 8."


print("All tests passed!")
