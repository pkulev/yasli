from equality import *


class Statement(Equality):
    pass


class Aexp(Equality):
    pass


class Bexp(Equality):
    pass


class AssignStatement(Statement):
    def __init__(self, name, aexp):
        self.name = name
        self.aexp = aexp

    def __repr__(self):
        return 'AssignStatement({0}, {1})'.format(self.name, self.aexp)

    def eval(self, env):
        value = self.aexp.eval(env)
        env[self.name] = value


class CompoundStatement(Statement):
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __repr__(self):
        return 'CompoundStatement({0}, {1})'.format(self.first, self.second)

    def eval(self, env):
        self.first.eval(env)
        self.second.eval(env)


class IfStatement(Statement):
    def __init__(self, condition, true_stmt, false_stmt):
        self.condition = condition
        self.true_stmt = true_stmt
        self.false_stmt = false_stmt

    def __repr__(self):
        return 'IfStatement({0}, {1}, {2})'.format(self.condition, self.true_stmt, self.false_stmt)

    def eval(self, env):
        condition_value = self.condition.eval(env)
        if condition_value:
            self.true_stmt.eval(env)
        else:
            if self.false_stmt:
                self.false_stmt.eval(env)


class WhileStatement(Statement):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

    def __repr__(self):
        return 'WhileStatement({0}, {1})'.format(self.condition, self.body)

    def eval(self, env):
        condition_value = self.condition.eval(env)
        while condition_value:
            self.body.eval(env)
            condition_value = self.condition.eval(env)


class IntAexp(Aexp):
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return 'IntAexp({0})'.format(self.i)

    def eval(self, env):
        return self.i


class VarAexp(Aexp):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'VarAexp({0})'.format(self.name)

    def eval(self, env):
        if self.name in env:
            return env[self.name]
        else:
            return 0


class BinopAexp(Aexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'BinopAexp(%s, %s, %s)' % (self.op, self.left, self.right)

    def eval(self, env):
        lvalue = self.left.eval(env)
        rvalue = self.right.eval(env)
        m = {'+': lambda: lvalue + rvalue,
             '-': lambda: lvalue - rvalue,
             '*': lambda: lvalue * rvalue,
             '/': lambda: lvalue / rvalue
             }
        try:
            value = m[self.op]()
        except KeyError:
            raise RuntimeError('Unknown operator: ' + str(self.op))
        return value


class RelopBexp(Bexp):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return 'RelopBexp({0},{1},{2})'.format(self.op, self.left, self.right)

    def eval(self, env):
        lvalue = self.left.eval(env)
        rvalue = self.right.eval(env)
        m = {'<' : lambda: lvalue <  rvalue,
             '<=': lambda: lvalue <= rvalue,
             '>' : lambda: lvalue >  rvalue,
             '>=': lambda: lvalue >= rvalue,
             '=' : lambda: lvalue == rvalue,
             '!=': lambda: lvalue != rvalue
             }
        try:
            value = m[self.op]()
        except KeyError:
            raise RuntimeError('Unknown operator: ' + str(self.op))
        return value


class AndBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'AndBexp({0}, {1})'.format(self.left, self.right)

    def eval(self, env):
        lvalue = self.left.eval(env)
        rvalue = self.right.eval(env)
        return lvalue and rvalue


class OrBexp(Bexp):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return 'OrBexp({0}, {1})'.format(self.left, self.right)

    def eval(self, env):
        lvalue = self.left.eval(env)
        rvalue = self.right.eval(env)
        return lvalue or rvalue


class NotBexp(Bexp):
    def __init__(self, exp):
        self.exp = exp

    def __repr__(self):
        return 'NotBexp({0})'.format(self.exp)

    def eval(self, env):
        value = self.exp.eval(env)
        return not value