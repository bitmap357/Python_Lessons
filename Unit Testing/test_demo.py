# import unittest
# import Demo
#
#
# class TestDemo(unittest.TestCase):
#
#     def test_add(self):
#         self.assertEquals(Demo.add(2, 2), 4)
#         self.assertEquals(Demo.add(10, 4), 14)
#         self.assertEquals(Demo.add(23, 7), 30)
#
#     def test_sub(self):
#         self.assertEquals(Demo.sub(10, 5), 5)
#         self.assertEquals(Demo.sub(4, 5), -1)
#
#     def test_mul(self):
#         self.assertEquals(Demo.mul(2, 3), 6)
#         self.assertEquals(Demo.mul(10, 4), 40)
#         self.assertEquals(Demo.mul(2, 7), 14)
#
#     def test_div(self):
#         self.assertEquals(Demo.div(4, 2), 2)
#         self.assertEquals(Demo.div(12, 4), 3)
#         self.assertEquals(Demo.div(25, 5), 5)
#
#
# if __name__ == '__main__':
#     unittest.main()

import unittest
import Demo


@unittest.skip("Skipping this test for some reason")
class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.calculate = Demo.Calculate()

    def tearDown(self) -> None:
        print("This is a teardown method")

    def test_add(self):
        self.assertEquals(self.calculate.add(4, 5), 9)

    def test_sub(self):
        self.assertEquals(self.calculate.sub(4, 5), -1)

    def test_mul(self):
        self.assertEquals(self.calculate.mul(4, 5), 20)

    def test_div(self):
        self.assertEquals(self.calculate.div(10, 5), 2)
        with self.assertRaises(ValueError):
            self.calculate.div(10, 0)


if __name__ == "__main__":
    unittest.main()
