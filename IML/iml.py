#! /usr/bin/env python

import sys
from datetime import datetime

import click

from iml_lexer import *
from iml_parser import *

MODE = None

def err(msg):
    delim = " "
    sys.stderr.write(str(datetime.now()) + delim + msg + '\n')


def log(msg):
    delim = " "
    sys.stdout.write(str(datetime.now()) + delim + msg + '\n')


def start_iml_repl():
    greeting = "IML interpreter\n"
    ind_lvl = 0
    prompt = "{level}==> "
    env = {}

    print(greeting)

    while True:

        src = input(prompt.format(level='=' * ind_lvl * 2))
        if src.split(' ')[0] == 'while':
            ind_lvl += 1
        if ind_lvl > 0 and src.strip() == 'end':
            ind_lvl -= 1

        #DEBUG
        print(src, type(src))
        tokens = iml_lex(src)
        print(tokens)
        parse_result = iml_parse(tokens)
        if not parse_result:
            err('Parse error!')
            return 1
        ast = parse_result.value
        ast.eval(env)
        log('Variable values:')
        for var, val in env.items():
            log('{0}: {1}'.format(str(var), str(val)))


def exec_iml_file(src):
        tokens = iml_lex(src)
        parse_result = iml_parse(tokens)
        if not parse_result:
            err('Parse error!')
            return 1

        ast = parse_result.value
        env = {}
        ast.eval(env)

        log('Final variable values:')
        for var, val in env.items():
            log('{0}: {1}'.format(str(var), str(val)))
        return 0

@click.command()
@click.option('-e', '--exec', default='', type=str, help='Execute file')
def main(exec):
    if exec:
        filename = exec
        with open(filename, 'r') as f:
            src = f.read()
        return exec_iml_file(src)
    else:
        return start_iml_repl()

if __name__ == '__main__':
    sys.exit(main())