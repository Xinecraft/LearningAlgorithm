def sortArray(array):
    length_range = range(len(array))
    for i in length_range:
        min_index = i
        for j in length_range[i + 1:]:
            if array[j] < array[min_index]:
                min_index = j
        swap(array, i, min_index)


def swap(array, i, min_index):
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp


# test = [5, 1, 4, 7, 2, 11, 1, 5, 3, -2, 10]
# sortArray(test)
# print(test)
