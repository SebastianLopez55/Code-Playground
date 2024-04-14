graph_no_cycle = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: []}
graph_cycle = {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}


def cycle_detection(graph):
    visited = set()
    visiting = set()  # recursion stack

    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False

        visiting.add(node)
        visiting.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        visiting.remove(node)
        return False

    for node in graph:
        if dfs(node):
            return True

    return False


# O(V + E) time
# O(V) space


print(cycle_detection(graph_no_cycle))
print(cycle_detection(graph_cycle))
