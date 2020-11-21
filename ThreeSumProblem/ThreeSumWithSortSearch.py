import time
import numpy


def threeSumCount(array):
    start_time = time.time()
    counter = 0
    array.sort()
    length_range = range(len(array))
    for i in length_range:
        for j in length_range[i + 1:]:
            # print("Matching index %s %s with value %s %s sums(-) to %s found: %s" % (i, j, array[i], array[j], -(array[i] + array[j]), -(array[i] + array[j]) in array and array[i] < array[j] < -(array[i] + array[j])))
            if -(array[i] + array[j]) in array:
                if array[i] < array[j] < -(array[i] + array[j]):  # Avoid Double Counting of Same Group
                    counter += 1
    print("SortSearch Time Taken --- %s seconds ---" % (time.time() - start_time))
    return counter
