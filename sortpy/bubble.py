"""Basic sort module.
"""
from __future__ import annotations


def sort(array: list[int]) -> list[int]:
    """Naive bubble sort implementation.
    """
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array
