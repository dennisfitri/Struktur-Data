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

data = [7, 5, 2, 8, 9, 1, 0, 6, 3, 4]
merge_sort(data)
print(data)
