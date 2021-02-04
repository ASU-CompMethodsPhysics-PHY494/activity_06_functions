# ASSIGNMENT: Activity 06 (Functions)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'step_plot.py'
POINTS = 4

def test_x_values():
    return _test_variable("x_values", [-4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0],
                          FILENAME,
                          check_type=False)
