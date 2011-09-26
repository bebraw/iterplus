iterplus - itertools extended
=============================

This library provides a set of functions that complement Python itertools. These include means to access iterable content via slicing, scan generator (easy series) and chainable wrapper (ie. a.map(...).filter(...)).

* Documentation: http://packages.python.org/iterplus/
* Source: http://github.com/bebraw/iterplus/
* Issue Tracker: http://github.com/bebraw/iterplus/issues/

Examples
--------

Scan
^^^^

    fibo = scan(0, 1, lambda a, b: a + b)
    pos_list = scan(0, 1)
    neg_list = scan(1, 0)

"scan" returns an iterator. Note how simple it's to define series such as Fibonacci's using it.

Sliceable
^^^^^^^^^

    sliceable(scan(0, 1))[2:5] # returns list containing third, fourth and fifth item

"sliceable" makes it possible to slice the content of iterators.

Chainable
^^^^^^^^^

    chainable([1, 2, 3]).map(lambda x: x * 2).filter(lambda x: x > 3).val() == [4, 6]

"chainable" makes it possible to use basic functional utilities (map, filter, reduce) using a chaining syntax.

