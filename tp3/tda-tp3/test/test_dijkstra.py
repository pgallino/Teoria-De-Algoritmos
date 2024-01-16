from unittest import TestCase

from graph.dijkstra import dijkstra_algorithm, path_between
from graph.residual_graph import ResidualGraph
from test.graph_mocks_factory import instance_one


class Test(TestCase):

    # TODO
    #  1 - meter test con aristas sin capacidad
    #  2 - que no exista un camino minimo posible
    #  3 -
    def test_dijkstra_algorithm(self):
        # given
        graph = instance_one()
        residual = ResidualGraph(graph)

        # when
        previous_nodes, shortest_path = dijkstra_algorithm(residual)
        path = path_between(previous_nodes, residual)

        # when
        expected_path = ['B', 'A', 'C']
        self.assertEqual(expected_path, path)
