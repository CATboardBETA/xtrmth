'''test functions.'''

from xtrmth import xm
import decimal as dc

def test_summation():
    '''test xm.summation function'''
    assert xm.summation(4, 'x=1', 'x*2')

def test_sq():
    '''test xm.sq function'''
    assert xm.sq(dc.Decimal(12.6), decimal=True, _print_unround=True)

def test_sqrt():
    assert xm.sqrt(dc.Decimal(158.76), decimal=True, _print_unround=True)

def test_cb():
    assert xm.cb(dc.Decimal(12.4), decimal=True, _print_unround=True)

def test_cbrt():
    assert xm.cb(dc.Decimal(146.4), decimal=True, _print_unround=True)

def test_xpn():
    assert xm.xpn(dc.Decimal(16.2), dc.Decimal(12), decimal=True, _print_debug=True)