import unittest
import Demo


class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEquals(Demo.add(2, 2), 4)
        self.assertEquals(Demo.add(10, 4), 14)
        self.assertEquals(Demo.add(23, 7), 30)




if __name__ == '__main__':
    unittest.main()