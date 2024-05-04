import unittest
from task2 import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_positive_case(self):
        arr = [-0.5, 0, 0.3, 0.5, 3.2, 4.5, 10.1, 40.56]
        x = 0.5
        result = binary_search(arr, x)
        self.assertEqual(result, (1, 0.5))

        x = 3.2
        result = binary_search(arr, x)
        self.assertEqual(result, (3, 3.2))

        x = 4
        result = binary_search(arr, x)
        self.assertEqual(result, (3, 4.5))

        x = -1
        result = binary_search(arr, x)
        self.assertEqual(result, (3, -0.5))

        x = -100
        result = binary_search(arr, x)
        self.assertEqual(result, (3, -0.5))

    def test_negative_case(self):
        arr = [-0.5, 0, 0.3, 0.5, 3.2, 4.5, 10.1, 40.56]
        x = 100
        result = binary_search(arr, x)
        self.assertEqual(result, (0, None))

        x = 40.57
        result = binary_search(arr, x)
        self.assertEqual(result, (0, None))

    def test_edge_cases(self):
        arr = [-0.5, 0, 0.3, 0.5, 3.2, 4.5, 10.1, 40.56]
        x = -0.5
        result = binary_search(arr, x)
        self.assertEqual(result, (3, -0.5))

        x = -0.3
        result = binary_search(arr, x)
        self.assertEqual(result, (3, 0))

        x = 40.56
        result = binary_search(arr, x)
        self.assertEqual(result, (4, 40.56))

        x = 40.53
        result = binary_search(arr, x)
        self.assertEqual(result, (4, 40.56))

    def test_empty_array(self):
        arr = []
        x = 5
        result = binary_search(arr, x)
        self.assertEqual(result, (0, None))

        arr = None
        x = 5
        result = binary_search(arr, x)
        self.assertEqual(result, (0, None))
    
    def test_empty_x(self):
        arr = [-0.5, 0, 0.3, 0.5, 3.2, 4.5, 10.1, 40.56]
        x = None
        result = binary_search(arr, x)
        self.assertEqual(result, (0, None))


if __name__ == '__main__':
    unittest.main()
