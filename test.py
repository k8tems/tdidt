import unittest
from tdidt import build, ExampleSet


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('expected.txt') as f:
            expected = f.read()

        e = ExampleSet()
        e.initialize_from_file('data_exercise_1.csv')
        # Remove test set from data set
        test_set = e.get_test_instances(int((1.0 / 3) * len(e.examples)))

        node_list = build(e)
        self.assertEqual(expected, ' '.join([str(n) for n in node_list]))


if __name__ == '__main__':
    unittest.main()
