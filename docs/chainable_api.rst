Chainable
=========

.. testsetup:: *

    from iterplus import chainable

"chainable" makes it possible to chain various functional tools. Using it you could write something like this for example:

.. doctest::

    >>> a = chainable([1, 2, 3]).map(lambda x: x * 2).filter(lambda x: x > 3).val()
    >>> assert a == [4, 6]

Currently the API supports just "map", "filter" and "reduce". Of these "map" and "filter" return something that may be further chained. If you want to extract the actual list out of the chain, use "val" as above. "reduce" returns a result directly. Here's an example of that:

.. doctest::

    >>> b = chainable([3, 2, 10]).filter(lambda x: x < 7).reduce(lambda x, y: x + y)
    >>> assert b == 5

