import sys


## B [{'A': ['D', 40, 1]}, {'G': ['D', 10, 1]}]
##C [{'A': ['R', 0, 0]}, {'F': ['R', 0, 0]}]
##A [{'C': ['D', 55, 2]}, {'B': ['R', 0, 1]}, {'G': ['R', 0, 1]}]
##G [{'A': ['D', 35, 1]}, {'F': ['D', 5, 2]}, {'B': ['R', 0, 1]}]
##F [{'C': ['D', 15, 2]}, {'G': ['R', 0, 0]}]

## TODO el camino de costo minimo tiene que tener capacidad distinta de 0.
def dijkstra_algorithm(graph):
    unvisited_nodes = list(graph.nodes)

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value

    # However, we initialize the starting node's value with 0
    start_node = graph.initial_node
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.graph[current_min_node]  # [{'A': ['D', 40, 1]}, {'G': ['D', 10, 1]}]
        for neighbor in neighbors:  # 'A': ['D', 40, 1]
            neighbor_destiny_node = list(neighbor.keys())[0]
            edge_destiny = neighbor[neighbor_destiny_node]  # ['D', 40, 1]
            if edge_destiny.capacity > 0:
                tentative_value = shortest_path[current_min_node] + edge_destiny.cost
                if tentative_value < shortest_path[neighbor_destiny_node]:
                    shortest_path[neighbor_destiny_node] = tentative_value
                    # We also update the best path to the current node
                    previous_nodes[neighbor_destiny_node] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


# previous_nodes {'A': 'B', 'G': 'B', 'C': 'A', 'F': 'G'}
# shortest_path {'B': 0, 'C': 3, 'A': 1, 'G': 1, 'F': 3}
def path_between(previous_nodes, graph):
    path = []
    finish_node = graph.finish_node
    initial_node = graph.initial_node

    while finish_node != initial_node:
        path.append(finish_node)
        finish_node = previous_nodes[finish_node]

    # Add the start finish_node manually
    path.append(initial_node)
    path.reverse()
    return path
