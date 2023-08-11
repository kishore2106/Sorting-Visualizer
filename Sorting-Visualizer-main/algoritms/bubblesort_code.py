import time


def bubble_sort(data, drawrectangle, delay):
    for i in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                try:
                    drawrectangle(data, [
                        'blue' if x == j else 'green' if x == j+1 else 'gray' if x >= len(data)-i else 'black' for x in range(len(data))
                    ])
                    time.sleep(delay)
                except:
                    pass

    drawrectangle(data, ['blue' for x in range(len(data))])