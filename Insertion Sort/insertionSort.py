inp = list(map(int, input("Enter numbers separated by space: ").split()))
print("Entered Array before Sorting is: ", inp)


def insertionSort(arr):
	n = len(arr)
	
	for i in range(1, n):
		temp = arr[i]
		j = i-1
		while j >= 0 and temp < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = temp


insertionSort(inp)
print("Entered Array after Sorting is: ", inp)
