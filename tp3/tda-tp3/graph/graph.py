from graph.edge import Edge, DIRECT_TYPE


class Graph:

    def __init__(self, start=None, end=None):
        self.initial_node = start
        self.finish_node = end
        self.graph = {}
        self.nodes_count = 0
        self.nodes = []
        self.max_cost = 0
        if start is not None:
            self.add_node(start)
        if end is not None:
            self.add_node(end)

    def add_node(self, node):
        if node not in self.graph:
            self.nodes.append(node)
            self.nodes_count = self.nodes_count + 1
            self.graph[node] = []

    def add_edge(self, from_node, to_node, cost, capacity, edge_type=DIRECT_TYPE):
        if from_node not in self.graph:
            self.add_node(from_node)

        if to_node not in self.graph:
            self.add_node(to_node)

        adjacent = {to_node: Edge(edge_type, capacity, cost)}

        if adjacent not in self.graph[from_node]:
            self.graph[from_node].append(adjacent)

        if self.max_cost < cost:
            self.max_cost = cost

    def get_edge(self, from_node, to_node):  # pedro
        for adjacent in self.graph[from_node]:
            if list(adjacent.keys())[0] == to_node:
                return adjacent[to_node]

    def print_graph(self):
        print("Start Node: ", self.initial_node)
        print("End Node: ", self.finish_node)
        print("Nodes Count: ", self.nodes_count)
        print("\n")
        print("Graph Edges List:")
        for node in self.nodes:
            for edges in self.graph[node]:
                for dest_node in edges:
                    print(node, "\t->\t", dest_node, "\tcost:\t", edges[dest_node].cost, "\tcapacity:\t",
                          edges[dest_node].capacity)
        print("\n")
        print("Node Edges List:")
        print("\n")
        for node in self.nodes:
            print(node, self.graph[node])
        print("\n")
