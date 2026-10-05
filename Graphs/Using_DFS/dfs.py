"""
Depth-first search (DFS): recursive vs. iterative.

DFS goes as deep as possible along one path before backing up to try the
next branch. Each node is visited once, so it runs in O(V + E) time with
O(V) extra space for the visited set and the call stack / explicit stack.

The outer loop over every node starts a new DFS from any node not reached
yet, so nodes that can't be reached from the first node are still visited.

1. dfs_recursive: the textbook version. The call stack remembers where to
   return to after finishing a branch. Visit order here: 0 1 4 5 6 2 3.

2. dfs_iterative: replaces recursion with an explicit stack (useful when the
   graph is deep enough to hit Python's recursion limit, ~1000 by default).
   Neighbors are pushed and the LAST one pushed is popped first, so siblings
   are visited right to left. Visit order here: 0 3 2 1 4 5 6.

   Note: it marks nodes visited when PUSHED, not when popped. That still
   visits every node exactly once, but it is not a true DFS order (a node can
   be claimed by an earlier push before the deeper path reaches it). Fine for
   "visit everything", but don't use this version for algorithms that rely on
   DFS order or finish times (topological sort, cycle detection, SCCs).
"""

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


print("dfs recursive:")
dfs_recursive(graph)


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


print("dfs iterative:")
dfs_iterative(graph)
