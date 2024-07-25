import unittest
from matrix import has_hole, count_holes
from colorama import Fore, Style


class TestHasHole(unittest.TestCase):

    """
    This class contains test cases for the `has_hole` function,
    which checks if a single cell is part of a hole (contiguous region of 0s)
    in the binary matrix.
    """

    def test_single_zero(self):
        """
        Tests if a single 0 surrounded by 1s is not considered a hole.
        """
        matrix = ["101", "011", "111"]
        row, col = 1, 1
        visited = set()
        self.assertFalse(has_hole(matrix, row, col, visited))
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_two_by_two_zeros(self):
        """
        Tests if a 2x2 block of 0s is considered a single hole.
        """
        matrix = ["1001", "0010", "0100", "1111"]
        row, col = 1, 1
        visited = set()
        self.assertTrue(has_hole(matrix, row, col, visited))
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_l_shaped_hole(self):
        """
        Tests if an L-shaped pattern of 0s is considered a single hole.
        """
        matrix = ["100", "100", "110"]
        row, col = 0, 1
        visited = set()
        self.assertTrue(has_hole(matrix, row, col, visited))
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_edge_hole(self):
        """
        Tests if a 0 cell on the edge of the matrix can be part of a hole.
        """
        matrix = ["0001", "0100", "0100", "1111"]
        row, col = 0, 0
        visited = set()
        self.assertTrue(has_hole(matrix, row, col, visited))
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_visited_cell(self):
        """
        Tests if the function avoids revisiting previously explored cells.
        """
        matrix = ["101", "011", "111"]
        row, col = 1, 1
        visited = set([(1, 1)])
        self.assertFalse(has_hole(matrix, row, col, visited))
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green


class TestCountHoles(unittest.TestCase):

    """
    This class contains test cases for the `count_holes` function,
    which calculates the total number of holes in the binary matrix.
    """

    def test_example_matrix(self):
        """
        Tests if the function correctly counts the holes in a sample matrix.
        """
        matrix = ["1001", "0010", "0100", "1111"]
        expected_holes = 2
        self.assertEqual(count_holes(matrix), expected_holes)
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_empty_matrix(self):
        """
        Tests if the function handles an empty matrix with no holes.
        """
        matrix = []
        expected_holes = 0
        self.assertEqual(count_holes(matrix), expected_holes)
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green

    def test_single_hole(self):
        """
        Tests if the function can identify a single hole in the matrix.
        """
        matrix = ["111", "100", "111"]
        expected_holes = 1
        self.assertEqual(count_holes(matrix), expected_holes)
        print(Fore.GREEN + "Test Passed!" + Style.RESET_ALL)  # Print success message in green


if __name__ == "__main__":
    unittest.main()
