from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        # Pop node from frontier set
        node = frontier.pop()

        # Find the popped node's neighbors
        node_neighbors = graph[node]

        # Update result and frontier sets
        result.add(node)
        frontier.update(node_neighbors)
        frontier -= result

    return result





def connected(graph):
    # Get random node from graph and get set of all reachable nodes from said node
    root_node = next(iter(graph))
    reachable_nodes = reachable(graph, root_node)

    # Make sure the set of reachable nodes includes all the nodes in the graph
    if reachable_nodes == set(graph.keys()):
        return True
    else:
        return False





def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    # Create a list of all nodes in graph
    nodes = set(graph.keys())
    # Create reachable set using a root_node that has been removed from nodes list
    root_node = nodes.pop()
    reachable_nodes = reachable(graph, root_node)
    # Remove all nodes that are known to be reachable from nodes set or avoid
    nodes -= reachable_nodes
    # Create set of reachable_nodes initialized reachable_nodes
    reachable_nodes_set = set()
    reachable_nodes_set.add(frozenset(reachable_nodes))

    # iterate through each node in remaining in nodes set and do remove node and add to reachable nodes set like above
    while nodes:
        root_node = nodes.pop()
        new_reachable_nodes = reachable(graph, root_node)
        nodes -= new_reachable_nodes
        reachable_nodes_set.add((frozenset(new_reachable_nodes)))

    # return length of number of reachable node lists aka components
    return len(reachable_nodes_set)


