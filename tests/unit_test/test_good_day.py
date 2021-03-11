import unittest
import sys
import good_day
from contextlib import contextmanager
from io import StringIO


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


class TestGoodDay(unittest.TestCase):
    def test_if_your_day_is_good(self):
        with captured_output() as (out, err):
            good_day.start()
        output = out.getvalue().strip()
        expected = 'Now your great day begins! 😊'
        self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()
