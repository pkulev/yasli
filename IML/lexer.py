import re
import sys


def lex(source, token_exprs):
    pos = 0
    tokens = []
    end = len(source)
    while pos < end:
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern)
            match = regex.match(source, pos)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character {s}'.format(source[pos]))
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens
