# ASSIGNMENT: Activity 06 (Functions)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'myfuncs.py'
POINTS = 2

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[32], [100.0], [-40.3], [1234.0], [0]], [{}, {}, {}, {}, {}], [273.15, 310.92777777777775, 232.98333333333332, 940.9277777777778, 255.3722222222222])))
def test_fahrenheit2kelvin(args, kwargs, reference):
    return _test_function("fahrenheit2kelvin",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False)
