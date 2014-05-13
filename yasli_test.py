#! /usr/bin/env python

from yasli import Interpreter as Inp

def test_numbers():
    assert Inp().eval('') == []
    assert Inp().eval('42') == [42]
    assert Inp().eval('42 12') == [42, 12]

test_numbers()
