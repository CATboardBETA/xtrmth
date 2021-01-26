"""All math functions"""

from typing import Union, SupportsInt, SupportsFloat
from decimal import Decimal

_mega_num = Union[int, float, Decimal, SupportsInt, SupportsFloat]
_num = Union[int, float, Decimal]
_dec_num = Union[float, Decimal]

def _total_round(value: _num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Rounds 'value' to the nearest 'precision' digits. Returns Union[int, float, decimal.Decimal]"""

    if _print_debug is True:
        print(value)
    if isinstance(value, int):
        return value
    elif precision < 0:
        raise ValueError("Cannot cast a negative integer onto 'xm._total_round(precision)'")

    return round(value, precision)

def summation(count: int, bottom_var: str, expression: str, precision: int = 10, _print_debug: bool = False) -> _num:
    """Summation function. Example: 'summation(4, 'z=1', 'z+1')' would return 14."""

    if precision < 0:
        raise ValueError("Cannot cast a negative integer onto 'xm.summation(precision)'")
    elif count == 0:
        return 0

    var, value = bottom_var.split('=')
    var = var.strip()

    value = int(eval(value))

    res = 0
    for i in range(value, count + 1):
        res += eval(expression.replace(var, str(i)))

    if _print_debug is True:
        print(res)
    res = _total_round(res, precision=precision)
    return res

def square(value: _num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Returns 'value' raised to the 2nd power, with 'precision' decimal points."""

    if precision < 0:
        raise ValueError("Cannot cast a negative integer onto 'xm.square(precision)'")

    if _print_debug is True:
        print(value*value)
    return _total_round(value*value, precision, _print_debug=_print_debug)

def square_root(value: _mega_num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Takes the square root of value, with 'precision' decimal places """

    if precision < 0:
        raise ValueError("Cannot cast a negative number onto 'xm.square_root(precision)'.")

    return exponent(value, 1/2, precision=precision, _print_debug=_print_debug)

def cube(value: _mega_num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Returns 'value' raised to the 2nd power, with """

    if precision < 0:
        raise ValueError("Cannot cast a negative number onto 'xm.cube(precision)'.")

    return _total_round(value * value * value, precision=precision, _print_debug=_print_debug)

def cube_root(value, precision: int = 10, _print_debug: bool = False) -> _num:
    """Takes the cube root of value, with 'precision' decimal places"""

    if precision < 0:
        raise ValueError("Cannot cast a negative number onto 'xm.cube_root(precision)'.")

    return exponent(value, 1/3, precision=precision, _print_debug=_print_debug)

def exponent(base: _mega_num, exponent: _mega_num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Raises 'base' to the power of 'exponent'."""

    if precision < 0:
        raise ValueError("Cannot cast a negative integer onto 'xm.exponenet(precision)'.")

    # Will most likely update to not use ** operator in a later update
    return _total_round(base**exponent, precision=precision, _print_debug=_print_debug)

def root(base: _mega_num, root: _mega_num, precision: int = 10, _print_debug: bool = False) -> _num:
    """Takes the 'root' root of 'base' """

    if precision < 0:
        raise ValueError("Cannot cast a negative integer onto 'xm.root(precision)'.")

    return exponent(base, 1/root, precision=precision, _print_debug=_print_debug)