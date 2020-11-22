def sortArray(array):
    length_range = range(len(array))
    for i in length_range:
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                swap(array, j, j-1)
            else:
                break


def swap(array, i, min_index):
    temp = array[i]
    array[i] = array[min_index]
    array[min_index] = temp


# test = [5, 1, 4, 7, 2, 11, 1, 5, 3, -2, 10]
# sortArray(test)
# print(test)
