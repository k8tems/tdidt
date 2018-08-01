import unittest
from tdidt import build


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('expected.txt') as f:
            expected = f.read()
        node_list, test_set = build('data_exercise_1.csv')
        self.assertEqual(expected, ' '.join([str(n) for n in node_list]))


if __name__ == '__main__':
    unittest.main()
