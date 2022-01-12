def partition(array, low, high):
	# memilih elemen paling kanan sebagai pivot
	pivot = array[high]

	i = low - 1 

	for j in range(low, high):
		if array[j] >= pivot:
			# jika elemen yang lebih kecil dari pivot ditemukan, tukar dengan elemen yang lebih besar yang ditujukan okeh i
			i = i + 1
            
			(array[i], array[j]) = (array[j], array[i])
		# swap ppivot dengan element
	(array[i + 1], array[high]) = (array[high], array[i + 1])
	return i + 1

def quick_sort(array, low, high):
	if low < high:
		pi = partition(array, low,high)
		quick_sort(array, low, pi - 1)
		quick_sort(array, pi + 1, high)

data = [1,5,3,7,2,8,4,0,9]
size = len(data)
quick_sort(data, 0, size - 1)
print("Urutan array dari yang terbesar", data)