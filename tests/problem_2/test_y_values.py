# ASSIGNMENT: Activity 06 (Functions)
# PROBLEM NUMBER: 2

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_variable

FILENAME = 'step_plot.py'
POINTS = 4

def test_y_values():
    return _test_variable("y_values", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
                          FILENAME,
                          check_type=False)
