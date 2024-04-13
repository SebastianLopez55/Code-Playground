graph = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: []}


def dfs_recursive(graph):
    visited = set()

    def dfs_helper_rec(graph, source):
        visited.add(source)
        print(source)
        neighbors = graph[source]
        for node in neighbors:
            if node not in visited:
                dfs_helper_rec(graph, node)

    for node in graph.keys():
        if node not in visited:
            dfs_helper_rec(graph, node)


# dfs_recursive(graph)


def dfs_iterative(graph):
    visited = set()
    stack = []

    def dfs_helper_iter(source):
        stack.append(source)
        visited.add(source)
        while len(stack) != 0:
            curr_node = stack.pop()
            print(curr_node)
            neighbors = graph[curr_node]
            for node in neighbors:
                if node not in visited:
                    visited.add(node)
                    stack.append(node)

    for source in graph.keys():
        if source not in visited:
            dfs_helper_iter(source)


dfs_iterative(graph)
