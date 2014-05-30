import sys
import argparse
from datetime import datetime


from iml_lexer import *
from iml_parser import *

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, help='File to execute', required=False)
if len(sys.argv) > 1:
    args = parser.parse_args()


def start_iml_repl():
    greeting = "IML interpreter\n"
    ind_lvl = 0
    prompt = "{level}==> "

    print(greeting)

    while True:

        src = input(prompt.format(level='=' * ind_lvl * 2))
        print(src)


def err(msg):
    delim = " "
    sys.stderr.write(str(datetime.now()) + delim + msg + '\n')


def log(msg):
    delim = " "
    sys.stdout.write(str(datetime.now()) + delim + msg + '\n')


def main():
    if not args.filename:
        start_iml_repl()

    filename = args.filename if args.filename else None
    with open(filename, 'r') as f:
        src = f.read()

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

if __name__ == '__main__':
    sys.exit(main())