from graph.max_flow_min_cost_result import MaxFlowMinCostResult
from graph.residual_graph import ResidualGraph


class NetworkFlow:

    def __init__(self, graph):
        self.graph = graph

    def max_flow_min_cost(self, verbose=False):
        residual = ResidualGraph(self.graph)
        if verbose:
            print("Grafo Residual:")
            residual.print_graph()

        path_found = True
        while path_found:
            path_result = residual.found_min_path()
            path_found = path_result.found
            if path_found:
                residual.update(path_result.path, path_result.bottleneck)

        max_flow = residual.get_max_flow()
        min_cost = residual.get_min_cost()
        return MaxFlowMinCostResult(True, max_flow, min_cost)
