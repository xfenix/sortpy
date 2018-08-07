def sort(array):
    for i, item in enumerate(array):
        for j, subitem in enumerate(array[i:]):
            if item > subitem:
                array[j + i] = item
                array[i] = subitem
    return array
