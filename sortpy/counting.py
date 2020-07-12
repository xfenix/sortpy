"""Basic sort module.
"""
from __future__ import annotations


def sort(array: list[int]) -> list[int]:
    """Counting sort implementation.
    """
    result: list[int] = [0, ] * len(array)
    low: int = min(array)
    high: int = max(array)
    count_array: list[int] = [0 for i in range(low, high + 1)]
    for i in array:
        count_array[i - low] += 1
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    for k in reversed(array):
        result[count_array[k - low] - 1] = k
        count_array[k - low] -= 1
    return result
