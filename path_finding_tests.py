import unittest
from path_finding import find_path, BOMB, TRENCH


class TestMethod(unittest.TestCase):
    def test_path_2x2(self):
        field = [[TRENCH, TRENCH], [0, BOMB]]
        solution = find_path(field)

        expected_list = [(0, 0), (0, 1), (1, 1)]

        print(solution.path)
        print(expected_list)

        self.assertListEqual(solution.path, expected_list)


if __name__ == "__main__":
    unittest.main()
