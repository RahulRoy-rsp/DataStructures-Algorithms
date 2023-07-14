arr = list(map(int, input("Enter the numbers separated by space: ").split()))

print("Sorting the array... ")

def mergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

mergeSort(arr)
print("The sorted array is: ", arr)

                        
