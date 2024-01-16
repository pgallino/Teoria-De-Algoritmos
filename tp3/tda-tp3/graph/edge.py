DIRECT_TYPE = "D"
REVERSE_TYPE = "R"


class Edge:
    def __init__(self, edge_type, capacity, cost):
        self.edge_type = edge_type
        self.capacity = capacity
        self.cost = cost

    def __repr__(self):
        return str([self.edge_type, self.capacity, self.cost])
