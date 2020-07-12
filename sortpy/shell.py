"""Basic sort module.
"""
import typing


def sort(array: list) -> list:
    """Shell sort implementation.
    """
    gap: int = int(len(array) / 2)
    while gap > 0:
        for i in range(gap, len(array)):
            temp: typing.Any = array[i]
            j: int = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j = j - gap
            array[j] = temp
        gap = int(gap / 2)
    return array
