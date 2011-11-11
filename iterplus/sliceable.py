# -*- coding: utf-8 -*-
from itertools import tee

def sliceable(iterator):
    class Slice(object):

        def __init__(self, iter):
            self._iter, self._root = tee(iter)
            self._cache = []

        def __getitem__(self, k):
            if isinstance(k, slice):
                return [self._get_value(i) for i in xrange(k.start, k.stop, k.step or 1)]

            return self._get_value(k)

        def _get_value(self, k):
            cache_len = len(self._cache)

            if k < cache_len:
                return self._cache[k]

            self._root, root_copy = tee(self._root)
            ret = None

            for i in xrange(k - cache_len + 1):
                ret = root_copy.next()
                self._cache.append(ret)

            self._root = root_copy

            return ret

        def next(self):
            return self._iter.next()

    return Slice(iterator)

