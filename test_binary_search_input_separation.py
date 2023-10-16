import unittest
# from binary_search import binary_search_interface
from mutants.m3 import binary_search_interface


class TestBinarySearchInputSeparation(unittest.TestCase):

    def test_list_SI_and_FI(self):
        SI_list = [7, 0, 5, 3, 8]
        FI_input = "7 0 5 3 8"
        FI_list = list(map(int, FI_input.split()))
        target_value = 3

        result_SI = binary_search_interface(SI_list, target_value)
        result_FI = binary_search_interface(FI_list, target_value)

        self.assertEqual(result_SI, 1)
        self.assertEqual(result_FI, 1)
        self.assertEqual(result_SI, result_FI)

    def test_with_one_comma(self):
        SI = [1, 2, 3, 4, 5]
        FI = "1 2 3, 4 5"
        FI_omit_comma = FI.replace(",", "")
        FI_list = list(map(int, FI_omit_comma.split()))
        target_value = 3
        SO = binary_search_interface(SI, target_value)
        FO = binary_search_interface(FI_list, target_value)
        self.assertEqual(SO, FO)

    def test_with_no_space(self):
        SI = [1, 2, 3, 4, 5]
        FI = "12345"
        FI_list = list(map(int, FI.split()))
        target_value = 3
        SO = binary_search_interface(SI, target_value)
        FO = binary_search_interface(FI_list, target_value)
        self.assertNotEqual(SO, FO)

    def test_empty_input(self):
        SI = []
        FI = ""
        target_value = 3
        SO = binary_search_interface(SI, target_value)
        FO = binary_search_interface(FI, target_value)
        self.assertEqual(SO, FO)

    def test_at_random(self):
        SI = [1, 2, 3, 4, 5]
        FI = "3 1 4 5 2"
        FI_list = list(map(int, FI.split()))
        target_value = 3
        SO = binary_search_interface(SI, target_value)
        FO = binary_search_interface(FI_list, target_value)
        self.assertEqual(SO, FO)


if __name__ == '__main__':
    unittest.main()
