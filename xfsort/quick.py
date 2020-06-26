"""Basic sort module.
"""
import random


def sort(array):
    """Quick sort implementation with random pivot point.
    """
    total_length = len(array)
    if total_length < 2:
        return array
    pivot = array[random.randint(0, total_length - 1)]
    less_pivot = []
    more_pivot = []
    equal_pivot = []
    for item in array:
        if item < pivot:
            less_pivot.append(item)
        elif item > pivot:
            more_pivot.append(item)
        else:
            equal_pivot.append(item)
    return sort(less_pivot) + equal_pivot + sort(more_pivot)
