Sliceable
=========

.. testsetup:: *

    from iterplus import sliceable, scan

"sliceable" makes it possible to apply Python's slice and stride notation to iterables. The following examples illustrate this:

Access via Index
^^^^^^^^^^^^^^^^

.. doctest::

    >>> pos_list = sliceable(scan(1, 3))

    >>> assert pos_list[0] == 1
    >>> assert pos_list[3] == 7

    >>> assert pos_list.next() == 1
    >>> assert pos_list[0] == 1

Slice
^^^^^

.. doctest::

    >>> pos_list = sliceable(scan(1, 3))

    >>> assert pos_list[1:3] == [3, 5]

Slice with Stride
^^^^^^^^^^^^^^^^^

.. doctest::

    >>> pos_list = sliceable(scan(1, 3))

    >>> assert pos_list[1:4:2] == [3, 7]

