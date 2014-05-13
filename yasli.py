import operator as op

from parsimonious.grammar import Grammar

class Interpreter(object):
    
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
        'program = number*'
        return children

    def number(self, node, children):
        'number = ~"[0-9]+" ~"\s*"'
        return int(node.text)
