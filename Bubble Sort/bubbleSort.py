inp = list(map(int, input("Enter numbers separated by space: ").split()))
print("Entered Array before Sorting is", inp)

def bubbleSort(arr):
	for i in range(len(arr)):
		for j in range(0, len(arr) - i - 1):
			
			if arr[j] > arr[j + 1]:
				arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubbleSort(inp)

print("Entered Array After Sorting is:", inp)

# This is often not used because of O(n2) Time Complexity.
