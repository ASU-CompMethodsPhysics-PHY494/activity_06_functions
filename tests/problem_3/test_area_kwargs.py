# ASSIGNMENT: Activity 06 (Functions)
# PROBLEM NUMBER: 3

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_function

FILENAME = 'myfuncs.py'
POINTS = 2

@pytest.mark.parametrize(("args", "kwargs", "reference"),
                         list(zip([[2, 4], [2, 4], [1, 1], [0.5, 0.1]], [{}, {'scale': 2}, {'scale': 0.5, 'offset': 9.0}, {'offset': 0.9}], [8, 16, 5.0, 0.95])))
def test_area_kwargs(args, kwargs, reference):
    return _test_function("area",
                          args,     # tuple or list
                          kwargs,   # dict
                          reference,
                          FILENAME,
                          check_type=False)
