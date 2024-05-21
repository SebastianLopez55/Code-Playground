d = {"a": 2, "b": 3}

while d["b"] >= 1:
    print(d["b"])
    d["b"] -= 1

    if d["b"] == 0:
        del d["b"]
