import sys
sys.path.append('../')

from graph.graph_factory import GraphFactory


def instance_one():
    graph = GraphFactory.Load("./test/examples/case-01.txt")
    return graph

def instance_two():
    graph = GraphFactory.Load("./test/examples/case-02.txt")
    return graph

#def instance_three():
#    graph = GraphFactory.Load("./test/examples/case-03.txt")
#    return graph
#
# def instance_four():
#    graph = GraphFactory.Load("./test/examples/case-04.txt")
#    return graph
#
# def instance_five():
#    graph = GraphFactory.Load("./test/examples/case-05.txt")
#    return graph
#
# def instance_six():
#    graph = GraphFactory.Load("./test/examples/case-06.txt")
#    return graph
#
# def instance_seven():
#    graph = GraphFactory.Load("./test/examples/case-07.txt")
#    return graph
#
# def instance_eight():
#    graph = GraphFactory.Load("./test/examples/case-08.txt")
#    return graph
#
# def instance_nine():
#    graph = GraphFactory.Load("./test/examples/case-09.txt")
#    return graph
