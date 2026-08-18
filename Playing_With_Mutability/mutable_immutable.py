print("Mutable object")
# MUTABLE — "change first element"
lst = [1, 2, 3]
lst_first_id = id(lst)
print(id(lst))       # A
lst[0] = 99          # in-place mutation
print(id(lst))       # A — SAME
print("Did lst id changed? ", lst_first_id != id(lst))


print("Immutable object")
# IMMUTABLE — "change first character"
s = "abc"
string_first_id = id(s)
print(id(s))         # B
s = "x" + s[1:]      # must build a new string
print(id(s))         # C — DIFFERENT
print("Did string id changed? ", string_first_id != id(s))
