# -*- coding: utf-8 -*-
# http://tomayko.com/writings/cleanest-python-find-in-list-function

def _template(ret):
    if ret is not None:
        return ret

    raise ValueError("'f' not in 'seq'")

def index(f, seq):
    """Returns the index of the first item in seq where f(item) == True."""
    ret = next((i for i in xrange(len(seq)) if f(seq[i])), None)

    return _template(ret)

def rindex(f, seq):
    """Returns the index of the last item in seq where f(item) == True."""
    ret = next((i for i in xrange(len(seq) - 1, -1, -1) if f(seq[i])), None)

    return _template(ret)

