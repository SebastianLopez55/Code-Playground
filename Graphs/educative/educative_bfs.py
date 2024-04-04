from Graph import Graph
from Queue import MyQueue

# You can check the input graph in console tab


# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex
def bfs_helper(g, source, visited):
    # visited = set()
    q = MyQueue()
    traversed = ""

    q.enqueue(source)
    visited.add(source)
    while not q.is_empty():
        curr_node = q.dequeue()
        neighbor = g.array[curr_node].head_node
        traversed += str(curr_node)
        while neighbor is not None:
            if neighbor.data not in visited:
                visited.add(neighbor.data)
                q.enqueue(neighbor.data)
            neighbor = neighbor.next_element

    return traversed, visited


def bfs_traversal(g, source):
    visited = set()
    all_traversed = ""

    if g.vertices == 0:
        return all_traversed

    all_traversed, visited = bfs_helper(g, source, visited)

    for i in range(g.vertices):
        if i not in visited:
            traversed, visited = bfs_helper(g, i, visited)
            all_traversed += traversed

    return all_traversed


g = Graph(4)
num_of_vertices = g.vertices
if num_of_vertices is 0:
    print("Graph is empty")
elif num_of_vertices < 0:
    print("Graph cannot have negative vertices")
else:
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    print(bfs_traversal(g, 0))
    assert bfs_traversal(g, 0) == "0213"
