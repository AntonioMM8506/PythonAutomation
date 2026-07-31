import unittest

class AssertMethodsDemo(unittest.TestCase):

    def test_assert_methods(self):
        # assertEqual checks if the two values are equal
        self.assertEqual(2 + 2, 4)

        # assertNotEqual checks if the two values are not equal
        self.assertNotEqual(5 - 3, 1)

        # assertTrue checks if the expression is True
        self.assertTrue(3 > 2)

        # assertFalse checks if the expression is False
        self.assertFalse(2 > 3)

        # assertIs checks if two objects are the same
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

        # assertIsNot checks if two objects are not the same
        c = [1, 2, 3]
        self.assertIsNot(a, c)

        # assertIsNone checks if the object is None
        self.assertIsNone(None)

        # assertIsNotNone checks if the object is not None
        self.assertIsNotNone(5)

        # assertIn checks if the first value is in the second value
        self.assertIn(3, [1, 2, 3])

        # assertNotIn checks if the first value is not in the second value
        self.assertNotIn(4, [1, 2, 3])

        # assertIs checks if two objects are the same
        self.assertIs("Hello", "Hello")

        # assertGreater checks if the first value is greater than the second value
        self.assertGreater(5, 3)

        # assertGreaterEqual checks if the first value is greater than or equal to the second value
        self.assertGreaterEqual(5, 5)

        # assertLess checks if the first value is less than the second value
        self.assertLess(3, 5)

        # assertLessEqual checks if the first value is less than or equal to the second value
        self.assertLessEqual(3, 3)

        #assertAlmostEqual checks if two values are approximately equal, useful for floating-point comparisons
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=7)

        # assertIsInstance checks if the object is an instance of the specified class
        self.assertIsInstance(5, int)


if __name__ == '__main__':
    unittest.main(verbosity=2)