import unittest
# from binary_search import binary_search_interface
from mutants.m3 import binary_search_interface


class TestBinarySearchOrderBehaviour(unittest.TestCase):

    def test_ascending_random_list(self):
        input_list_SI = [1, 2, 3, 4, 5]
        input_list_FI = [3, 1, 2, 5, 4]
        target_value = 2
        expected_index = 1
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)

    def test_SI_equals_FI_with_duplicates(self):
        input_list_SI = [1, 2, 2, 3, 3, 3]
        input_list_FI = [3, 1, 2, 5, 4, 2]
        target_value = 2
        expected_index = 2
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)

    def test_descending_order(self):
        input_list_SI = [5, 4, 3, 2, 1]  # SI
        input_list_FI = [1, 2, 3, 4, 5]  # FI
        target_value = 4
        expected_index = 3
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)

    def test_with_large_values(self):
        input_list_SI = [200, 1000, 500, 30000, 90000]  # SI
        input_list_FI = [500, 1000, 200, 90000, 30000]  # FI
        target_value = 500
        expected_index = 1
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)


if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()
