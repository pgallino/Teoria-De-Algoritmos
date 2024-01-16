from unittest import TestCase
from test.graph_mocks_factory import instance_one, instance_two, instance_three, instance_four, instance_five, \
instance_six, instance_seven, instance_eight, instance_nine

class TestGraphNegativeCycles(TestCase):

    # Caso uno: Grafo de 7 nodos con un ciclo negativo de coste -4
    def test_one_negative_cycle_with_instance_one(self):
        # given
        graph = instance_one()
        cycle_1 = ["A","C","D","F","G"]
        cycles = [cycle_1]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_one_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_one_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message) # costo: -4
        self.assertTrue(exists_at_least_one_cycle(result.cycle, cycles))
        self.assertEqual(result.weight, -4)


    # Caso dos: Grafo de 7 nodos SIN ciclos negativos
    def test_no_negative_cycles_with_instance_two(self):
        # given
        graph = instance_two()

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_two_is_negative_cycle_not_found(result)

    def then_the_expected_result_for_instance_two_is_negative_cycle_not_found(self, result):
        self.assertFalse(result.found)
        self.assertEqual("No existen ciclos negativos en el grafo", result.message)


    # Caso tres: Grafo de 7 nodos 
    def test_no_negative_cycles_with_instance_three(self):
        # given
        graph = instance_three()

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_three_is_negative_cycle_not_found(result)

    def then_the_expected_result_for_instance_three_is_negative_cycle_not_found(self, result):
        self.assertFalse(result.found)
        self.assertEqual("No existen ciclos negativos en el grafo", result.message)


    # Caso cuatro: Grafo con un ciclo negativo 
    def test_no_negative_cycles_with_instance_four(self):
        # given
        graph = instance_four()
        cycle_1 = ["B", "C"]
        cycles = [cycle_1]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_four_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_four_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message)
        self.assertTrue(exists_at_least_one_cycle(result.cycle, cycles))
        self.assertEqual(result.weight, -4)


    # Caso cinco: Grafo de con un ciclo negativo
    def test_negative_cycles_with_instance_five(self):
        # given
        graph = instance_five()
        cycle_1 = ["8", "7", "5"]
        cycles = [cycle_1]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_five_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_five_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message)
        self.assertTrue(exists_at_least_one_cycle(result.cycle, cycles))
        self.assertEqual(result.weight, -2)

    # Caso seis: Grafo de con un nodo perteneciente a dos ciclos negativos
    def test_negative_cycles_with_instance_six(self):
        # given
        graph = instance_six()
        cycle_1 = [["B", "C"], -4]
        cycle_2 = [["B", "E"], -4]
        cycles = [cycle_1, cycle_2]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_six_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_six_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message)
        self.assertTrue(exists_at_least_one_cycle_with_weight(result, cycles))


    # Caso siete: Grafo de con dos ciclos negativos
    def test_negative_cycles_with_instance_seven(self):
        # given
        graph = instance_seven()
        cycle_1 = [["4", "3", "1"], -1]
        cycle_2 = [["5", "7", "8"], -2] 
        cycles = [cycle_1, cycle_2]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_seven_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_seven_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message)
        self.assertTrue(exists_at_least_one_cycle_with_weight(result, cycles))


    # Caso ocho: Grafo sin ciclos
    def test_negative_cycles_with_instance_eight(self):
        # given
        graph = instance_eight()

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_eight_is_negative_cycle_not_found(result)

    def then_the_expected_result_for_instance_eight_is_negative_cycle_not_found(self, result):
        self.assertFalse(result.found)
        self.assertEqual("No existen ciclos negativos en el grafo", result.message)

    # Caso nueve: Grafo con tres ciclos negativos
    def test_negative_cycles_with_instance_nine(self):
        # given
        graph = instance_nine()
        cycle_1 = [["B", "C"], -4]
        cycle_2 = [["B", "E"], -4]
        cycle_3 = [["F", "A", "G"], -9]
        cycles = [cycle_1, cycle_2, cycle_3]

        # when
        result = graph.verify_negative_cycles()

        # then
        self.then_the_expected_result_for_instance_eight_is_negative_cycle_found(result, cycles)

    def then_the_expected_result_for_instance_eight_is_negative_cycle_found(self, result, cycles):
        self.assertTrue(result.found)
        self.assertTrue("Existe al menos un ciclo negativo en el grafo" in result.message)
        self.assertTrue(exists_at_least_one_cycle_with_weight(result, cycles))


def exists_at_least_one_cycle(result, cycles):
    return any(exists_nodes_in_cycle(cycle, result) for cycle in cycles)

def exists_at_least_one_cycle_with_weight(result, cycles):
    return any(exists_nodes_in_cycle(cycle[0], result.cycle) and (cycle[1] == result.weight) for cycle in cycles)

def exists_nodes_in_cycle(nodes, cycle):
    return all(node in cycle for node in nodes)