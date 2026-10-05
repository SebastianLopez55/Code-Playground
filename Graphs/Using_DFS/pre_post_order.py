"""
DFS pre/post numbers (start and finish times).

A single clock increases by 1 at two moments for every node:
  pre[node]  - when DFS first reaches node (start)
  post[node] - when DFS is done with node and everything reachable from it
               (finish)
So with V nodes the timestamps run 1..2V and are all distinct.

Parenthesis property: for any two nodes, their [pre, post] intervals are
either nested (one is a descendant of the other in the DFS tree) or disjoint
(neither is reached from the other in this DFS). They never partially
overlap. For this graph:

  0 [1 ......................... 14]
  1   [2 ........... 9]
  4     [3 ..... 8]
  5       [4 . 7]
  6         [5 6]
  2                  [10 11]
  3                          [12 13]

These numbers are the base for other DFS algorithms:
  - topological sort: list nodes by decreasing post number
  - cycle detection:  an edge to a node that has started but not finished
  - Kosaraju's SCCs:  the node with the highest post number is in a "source"
                      component

Time: O(V + E). Space: O(V).
(Same function as dfs_with_timestamps in topological_sort.py.)
"""

graph = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: []}

"""
Graph G: 

       0
   /   |   \
  1    2    3
  |
  4
  |
  5
  |
  6
  
"""


def dfs(graph):
    n = len(graph)
    clock = 1
    visited = [False] * n
    preorder, postorder = [0] * n, [0] * n

    def explore(node):
        nonlocal clock
        visited[node] = True
        preorder[node] = clock
        clock += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                explore(neighbor)

        postorder[node] = clock
        clock += 1

    for source in graph:
        if not visited[source]:
            explore(source)

    return preorder, postorder


pre, post = dfs(graph)
for node in graph:
    print(f"\nNode {node} traversal label [{pre[node]}, {post[node]}]")
