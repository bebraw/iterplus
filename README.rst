This library provides a set of functions that complement Python itertools. These include means to access iterable content via slicing, scan generator (easy series), chainable wrapper (ie. a.map(...).filter(...)) and index (returns first or last matched index in seq).

* Documentation: http://packages.python.org/iterplus/
* Source: http://github.com/bebraw/iterplus/
* Issue Tracker: http://github.com/bebraw/iterplus/issues/

Examples
--------

The following examples illustrate the basic usage:

Scan
====

::

    fibo = scan(0, 1, lambda a, b: a + b)

"scan" returns an iterator. Note how simple it's to define series such as Fibonacci's using it. In case an explicit rule is not provided, it infers one automatically (ie. 1,2,3,...).

Sliceable
=========

::

    sliceable(scan(0, 1))[2:5] # returns list containing third, fourth and fifth item

"sliceable" makes it possible to slice the content of iterators.

Chainable
=========

::

    chainable([1, 2, 3]).map(lambda x: x * 2).filter(lambda x: x > 3).val() == [4, 6]

"chainable" makes it possible to use basic functional utilities (map, filter, reduce) using a chaining syntax.

Index
=====

::

    index(lambda a: a > 4, [3, 10, 8]) == 1    
    rindex(lambda a: a < 5, [3, 10, 8]) == 0

"index" and "rindex" make it possible to find the first or the last item of a sequence matching to a given rule.

.. _itertools: http://docs.python.org/library/itertools.html

License
-------

iterplus is available under MIT license. See LICENSE for more details.

