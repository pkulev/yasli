import sys

from iml_parser import *

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.stderr.write('usage: {0} filename parsername'.format(sys.argv[0]))
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, 'r') as file:
        source = file.read()
    tokens = iml_lex(source)
    parser = globals()[sys.argv[2]]()
    result = parser(tokens, 0)
    print(result)

