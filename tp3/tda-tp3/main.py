import args
from graph.graph_factory import GraphFactory
from graph.network_flow import NetworkFlow

def main():
    # obtención de argumentos
    arguments = args.parse_arguments()
    verbose = bool(arguments.verbose)
    file = arguments.file

    # cargar grafo
    graph = GraphFactory.Load(file)

    if verbose:
        graph.print_graph()

    # procesar grafo
    network = NetworkFlow(graph)
    result = network.max_flow_min_cost(verbose)

    print(result.message)
    
if __name__ == '__main__':
    main()
