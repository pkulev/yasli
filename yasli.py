import operator as op

from parsimonious.grammar import Grammar

class Interpreter(object):
    
    def __init__(self, env={}):
        self.env = env
    
    def parse(self, source):
        grammar = '\n'.join(value.__doc__ for key, value in vars(self.__class__).items()
                            if not key.startswith('__') and hasattr(value, '__doc__')
                            and getattr(value, '__doc__'))
        return Grammar(grammar)['program'].parse(source)

    def eval(self, source):
        node = self.parse(source) if isinstance(source, str) else source
        method = getattr(self, node.expr_name, lambda *a: 'error')
        return method(node, [self.eval(n) for n in node])

    def program(self, node, children):
        'program = expr*'
        return children

    def expr(self, node, children):
        'expr = number / name _'
        return children[0]

    def name(self, node, children):
        'name = ~"[a-z]+" _'
        return self.env.get(node.text.strip(), -1)

    def number(self, node, children):
        'number = ~"[0-9]+" _'
        return int(node.text)

    def _(self, node, children):
        '_ = ~"\s*"'
