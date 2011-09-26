Scan
====

.. testsetup:: *

    from iterplus import scan

"scan" provides simple means to define various types of series. The following examples illustrate this better.

Incremental Scan
^^^^^^^^^^^^^^^^

.. doctest::

    >>> pos_list = scan(1, 2) # returns a generator

    >>> assert pos_list.next() == 1
    >>> assert pos_list.next() == 2
    >>> assert pos_list.next() == 3

Decremental Scan
^^^^^^^^^^^^^^^^

.. doctest::

    >>> neg_list = scan(-2, -5)

    >>> assert neg_list.next() == -2
    >>> assert neg_list.next() == -5
    >>> assert neg_list.next() == -8

Constant Scan
^^^^^^^^^^^^

.. doctest::

    >>> c_list = scan(7, 7)

    >>> assert c_list.next() == 7
    >>> assert c_list.next() == 7
    >>> assert c_list.next() == 7

Custom Rule
^^^^^^^^^^^

.. doctest::

    >>> fibo = scan(0, 1, lambda a, b: a + b)

    >>> assert fibo.next() == 0
    >>> assert fibo.next() == 1
    >>> assert fibo.next() == 1
    >>> assert fibo.next() == 2

