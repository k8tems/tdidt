import unittest
from tdidt import build, get_dataset


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('expected.txt') as f:
            expected = f.read()

        train_set, test_set = get_dataset('data_exercise_1.csv')

        node_list = build(train_set)
        self.assertEqual(expected, ' '.join([str(n) for n in node_list]))


if __name__ == '__main__':
    unittest.main()
