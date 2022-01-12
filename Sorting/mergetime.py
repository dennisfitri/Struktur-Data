from time import time
from random import randint

def merge (a, b):
    result = []
    while a and b:
        if a[0] < b[0]:
            less = a.pop(0) if a[0] < b[0] else b.pop(0)
            result.append(less)
        return result + a + b

def merge_sort(data):
    count = len (data) 
    if count > 1:
        a = data [0:count//2]
        b = data [count//2:]
        merge_sort(a)
        merge_sort(b)
        data[0:] = merge(a, b) #artinya mengarahkan data menuju tempat lain jadi mengganti di posisi semula, kalo gak begini maka akan menuju ke memori lain

data = [randint(0, 100) for i in range(10_000)]
start = time()
merge_sort(data)
end = time()
print(end - start)
