import random


def shuffle_stg(s: str) -> str:
    # Convert string to a list to shuffle characters
    arr = list(s)
    n = len(arr)
    for i in range(n):
        # Pick a random index from i (inclusive) to the end of the array
        swap_idx = random.randrange(i, n)
        # Swap the current element with the element at the random index
        arr[i], arr[swap_idx] = arr[swap_idx], arr[i]
    # Convert the list back to a string and return
    return "".join(arr)


s = "hope"
print(shuffle_stg(s))

# O(n) time
# O(1) space
