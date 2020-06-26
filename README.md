Normal sorting
===

[![Build Status](https://travis-ci.org/xfenix/xfsort.svg?branch=master)](https://travis-ci.org/xfenix/xfsort)
[![codecov](https://codecov.io/gh/xfenix/xfsort/branch/master/graph/badge.svg)](https://codecov.io/gh/xfenix/xfsort)

Currenly implemented sorting algorithms:

* Bubble (of course just for fun)
* Quick (with random pivot)
* Merge
* Insertion
* Heap
* More to go...

Compatibility
--------

Python 3.5+ (test coverage include python 3.5, 3.6, 3.7, 3.8)

Usage
--------

* Install xfsort with `python setup.py install` (pip install xfsort in near future)
* Import sorting algorithm `from xfsort.quick import sort`

Also
--------

Test coverage with fixtures and random generated test cases (reference function is python basic timsort)
