import copy

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


print()
print("=== 1. Assignment shares the same object ===")
lst = [1, 2, 3]
alias = lst
print(f"same object: {lst is alias}")
alias.append(4)
print(f"original changed: {lst}\n")

print("=== 2. Mutation keeps id, rebinding changes it ===")
lst = [1, 2, 3]
before = id(lst)
lst.append(4)
print(f"after mutation, same id: {id(lst) == before}")
lst = [9, 9, 9]
print(f"after rebinding, same id: {id(lst) == before}\n")

print("=== 3. Immutables always change id on 'change' ===")
x = 5
before = id(x)
x = x + 1
print(f"int, same id: {id(x) == before}")
s = "hello"
before = id(s)
s = s + " world"
print(f"str, same id: {id(s) == before}\n")

print("=== 4. Shallow copy with IMMUTABLE contents — safe ===")
original = [1, 2, 3]
shallow = copy.copy(original)
print(f"outer lists same object: {original is shallow}")
print(f"element 0 same object:   {original[0] is shallow[0]}")
shallow[0] = 99
print(f"original unaffected: {original}\n")

print("=== 5. Shallow copy with MUTABLE contents — leaks ===")
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
print(f"inner list shared: {original[0] is shallow[0]}")
shallow[0].append(99)
print(f"original LEAKED: {original}\n")

print("=== 6. Deep copy with MUTABLE contents — isolated ===")
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
print(f"inner list shared: {original[0] is deep[0]}")
deep[0].append(99)
print(f"original safe: {original}\n")

print("=== 7. Deep copy does nothing for immutables ===")
original = [1, 2, 3]
deep = copy.deepcopy(original)
print(f"element 0 still shared: {original[0] is deep[0]}\n")

print("=== 8. The [[]] * n trap ===")
trap = [[]] * 3
trap[0].append("x")
print(f"all slots share one list: {trap}")
safe = [[] for _ in range(3)]
safe[0].append("x")
print(f"comprehension is independent: {safe}\n")

print("=== 9. Immutable container, mutable contents ===")
lst = [1, 2]
tup = (0, lst)
print(f"tuple id before: {id(tup)}")
tup[1].append(3)
print(f"tuple id after:  {id(tup)}  (unchanged)")
print(f"but contents changed: {tup}")