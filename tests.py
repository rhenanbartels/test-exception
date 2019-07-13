from unittest import TestCase, mock

from main import func, func2


class Test(TestCase):
    def test_function_that_raises_another_exception(self):
        with self.assertRaises(KeyError):
            func()

    def test_mocked_function_exception(self):
        with self.assertRaises(KeyError):
            m = mock.MagicMock()
            m.side_effect = ZeroDivisionError
            func2(m)
