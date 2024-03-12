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


# O(n) time
# O(1) space


# TEST: Are the letter truly random?
def test_shuffle_stg1(s: str, num_shuffles: int):
    pos_counts = {char: [0] * len(s) for char in s}
    for _ in range(num_shuffles):
        shuffled = shuffle_stg(s)
        for i, char in enumerate(shuffled):
            pos_counts[char][i] += 1
    return pos_counts


s = "Hope you make it!"
print(shuffle_stg(s))
print(test_shuffle_stg1(s, 10000))
