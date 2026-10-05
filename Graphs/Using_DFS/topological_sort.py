"""
Topological sort with DFS.

A topological order of a directed acyclic graph (DAG) lists the nodes so that
every edge u -> v points forward: u always appears before v.

INVARIANT: in a DAG, for every edge u -> v, finish[u] > finish[v].

DFS guarantees this by construction: it can't return from u until v has been
fully explored (either inside u's call or earlier). So listing nodes by
decreasing finish time is a topological order. The invariant only holds
without cycles: in a cycle, some edge points back to a node that hasn't
finished yet, which is how cycle detection works.

This file has two versions of the same algorithm:
  1. dfs_with_timestamps: THEORY version. Uses an explicit clock to record
                          start/finish times, then bucket-sorts nodes by
                          finish time. Makes the invariant visible: you can
                          print finish_times and check it edge by edge.
  2. topological_sort:    PRACTICAL version (what to write in an interview).
                          No clock: it appends each node the moment it
                          finishes, so the list's order IS the finish order.
                          Same invariant, it just stays implicit.

Read (1) to understand WHY (2) works. Both are O(V + E).
"""


def dfs_with_timestamps(graph):
    """
    Run DFS over the whole graph, record when each node starts and finishes,
    then use the finish times to build a topological order.

    Returns (start_times, finish_times, topo_order):
      start_times[node]  - clock value when DFS first reaches node
      finish_times[node] - clock value when DFS is done with node and
                           everything reachable from it
      topo_order         - nodes sorted by decreasing finish time

    (start/finish are the "pre" and "post" numbers from the DPV textbook.)

    Time: O(V + E). Space: O(V).
    """
    num_nodes = len(graph)
    clock = 1  # increases by 1 on every start and every finish
    visited = [False] * num_nodes
    start_times = [0] * num_nodes
    finish_times = [0] * num_nodes

    def explore(node):
        """Visit node, then recursively visit every unvisited node it points to."""
        nonlocal clock
        visited[node] = True

        # Record the moment we first reach this node.
        start_times[node] = clock
        clock += 1

        for neighbor in graph[node]:
            if not visited[neighbor]:
                explore(neighbor)

        # All descendants are done at this point, so this node is done too.
        finish_times[node] = clock
        clock += 1

    # Start a new DFS from every node not reached yet, so disconnected parts
    # of the graph are also covered.
    for start_node in graph:
        if not visited[start_node]:
            explore(start_node)

    # BUCKET SORT: build the topological order = nodes by decreasing finish time.
    # A comparison sort would cost O(V log V), but we don't need one: every
    # timestamp is a distinct integer from 1 to 2V, so we use bucket sort with
    # one bucket per timestamp (at most one node per bucket, a.k.a. pigeonhole
    # sort). Each node goes straight into the bucket numbered by its finish
    # time. Buckets for start times stay None. Reading the buckets from highest
    # to lowest gives decreasing finish time in O(V).
    slots = [None] * (2 * num_nodes + 1)  # index = timestamp, value = node
    for node in graph:
        slots[finish_times[node]] = node
    topo_order = [node for node in reversed(slots) if node is not None]

    return start_times, finish_times, topo_order


def topological_sort(graph):
    """
    Return the nodes of a DAG in topological order (every edge points forward).

    Same DFS as above, but instead of timestamps it appends each node to
    finish_order at the moment it finishes. finish_order is then sorted by
    increasing finish time; reversing it gives decreasing finish time, which
    is a topological order.

    Assumes the graph has no cycles. With a cycle there is no valid order,
    and this function will still return a list without warning.

    Time: O(V + E). Space: O(V).
    """
    visited = set()
    finish_order = []  # nodes in the order they finish (earliest first)

    def explore(node):
        """Visit everything reachable from node, then record node as finished."""
        visited.add(node)

        # Finish everything this node points to first...
        for neighbor in graph[node]:
            if neighbor not in visited:
                explore(neighbor)

        # ...so by the time we get here, every node after this one in the
        # topological order is already in finish_order. This line is the
        # equivalent of "finish_times[node] = clock" above.
        finish_order.append(node)

    for start_node in graph:
        if start_node not in visited:
            explore(start_node)

    # Last to finish comes first in the topological order.
    return finish_order[::-1]


# Adjacency list: node -> list of nodes it has an edge to.
graph = {0: [1, 2, 3], 1: [4], 2: [], 3: [], 4: [5], 5: [6], 6: []}

"""
Graph G (all edges point downward):

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

start_times, finish_times, clock_order = dfs_with_timestamps(graph)

print("\n== Topological Sort w/ Clock==\n")
print("Finish times: ", finish_times)
print(" -> ".join(str(node) for node in clock_order))
print()

print("== Topological Sort w/o Clock== \n")
order = topological_sort(graph)
print(" -> ".join(str(node) for node in order))
