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
print()

# Toposort
post_map = {}
for i, post_num in enumerate(post):
    post_map[post_num] = i
sorted_keys = sorted(post_map.keys(), reverse=True)

toposort = []
for key in sorted_keys:
    toposort.append(post_map[key])

print(f"Topological sort starting from source: {toposort}")
