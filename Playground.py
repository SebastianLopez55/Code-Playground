"""
Code Playground 

"""

from collections import Counter

test_set = set()
test_set.add(("a", "b"))
print(test_set)


s = "abcd"
char_count = Counter(s)

print(char_count)


del char_count["a"]
char_count.pop("b")

print(char_count)
