import unittest
from tdidt import build, DataSet


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('expected.txt') as f:
            expected = f.read()

        train_set = DataSet()
        train_set.initialize_from_file('data_exercise_1.csv')
        # Remove test set from data set
        test_set = train_set.get_test_instances(int((1.0 / 3) * len(train_set.examples)))

        node_list = build(train_set)
        self.assertEqual(expected, ' '.join([str(n) for n in node_list]))


if __name__ == '__main__':
    unittest.main()
