#!/usr/bin/env python
# coding: utf-8

"""
rngen.py
shanahanjrs

a -> alpha upper and lower
l -> alpha lower
u -> alpha upper
n -> numeric
m -> alpha upper and lower + numeric
s -> symbol
x -> any
"""

import sys
from random import choice

_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*()-_=+?'
_VALID_CODES = ['a', 'l', 'u', 'n', 'm', 's', 'x']
_CODES = {
    'a': _CHARS[:52],
    'l': _CHARS[:26],
    'u': _CHARS[26:52],
    'n': _CHARS[52:62],
    'm': _CHARS[:62],
    's': _CHARS[62:],
    'x': _CHARS,
}
_CODE_LEN = {
    'a': len(_CODES['a']),
    'l': len(_CODES['l']),
    'u': len(_CODES['u']),
    'n': len(_CODES['n']),
    'm': len(_CODES['m']),
    's': len(_CODES['s']),
    'x': len(_CODES['x']),
}

def usage():
    print("rngen")
    print("random string and number generator based on a specified pattern")
    print("John Shanahan")
    print("Usage:")
    print("    $ rngen aaa")
    print("    > ZjL")

def generate(code):
    """
    takes a code and returns the random char from that codes range
    """
    generated_string = []

    for i in code:
        if i not in _VALID_CODES:
            sys.exit('Invalid code "%s" entered' % i)

        generated_string.append(choice(_CODES[i]))

    return ''.join(generated_string)


if __name__ == '__main__':
    if len(sys.argv) < 2 or '--help' in sys.argv:
        sys.exit(usage())

    print(generate(sys.argv[1]))

