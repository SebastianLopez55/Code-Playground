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


def bfs_traversal_helper(g, source, visited):
    # Note: g is of type Graph.py class
    q = MyQueue()
    result = ""

    visited.add(source)
    q.enqueue(source)
    while not q.is_empty():

        curr_node = q.dequeue()
        result += str(curr_node)
        neighbor = g.array[curr_node].head_node
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
