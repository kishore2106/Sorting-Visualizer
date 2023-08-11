import time
# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot

# to come up with a "sorted" nums relative to the pivot
# Function to find the partition position


def partition(array, low, high, drawrectangle, delay):

    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
            drawrectangle(array, ['blue' if x == i else 'green' if x ==
                          j else 'white' if x ==
                          pivot else 'black' for x in range(len(array))])
            time.sleep(delay)

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    drawrectangle(array, ['blue' if x == i+1 else 'green' if x ==
                  high else 'black' for x in range(len(array))])
    time.sleep(delay)
    drawrectangle(array, ['blue' for x in range(len(array))])

    # Return the position from where partition is done
    return i + 1

# function to perform quicksort


def quickSort(array, low, high, drawrectangle, delay):
    if low < high:

        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high, drawrectangle, delay)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1, drawrectangle, delay)

        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high, drawrectangle, delay)


# data = [1, 7, 4, 1, 10, 9, -2]
# print("Unsorted Array")
# print(data)

# size = len(data)

# quickSort(data, 0, size - 1)

# print('Sorted Array in Ascending Order:')
# print(data)
