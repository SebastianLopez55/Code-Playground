from Graph import Graph
from Queue import MyQueue

# This implementation of bfs also works for graphs with disconnected components.


def bfs_traversal_helper(g, source, visited):
    # Note: g is of type Graph.py class
    q = MyQueue()
    result = ""

    # Mark source as visited and enqueue
    visited.add(source)
    q.enqueue(source)

    # Main BFS loop
    while not q.is_empty():
        curr_node = q.dequeue()
        result += str(curr_node)
        neighbor = g.array[curr_node].head_node

        # Add curr_node's children to queue() and mark it as visited.
        while neighbor is not None:
            if neighbor.data not in visited:
                q.enqueue(neighbor.data)
                visited.add(neighbor.data)
            neighbor = neighbor.next_element

    return result, visited


def bfs_traversal(g, source):
    result, visited = "", set()

    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result

    # Explore from given source
    result, visited = bfs_traversal_helper(g, source, visited)

    # visit remaining nodes
    for i in range(num_of_vertices):
        if i not in visited:
            result_new, visited = bfs_traversal_helper(g, i, visited)
            result += result_new

    return result


# TEST CASES

# Create the graph
graph = Graph(4)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

# Expected Output: "0 2 1 3" (or any other order that correctly represents BFS traversal from vertex 0)
print(bfs_traversal(graph, 0))


# Create the graph
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(3, 4)
graph.add_edge(4, 5)

# Expected Output: "0 1 2 3 4 5" (starting from vertex 0, then jumping to new components as necessary)
print(bfs_traversal(graph, 0))


# Create the graph
graph = Graph(3)  # 3 vertices, but no edges added

# Expected Output: "0 1 2" (each vertex by itself, since there are no edges)
print(bfs_traversal(graph, 0))
