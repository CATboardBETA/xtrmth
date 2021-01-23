"""Math functions, no variables"""

import typing as tp
import decimal as dc

_meganum = tp.Union[int, float, dc.Decimal, tp.SupportsInt, tp.SupportsFloat]
_num = tp.Union[int, float, dc.Decimal]
_micronum = tp.Union[int, float]
_decnum = tp.Union[float, dc.Decimal]

def _total_round(value: _num, precision: int = 10, decimal: bool = False) -> _num:
    """Rounds 'value' to the nearest 'precision' digits."""
    if isinstance(value, int):
        return value
    elif precision < 0:
        raise ValueError('Cannot cast a negative integer onto \'xm._total_round(precision)\'')
    elif decimal is True:
        if isinstance(value, dc.Decimal):
            return round(value, precision)
        elif not isinstance(value, dc.Decimal) and decimal is True:
            raise TypeError('Cannot cannot cast \'float\' onto \'xm._total_round(value)\' \
with opperand \'decimal\' as \'True\'.')
    elif decimal is False:
        if isinstance(value, float):
            return round(value, precision)
        elif not isinstance(value, float):
            raise TypeError('Cannot cast \'decimal\' onto \'xm._total_round(value)\' \
with opperand \'decimal\' as \'False\'.')
    
def summation(count: int, bottom_var: str, expression: str, precision: int = 10, \
decimal: bool = False) -> _num:
    '''Summation function. Example: 'summation(4, 'z=1', 'z+1')' would return 14.'''
    
    if precision < 0:
        raise ValueError('Cannot cast a negative integer onto \'xm.summation(precision)\'')
    var, value = bottom_var.split('=')
    var = var.strip()
    
    if decimal is True:
        value = dc.Decimal(eval(value))
    else:
        value = int(eval(value))

    res = 0
    for i in range(value, count+1):
        res += eval(expression.replace(var, str(i)))

    if decimal is True:
        return _total_round(value=res, precision=precision, decimal=True)
    return _total_round(res, precision=precision, decimal=False)

def sq(value: _num, precision: int = 10, decimal: bool = False, _print_unround: bool = False) -> _micronum:
    '''Returns 'value' raised to the 2nd power, with 'precision' decimal points.'''
    if isinstance(value, float) and decimal is True:
        raise TypeError('Cannot cannot cast \'float\' onto \'xm.cb\' \
with opperand \'decimal\' as \'True\'.')
    elif isinstance(value, dc.Decimal) and decimal is False:
        raise TypeError('Cannot cannot cast \'decimal\' onto \'xm.cb\' \
with opperand \'decimal\' as \'False\'.')
    elif isinstance(value, dc.Decimal) and decimal is True:
        if _print_unround is True:
            print(value*value)
        return _total_round(value*value, precision, decimal=True)
    if _print_unround is True:
        print(value*value)
    return _total_round(value*value, precision, decimal=False)

def sqrt(value: _meganum, precision: int = 10, decimal: bool = False, _print_unround: bool = False) -> _num:
    if decimal is True:
        x = dc.Decimal(value)
        y = dc.Decimal(1)
        e = dc.Decimal(0.000000000000000000000000000000000000000000000000000000000000000001)
    else:
        x = value
        y = 1
        e = 0.0000000000000000000000001
    
    while x - y > e:
        x = (x + y)/2
        y = value / x

    if _print_unround is True:
        print(x)

    return(_total_round(x, precision, decimal=decimal))

def cb(value: _meganum, precision: int = 10, decimal: bool = False, _print_unround: bool = False) -> _num:
    '''Returns 'value' raised to the 2nd power, with '''
    if isinstance(value, float) and decimal is True:
        raise TypeError('Cannot cannot cast \'float\' onto \'xm.cb\' \
with opperand \'decimal\' as \'True\'.')
    elif isinstance(value, dc.Decimal) and decimal is False:
        raise TypeError('Cannot cannot cast \'decimal\' onto \'xm.cb\' \
with opperand \'decimal\' as \'False\'.')
    elif isinstance(value, dc.Decimal) and decimal is True:
        if _print_unround is True:
            print(value*value*value)
        return _total_round(value*value*value, precision, decimal=True)
    if _print_unround is True:
        print(value*value*value)
    return _total_round(value*value*value, precision, decimal=False)

def cbrt(value, _print_unround: bool = False) -> _num:
    x = value**(1/3)

    if _print_unround is True:
        print(x)

    if type(x) is float:
        if round(x, 10) == int(round(x, 10)): return int(round(x, 10))
        return round(x, 10)
    return x

def xpn(base: _meganum, exponent: _meganum, decimal: bool = False, precision: int = 10, _print_debug: bool = False) \
-> _num:
    '''Raises 'base' to the power of 'exponent'.'''
    
    if not isinstance(base, dc.Decimal) and decimal is True:
        raise TypeError(f'Cannot cast \'{type(base).__name__()}\' onto \'xm.xpn(base)\' with opperand \'decimal\' as \'True\'')
    elif isinstance(base, dc.Decimal) and decimal is False:
        raise TypeError('Cannot cast \'decimal.Decimal\' onto \'xm.xpn(base)\' with opperand \'decimal\' as \'False\'')
        
    out = 1
    
    if isinstance(exponent, int):
        if _print_debug is True:
            print('exponent is int')
        for i in range(exponent):
            if _print_debug is True:
                print(out)
            out *= base
        return _total_round(out, precision=precision, decimal=decimal)
    else:
        # will update with my own algorithim in a later update
        return _total_round(base**exponent, precision=precision, decimal=decimal)

def rt(base: _meganum, root: _meganum, precision: int = 10, decimal: bool = False, _print_debug: bool = False) -> _num:
    '''Takes the 'root' root of 'base' '''

    if isinstance(base, dc.Decimal) and decimal is False:
        raise TypeError('Cannot cast \'decimal.Decimal\' onto \'xm.rd(base)\' with opperand \'decimal\' as \'False\'')
    elif not isinstance(base, dc.Decimal) and decimal is True:
        raise TypeError(f'Cannot cast \'{type(base).__name__}\' onto \'xm.rd(base)\' with opperand \'decimal\' as \'False\'')
    elif isinstance(root, dc.Decimal) and decimal is False:
        raise TypeError('Cannot cast \'decimal.Decimal\' onto \'xm.rd(root)\' with opperand \'decimal\' as \'False\'')
    elif not isinstance(root, dc.Decimal) and decimal is True:
        raise TypeError(f'Cannot cast \'{type(root).__name__}\' onto \'xm.rd(root)\' with opperand \'decimal\' as \'True\'')
    
    if decimal is True:
        return xpn(base = base, exponent = (dc.Decimal(1) / root), decimal = True, precision = precision, _print_debug = _print_debug)
    return xpn(base = base, exponent = (1 / root), decimal = False, precision = precision, _print_debug = _print_debug)