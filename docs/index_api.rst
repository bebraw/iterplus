Index
=====

.. testsetup:: *

    from iterplus import index, rindex

iterplus provides functions that may be used to find index of the first or the last matching item. These functions are known as "index" and "rindex". The following examples should give you an idea how they behave.

index
^^^^^

.. doctest::

    >>> items = [10, 27, 4, 340, 3]

    >>> index(lambda a: a < 12, items)
    0

    >>> index(lambda a: a > 20, items)
    1

    >>> index(lambda a: a < 9, items)
    2

    >>> index(lambda a: a > 500, items)
    Traceback (most recent call last):
    ...
    ValueError: 'f' not in 'seq'

rindex
^^^^^^

.. doctest::

    >>> items = [10, 27, 4, 340, 3]

    >>> rindex(lambda a: a < 12, items)
    4

    >>> rindex(lambda a: a > 20, items)
    3

    >>> rindex(lambda a: a < 9, items)
    4

    >>> rindex(lambda a: a > 500, items)
    Traceback (most recent call last):
    ...
    ValueError: 'f' not in 'seq'

