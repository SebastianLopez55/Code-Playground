def test_check_if_eulerian_cycle_exists(func=lambda x: x):
    test_cases = [
        {
            "n": 5,
            "edges": [[0, 1], [0, 2], [1, 3], [3, 0], [3, 2], [4, 3], [4, 0]],
            "expected": True,
        },
        {
            "n": 6,
            "edges": [[0, 4], [0, 5], [1, 2], [2, 3], [3, 1], [4, 3]],
            "expected": False,
        },
        # Additional test cases can be added here
    ]

    for i, test_case in enumerate(test_cases):
        n = test_case["n"]
        edges = test_case["edges"]
        expected = test_case["expected"]

        result = func(n, edges)

        assert (
            result == expected
        ), f"Test case {i + 1} failed: expected {expected}, got {result}"
        print(f"Test case {i + 1} passed")


def check_if_eulerian_cycle_exists(n, edges):
    degree = [0] * n
    for edge in edges:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

    for d in degree:
        if d % 2 != 0:
            return False

    return True


def check_if_eulerian_cycle_exists2(n, edges):
    vertex_degree_map = {i: 0 for i in range(n)}

    for i in range(len(edges)):
        for j in range(2):
            vertex_degree_map[edges[i][j]] += 1

    for degree in vertex_degree_map.values():
        if degree % 2 != 0:
            return 0

    return 1


if __name__ == "__main__":
    func = check_if_eulerian_cycle_exists2
    test_check_if_eulerian_cycle_exists(func)
