"""Basic sort module.
"""
import typing
import random


def sort(array: list) -> list:
    """Quick sort implementation with random pivot point.
    """
    total_length: int = len(array)
    if total_length < 2:
        return array
    pivot: typing.Any = array[random.randint(0, total_length - 1)]
    less_pivot: list = []
    more_pivot: list = []
    equal_pivot: list = []
    for item in array:
        if item < pivot:
            less_pivot.append(item)
        elif item > pivot:
            more_pivot.append(item)
        else:
            equal_pivot.append(item)
    return sort(less_pivot) + equal_pivot + sort(more_pivot)
