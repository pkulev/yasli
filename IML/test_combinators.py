import unittest

from iml_lexer import *
from combinators import *

id = Tag(ID)
integer = Tag(INT)
def keyword(s):
    return Reserved(s, RESERVED)

class TestCombinators(unittest.TestCase):
    def combinators_test(self, code, parser, expected):
        tokens = iml_lex(code)
        result = parser(tokens, 0)
        self.assertNotEquals(None, result)
        self.assertEquals(expected, result.value)

    def test_tag(self):
        self.combinator_test('if', Tag(RESERVED), 'if')

    def test_reserved(self):
        self.combinator_test('if', Reserved('if', RESERVED), 'if')

    def test_concat(self):
        parser = Concat(id, id)
        self.combinator_test('x y', parser, ('x', 'y'))
    
    def test_concat_sugar(self):
        parser = id + id
#        self.combinator_test('x y', parser
