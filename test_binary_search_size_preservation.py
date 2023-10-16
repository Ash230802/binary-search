import unittest
import random
from mutants.m3 import binary_search_interface


class TestBinarySearchSizePreservation(unittest.TestCase):
    def test_size_list(self):
        input_list_SI = [8, 3, 1, 5, 6]  # SI
        input_list_FI = [8, 3, 1, 5, 6, 9]  # FI
        target_value = 3
        expected_index = 1
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)

    def test_with_large_sorted_list(self):
        input_list_SI = list(range(1000))  # SI
        input_list_FI = list(range(700))  # FI
        target_value = 500
        expected_index = 500
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)
        print(f"SI result: {result_SI}")
        print(f"FI result: {result_FI}")

    def test_with_large_shuffled_list(self):
        input_list_SI = list(range(1000))  # SI
        input_list_FI = list(range(800))  # FI
        random.shuffle(input_list_SI)
        random.shuffle(input_list_FI)
        target_value = 750
        expected_index = 750
        result_SI = binary_search_interface(input_list_SI, target_value)
        result_FI = binary_search_interface(input_list_FI, target_value)
        self.assertEqual(result_SI, expected_index)
        self.assertEqual(result_FI, expected_index)
        # Check if SI and FI results are the same
        self.assertEqual(result_SI, result_FI)
        print(f"SI result: {result_SI}")
        print(f"FI result: {result_FI}")


if __name__ == '__main__':
    unittest.main()
