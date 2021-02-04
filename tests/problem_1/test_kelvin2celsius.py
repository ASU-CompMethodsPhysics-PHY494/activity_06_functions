# ASSIGNMENT: Activity 06 (Functions)
# PROBLEM NUMBER: 1

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'myfuncs.py'
POINTS = 2

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[273.15], [0.0], [373.15], [1234.5], [4.2]], [{}, {}, {}, {}, {}], [0.0, -273.15, 100.0, 961.35, -268.95])))
def test_kelvin2celsius(args, kwargs, reference):
    return _test_function("kelvin2celsius",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False)
