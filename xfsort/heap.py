def heapify(a, count):
    start = int((count - 2) / 2)
    while start >= 0:
        shift_down(a, start, count - 1)
        start -= 1


def shift_down(a, start, end):
    root = start
    while (root * 2 + 1) <= end:
        child = root * 2 + 1
        swap = root
        if a[swap] < a[child]:
            swap = child
        if (child + 1) <= end and a[swap] < a[child + 1]:
            swap = child + 1
        if swap != root:
            a[root], a[swap] = a[swap], a[root]
            root = swap
        else:
            return


def sort(array):
    heapify(array, len(array))
    end = len(array) - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        shift_down(array, 0, end)
