from unittest import TestCase
from test.graph_mocks_factory import instance_one, instance_two
from graph.network_flow import NetworkFlow


class TestGraphMaxFlowMinCost(TestCase):

    # Caso uno: 
    def test_max_flow_min_cost_with_instance_one(self):
        # given
        graph = instance_one()
        network = NetworkFlow(graph)

        # when
        result = network.max_flow_min_cost()

        # then
        self.then_the_expected_result_for_instance_one_is_flow_50_cost_160(result)

    def then_the_expected_result_for_instance_one_is_flow_50_cost_160(self, result):
        self.assertEqual(result.flow, 50)
        self.assertEqual(result.cost, 160)

    # Caso dos: 
    def test_max_flow_min_cost_with_instance_two(self):
        # given
        graph = instance_two()
        network = NetworkFlow(graph)
        
        # when
        result = network.max_flow_min_cost()

        # then
        self.then_the_expected_result_for_instance_one_is_flow_60_cost_205(result)

    def then_the_expected_result_for_instance_one_is_flow_60_cost_205(self, result):
        self.assertEqual(result.flow, 60)
        self.assertEqual(result.cost, 205)
