import unittest
import Demo


class TestDemo(unittest.TestCase):

    def test_add(self):
        self.assertEquals(Demo.add(2, 3), 5)
