import unittest
import Demo


class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEquals(Demo.add(2, 2), 4)
        self.assertEquals(Demo.add(10, 4), 14)
        self.assertEquals(Demo.add(23, 7), 30)

    def test_sub(self):
        self.assertEquals(Demo.sub(10, 5), 5)
        self.assertEquals(Demo.sub(4, 5), -1)


if __name__ == '__main__':
    unittest.main()