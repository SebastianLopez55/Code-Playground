"""
Cycle detection in a directed graph with DFS.

Each node is in one of three states:
  unvisited  - DFS hasn't reached it
  visiting   - DFS has started it but not finished (it's on the current path,
               i.e. the recursion stack)
  visited    - DFS has finished it and everything reachable from it

Key idea: while exploring, if we follow an edge to a node that is still
"visiting", that node is an ancestor on the current path, so the edge closes
a loop -> cycle. (In pre/post terms: an edge to a node that has started but
not finished. This is a "back edge".) An edge to a "visited" node is safe:
that node is fully finished, so it can't lead back to the current path.

In a DAG this never happens, which is exactly why the topological sort
invariant finish[u] > finish[v] holds for every edge u -> v.

Note: for an undirected graph, "visited" alone is not enough either; there
you ignore the edge back to the parent instead of using three states.

Time: O(V + E) when finished nodes are added to `visited` (see below).
Space: O(V) for the two sets and the recursion stack.

Heads-up on this implementation:
  - dfs() never adds a node to `visited`, so the `node in visited` check is
    never true. It is still correct, but a finished node can be re-explored
    from every path that reaches it, which can blow up far past O(V + E) in
    graphs with many paths. Fix: `visited.add(node)` right after
    `visiting.remove(node)`.
  - `visiting.add(node)` appears twice; the second call does nothing.
"""

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
