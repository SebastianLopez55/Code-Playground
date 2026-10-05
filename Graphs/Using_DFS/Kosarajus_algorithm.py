"""
Kosaraju's algorithm: strongly connected components (SCCs).

A strongly connected component is a maximal group of nodes where every node
can reach every other node. Shrinking each SCC to a single node always gives
a DAG (the "condensation" graph), because any cycle between components would
merge them into one.

Algorithm (two DFS passes):
  1. DFS on the original graph and record nodes in finish order (the same
     append-on-finish trick as topological_sort). The node that finishes
     LAST is always in a "source" SCC of the condensation: no other SCC has
     an edge into it.
  2. Transpose the graph (reverse every edge). Now that source SCC becomes a
     "sink": its nodes can't reach any other SCC.
  3. Pop nodes from latest finish to earliest. Each time we hit an unvisited
     node, DFS in the transposed graph from it. Because its SCC is a sink in
     the reversed graph (and SCCs found earlier are already visited), the
     DFS collects exactly that one SCC and nothing else.

Why "topological_sort" on a graph that may have cycles: the order is not a
true topological order then, but the finish order still puts the source
SCCs last, which is all step 3 needs.

Examples:
  graph1 has no cycles, so every node is its own SCC -> 7 components.
  graph2 adds 6 -> 1, creating the cycle 1 -> 4 -> 5 -> 6 -> 1, so
  {1, 4, 5, 6} merge into one SCC -> 4 components.

Time: O(V + E) (two DFS passes + building the transpose).
Space: O(V + E) for the transposed graph.
"""

graph1 = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: []}
graph2 = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: [1]}


"""
Graph G: directed 

       0
   /   |   \
  v    v    v
  1    2    3
  |
  v
  4
  |
  v
  5
  |
  v
  6
  
"""


def topological_sort(graph):
    visited = set()
    stack = []

    def explore(node):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor)

        stack.append(node)

    for source in graph:
        if source not in visited:
            explore(source)

    return stack


def transpose_graph(graph):
    transposed = {node: [] for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            transposed[neighbor].append(node)
    return transposed


def kosarajus_scc(graph):
    stack_topsort = topological_sort(graph)
    graph_rev = transpose_graph(graph)
    visited = set()
    sccs = []

    def explore(node, scc):
        visited.add(node)
        scc.append(node)
        for neighbor in graph_rev[node]:
            if neighbor not in visited:
                explore(neighbor, scc)

    while stack_topsort:
        source = stack_topsort.pop()
        if source not in visited:
            scc = []
            explore(source, scc)
            sccs.append(scc)

    return sccs


print(
    f"\nGraph 1 has {len(kosarajus_scc(graph1))} strongly connected components which are:",
    kosarajus_scc(graph1),
)

print(
    f"\nGraph 2 has {len(kosarajus_scc(graph2))} strongly connected components which are:",
    kosarajus_scc(graph2),
)
