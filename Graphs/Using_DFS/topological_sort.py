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


pre, post = dfs(graph)
for node in graph:
    print(f"\nNode {node} traversal label [{pre[node]}, {post[node]}]")
print()


print("== Topological Sort == \n")
top_sort_stack = topological_sort(graph)
while top_sort_stack:
    current_node = top_sort_stack.pop()
    if top_sort_stack:
        print(f"{current_node} -> ", end="")
    else:
        print(f"{current_node}")
