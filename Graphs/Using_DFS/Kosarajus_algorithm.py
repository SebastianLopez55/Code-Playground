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
