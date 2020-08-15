"""Demonstration of simple unit tests.

Unit tests make it possible to reliably test the code you write and help avoid bugs.
Typically you will write code and the tests for that code in separate files.
By convention, a unit test file is one whose filename ends in `_test.py` (such as this file).

In this file a nonsensically simple function named `double` is defined and some unit tests
follow its definition. Unit test functions can be identified by beginning with a prefix of
`test_`. Within tests, the code under test is evaluated in some way and its results are compared
with expected results with assertions made using Python's `assert` keyword.

With the Python plugin installed in VSCode, you should be able to run an individual unit test
by clicking the "Run Test" button that appears above it. Otherwise, look for the _beaker_ icon
in the activity bar to run all tests. You can also do this from the Command Palatte if you search
for "Python: Run All Tests". If any tests fail you will be taken to a results listing. From there
if you press the page with the arrow icon it will take you directly to the failing test.

If a test fails, you can run the test using the debugger in VSCode by setting a breakpoint in the
unit test's code. To set a break point, hover your mouse just to the left of the line number and
click the red circle to add a breakpoint. Then select the "Debug Test" option just above the test
to begin the interactive debugger.

To run tests from the command-line, run `python -m pytest [optional: directory or file]`.
To run the tests in this file, for example: `python -m pytest comp110/demos/unit_test.py`
"""

__author__ = "Kris Jordan <kris@cs.unc.edu>"


def double(x: int) -> int:
    """Given an integer, double it.
    
    Arguments:
        x: The input integer to double.

    Returns:
        The result of doubling the input.
    """
    return x * 2
    

def test_double_positive() -> None:
    assert double(1) == 2
    assert double(2) == 4
    assert double(100) == 200


def test_double_negative() -> None:
    assert double(-1) == -2
    assert double(-2) == -4
    assert double(-100) == -200


def test_double_zero() -> None:
    assert double(0) == 0
