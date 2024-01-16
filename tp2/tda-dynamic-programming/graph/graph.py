from graph.negative_cycle_result import NegativeCycleResult

BIG_NUMBER = 10000

class Graph:

    def __init__(self, start):
        self.initial_node = start
        self.graph = {}
        self.nodes_count = 0
        self.nodes = []
        self.negative_cycles_candidate = []
        self.add_node(start)

    def add_node(self, node):
        if node not in self.graph:
            self.nodes.append(node)
            self.nodes_count = self.nodes_count + 1
            self.graph[node] = []

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.add_node(from_node)
        
        if to_node not in self.graph:
            self.add_node(to_node)

        origin = [from_node, weight]
        if origin not in self.graph[to_node]:
            self.graph[to_node].append(origin)

    def print_graph(self):
        print("Start Node: ", self.initial_node)
        print("Nodes Count: ", self.nodes_count)
        print("Graph Edges List:")
        for node in self.nodes:
            for edges in self.graph[node]:
                print(edges[0], "\t -> \t", node, "\tweight:\t", edges[1])
        
        print("Node Edges List:")
        for node in self.nodes:
            print(node, self.graph[node])

    def verify_negative_cycles(self, verbose=False):
        matrix = self.initialize_matrix()
        matrix = self.iterate_matrix(matrix)

        negative_cycle_found = self.exist_negative_cycle(matrix)

        if verbose:
            print_matrix(matrix, self.nodes)
            print("Candidatos a pertenecer a un ciclo negativo")
            print(self.negative_cycles_candidate)

        if negative_cycle_found:
            cycle, weight = self.get_negative_cycle(matrix)
            return NegativeCycleResult(True, "Existe al menos un ciclo negativo en el grafo", cycle_str(cycle), weight)
        else:
            return NegativeCycleResult(False, "No existen ciclos negativos en el grafo")

    def initialize_matrix(self):
        # initialize first row of the matrix with zero for the start node
        matrix = []
        first_row = []
        for node in self.nodes:
            if node != self.initial_node:
                first_row.append((BIG_NUMBER,node,BIG_NUMBER))
            else:
                first_row.append((0,node,0))

        matrix.append(first_row)

        return matrix

    def iterate_matrix(self, matrix):
        # iterate n times the matrix
        for i in range(self.nodes_count):
            previous_row = matrix[i]
            new_row = []

            for idx, node in enumerate(self.nodes):
                new_path_weight = (previous_row[idx][0], node, 0)

                for edge in self.graph[node]:
                    previous_node = edge[0]
                    idx = self.nodes.index(previous_node)
                    path_weight_previous_node = previous_row[idx][0]

                    if new_path_weight[0] > path_weight_previous_node + edge[1]:
                          if path_weight_previous_node != BIG_NUMBER and path_weight_previous_node != BIG_NUMBER:
                              new_path_weight = (path_weight_previous_node + edge[1], previous_node, edge[1])

                new_row.append(new_path_weight)

            matrix.append(new_row)

        return matrix

    def exist_negative_cycle(self, matrix):
        # verity an improvement in the last two rows
        last_row_idx = self.nodes_count

        result = False
        for i in range(self.nodes_count):
            if matrix[last_row_idx][i][0] < matrix[last_row_idx - 1][i][0]:
                result = True
                self.negative_cycles_candidate.append(self.nodes[i])
        return result

    def get_negative_cycle(self, matrix):
        
        row_idx = self.nodes_count

        found = False
        candidate_idx = 0
        while (candidate_idx < len(self.negative_cycles_candidate)) and not found:
            candidate = self.negative_cycles_candidate[candidate_idx]
            previous = candidate
            cycle = [previous]
            weight = []

            while (row_idx > 0) and not found:
                weight.append(matrix[row_idx][self.nodes.index(previous)][2])
                previous = matrix[row_idx][self.nodes.index(previous)][1]

                if previous not in cycle:
                    cycle.append(previous)
                else:
                    # ya existe y hay que cortar
                    idx = cycle.index(previous)
                    cycle = cycle[idx:]
                    weight = weight[idx:]
                    found = True
                
                row_idx = row_idx - 1 
            candidate_idx = candidate_idx + 1

        return (cycle, sum(weight))


def print_matrix(matrix, nodes):
    print("\nit", nodes)
    for i in range(len(matrix)):
        print(i, " ", matrix[i])
    print("\n")


def cycle_str(cycle):
    return ",".join(cycle)