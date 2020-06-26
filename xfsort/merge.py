"""Basic sort module.
"""


def sort(array):
    """Merge sort implementation.
    """
    if len(array) < 2:
        return array
    result, mid = [], int(len(array) / 2)
    first_half = sort(array[:mid])
    second_half = sort(array[mid:])
    while (len(first_half) > 0) and (len(second_half) > 0):
        if first_half[0] > second_half[0]:
            result.append(second_half.pop(0))
        else:
            result.append(first_half.pop(0))
    result.extend(first_half + second_half)
    return result
