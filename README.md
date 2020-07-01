Normal sorting
===
[![PyPI version](https://badge.fury.io/py/xfsort_collection.svg)](https://badge.fury.io/py/xfsort_collection)
![CI status](https://github.com/xfenix/xfsort/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/xfenix/xfsort/branch/master/graph/badge.svg)](https://codecov.io/gh/xfenix/xfsort)

Various sorting algorithms implemented in pure python. Now with typing support and for python 3.7/3.8.  
Currently implemented following:
* Bubble (of course just for fun)
* Quick (with random pivot)
* Merge
* Insertion
* Heap
* More to go...

Compatibility
--------
Python 3.7+ (test coverage include python 3.7, 3.8)

Usage
--------
* Install xfsort with `python setup.py install` (pip install xfsort in near future)
* Import sorting algorithm `from xfsort.quick import sort`

Also
--------
Test coverage with fixtures and random generated test cases (reference function is python basic timsort)
