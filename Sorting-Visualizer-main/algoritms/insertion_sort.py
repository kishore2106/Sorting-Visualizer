import time


def insertionSort(array, drawrectangle, delay):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
            drawrectangle(array, ['blue' if x == j else 'green' if x == j +
                          1 else 'gray' if x < step-2 else 'black' for x in range(len(array))])
            time.sleep(delay)
        # Place key at after the element just smaller than it.
        array[j + 1] = key
    drawrectangle(array, ['blue' for x in range(len(array))])