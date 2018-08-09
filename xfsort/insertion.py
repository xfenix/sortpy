def sort(array):
    for j in range(1, len(array)):
        key = array[j]
        i = j - 1
        while i > -1 and key < array[i]:
            array[i + 1] = array[i]
            i = i - 1
        array[i + 1] = key
    return array
