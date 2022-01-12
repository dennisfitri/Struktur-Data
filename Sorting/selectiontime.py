from time import time
from random import randint
#randint untuk batas tertinggi


def selection_sort(data):
    start = time()
    count = len(data)
    for k in range(count):
        j = count - k - 1
        big = 0
        for i in range(j + 1):
            if data[i] > data[big]:
                big = i
        data[j], data[big] = data[big], data[j]
    end = time()
    return end - start

data = [randint(0,100) for i in range(4_000)]
interval = selection_sort(data)
print(selection_sort(data))