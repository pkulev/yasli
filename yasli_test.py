#! /usr/bin/env python

from yasli import Interpreter as Inp

def test_numbers():
    assert Inp().eval('') == []
    assert Inp().eval('42') == [42]
    assert Inp().eval('42 12') == [42, 12]

def test_variables():
#    assert Inp().eval('a') == [42]
    assert Inp().eval({'a': 42}).eval('a') == [42]

test_numbers()
test_variables()
