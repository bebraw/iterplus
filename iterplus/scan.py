# -*- coding: utf-8 -*-

def scan(a, b, rule=None):
    diff = b - a
    rule = rule or (lambda x, y: y + diff)

    yield a
    yield b

    while True:
        a, b = b, rule(a, b)

        yield b

