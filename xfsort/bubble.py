"""Basic sort module.
"""


def sort(array):
    """Naive bubble sort implementation.
    """
    for i in range(len(array)):
        for j in range(len(array) - 1, i, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array
