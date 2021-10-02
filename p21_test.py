import unittest
from p21 import generate_sons_probs, add_lists


class test_problem20(unittest.TestCase):
    def test_generate_sons(self):
        pass

    def test_add_lists(self):
        lst1 = [1, 2, 3]
        lst2 = [4, 5, 6]
        self.assertEqual(add_lists(lst1, lst2), [5, 7, 9])

        lst2 = [3, 4]
        self.assertEqual(add_lists(lst1, lst2), [4, 6, 3])

        lst1 = []
        self.assertEqual(add_lists(lst1, lst2), [3, 4])


if __name__ == '__main__':
    unittest.main()
