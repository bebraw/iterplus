# -*- coding: utf-8 -*-

def chainable(items):
    class Chain(object):

        def __init__(self, items):
            self._items = items

        def map(self, a):
            return Chain(map(a, self._items))

        def filter(self, a):
            return Chain(filter(a, self._items))

        def reduce(self, a):
            return reduce(a, self._items)

        def val(self):
            return self._items

    return Chain(items)

