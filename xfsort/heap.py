def sort(array):
    def sift(start, count):
        root = start

        while root * 2 + 1 < count:
            child = root * 2 + 1
            if child < count - 1 and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                array[root], array[child] = array[child], array[root]
                root = child
            else:
                return

    count = len(array)
    start = int(count / 2) - 1
    end = count - 1

    while start >= 0:
        sift(start, count)
        start -= 1

    while end > 0:
        array[end], array[0] = array[0], array[end]
        sift(0, end)
        end -= 1

    return array
