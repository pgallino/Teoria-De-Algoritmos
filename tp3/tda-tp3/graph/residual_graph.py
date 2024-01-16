import sys

from graph.dijkstra import dijkstra_algorithm, path_between
from graph.graph import Graph
from graph.min_path_result import MinPathResult
from graph.edge import REVERSE_TYPE
import copy


def find_bottleneck_of(path, graph):
    bottleneck = sys.maxsize
    for i in range(len(path) - 1):  # voy tomando las parejas de nodos y le resto o sumo el bottleneck a las aristas
        edge = graph.get_edge(path[i], path[i + 1])
        if bottleneck > edge.capacity:
            bottleneck = edge.capacity
    return bottleneck


class ResidualGraph(Graph):

    def __init__(self, graph):
        super().__init__()
        self.__dict__ = copy.deepcopy(graph.__dict__)
        self.path_count = 2
        new_edges = []

        for node in self.graph:
            for edges in self.graph[node]:
                for dest_node in edges:
                    new_edges.append([dest_node, node, (edges[dest_node].cost * -1) + graph.max_cost, 0, REVERSE_TYPE])

        for edge in new_edges:
            self.add_edge(edge[0], edge[1], edge[2], edge[3], edge[4])

    # TODO test it!
    def found_min_path(self):
        previous_nodes, _ = dijkstra_algorithm(self)
        if len(previous_nodes) == 0:
            return MinPathResult(False)
        path = path_between(previous_nodes, self)
        bottleneck = find_bottleneck_of(path, self)
        return MinPathResult(True, path, bottleneck)

    def update(self, path, bottleneck):  # pedro
        for i in range(len(path) - 1):  # voy tomando las parejas de nodos y le resto o sumo el bottleneck a las aristas
            edge = self.get_edge(path[i], path[i + 1])
            reversed_edge = self.get_edge(path[i + 1], path[i])
            if edge.edge_type == REVERSE_TYPE:
                edge.capacity += bottleneck
                reversed_edge.capacity -= bottleneck
            else:
                edge.capacity -= bottleneck
                reversed_edge.capacity += bottleneck

    def get_min_cost(self):  # pedro
        min_cost = 0
        for node in self.nodes:
            for adjacent in self.graph[node]:
                edge = adjacent[list(adjacent.keys())[0]]
                if edge.edge_type == REVERSE_TYPE:
                    min_cost += (edge.cost - self.max_cost) * edge.capacity * -1
        return min_cost

    def get_max_flow(self):  # pedro
        node = self.finish_node
        max_flow = 0
        for adjacent in self.graph[node]:
            edge = adjacent[list(adjacent.keys())[0]]
            if edge.edge_type == REVERSE_TYPE:
                max_flow += edge.capacity
        return max_flow
