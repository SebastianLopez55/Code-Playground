import random as r


def shuffle_stg(s: str):
    included = set()
    shuffle = []

    while len(shuffle) < len(s):
        rand_idx = r.randint(0, len(s) - 1)
        if rand_idx not in included:
            included.add(rand_idx)
            shuffle.append(s[rand_idx])

    return "".join(shuffle)


s = "hope"
print(shuffle_stg(s))
