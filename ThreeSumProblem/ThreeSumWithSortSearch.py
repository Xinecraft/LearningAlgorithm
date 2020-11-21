import time
import numpy

start_time = time.time()


def threeSumCount(array):
    counter = 0
    length_range = range(len(array))
    array.sort()
    for i in length_range:
        for j in length_range[i + 1:]:
            if -(array[i] + array[j]) in array:
                counter += 1
    return counter


# Test
k = numpy.random.randint(-10000, 10000, 400)
print(threeSumCount(k))

print("Time Taken --- %s seconds ---" % (time.time() - start_time))
