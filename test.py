import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with open('expected.txt') as f:
            expected = f.read()


if __name__ == '__main__':
    unittest.main()
