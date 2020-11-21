import time
import numpy


def threeSumCount(array):
    start_time = time.time()
    counter = 0
    length_range = range(len(array))
    for i in length_range:
        for j in length_range[i + 1:]:
            for z in length_range[j + 1:]:
                # print("Matching index %s %s %s with value %s %s %s will result to %s" % (i, j, z, array[i], array[j], array[z], array[i] + array[j] + array[z]))
                if array[i] + array[j] + array[z] == 0:
                    counter += 1
    print("BruteForce Time Taken --- %s seconds ---" % (time.time() - start_time))
    return counter
