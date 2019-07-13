from unittest import TestCase

from main import func


class Test(TestCase):
    def test_function_that_raises_another_exception(self):
        with self.assertRaises(KeyError):
            func()
