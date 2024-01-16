import args
from graph.graph_factory import GraphFactory

def main():
    # obtención de argumentos
    arguments = args.parse_arguments()
    verbose = bool(arguments.verbose)
    file = arguments.file

    # cargar grafo
    graph = GraphFactory.Load(file)

    # procesar grafo
    result = graph.verify_negative_cycles(verbose)

    if verbose:
        graph.print_graph()

    if result.found:
        print(result.message + ". " + result.cycle + " → costo:" + str(result.weight))
    else:
        print(result.message)
    
if __name__ == '__main__':
    main()
