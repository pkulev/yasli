#! /usr/bin/env python

import sys
from iml_lexer import *

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except Exception as e:
        print(e)

    file = open(filename)
    src = file.read()
    file.close()
    tokens = iml_lex(src)
    from pprint import pprint
    pprint(tokens)
