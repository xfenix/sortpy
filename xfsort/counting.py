def sort(array):
    result = [0] * len(array)
    low = min(array)
    high = max(array)
    count_array = [0 for i in range(low, high + 1)]
    for i in array:
        count_array[i - low] += 1
    for j in range(1, len(count_array)):
        count_array[j] += count_array[j - 1]
    for k in reversed(array):
        result[count_array[k - low] - 1] = k
        count_array[k - low] -= 1
    return result
