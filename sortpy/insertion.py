"""Basic sort module.
"""
from __future__ import annotations
import typing


def sort(array: list) -> list:
    """Insertion sort implementation.
    """
    for j in range(1, len(array)):
        key: typing.Any = array[j]
        i: int = j - 1
        while i > -1 and key < array[i]:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array
