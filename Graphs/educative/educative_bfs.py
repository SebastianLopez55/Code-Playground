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


def test_bfs():
    # Test Case 1: Simple Connected Graph
    g1 = Graph(4)
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 3)
    g1.add_edge(2, 3)
    print("Output:", bfs_traversal(g1, 0))
    assert bfs_traversal(g1, 0) == "0213", "Test Case 1 Failed"

    # Test Case 2: Graph with Disconnected Components
    g2 = Graph(5)  # Adding an extra vertex to introduce a disconnected component
    g2.add_edge(0, 1)
    g2.add_edge(0, 2)
    g2.add_edge(1, 3)
    g2.add_edge(2, 3)
    # Assuming bfs_traversal modifies its behavior for disconnected components
    print("Output:", bfs_traversal(g2, 0))
    assert bfs_traversal(g2, 0) == "02134", "Test Case 2 Failed"

    # Test Case 3: An Empty Graph
    g3 = Graph(0)
    print("Output:", None if bfs_traversal(g3, 0) == "" else bfs_traversal(g3, 0))
    assert bfs_traversal(g3, 0) == "", "Test Case 3 Failed"

    print("\nAll test cases passed!")


# Assuming we're calling the test function to execute tests
test_bfs()
