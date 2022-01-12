from time import time
from random import randint


def bubble_sort(data):
    start = time()
    n = len(data) # jumlah list
    # perulangan pertama
    for i in range(n-1): 
        # perulangan kedua
        for j in range(n - i - 1):
            # bandingkan masing" elemen
            if data[j] > data[j + 1]:
                # jika lebih besar, tukar.
                data[j], data[j + 1] = data[j + 1], data[j]
    end = time()
    return end - start

data = [randint(0,100) for i in range(4_000)]
interval = bubble_sort(data)
print(bubble_sort(data))