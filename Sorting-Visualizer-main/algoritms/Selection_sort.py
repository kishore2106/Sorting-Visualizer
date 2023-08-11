import time


def selectionSort(array, size, drawrectangle, delay):

    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
        # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        drawrectangle(array, ['blue' if x == ind else 'green' if x ==
                      min_index else 'gray' if x <= ind else 'black' for x in range(len(array))])
        time.sleep(delay)
    drawrectangle(array, ['blue' for x in range(len(array))])