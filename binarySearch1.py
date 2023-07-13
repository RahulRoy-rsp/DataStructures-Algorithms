arr = list(map(int, input("Enter the numbers separated by space: ").split()))

toSearch = int(input("Enter an element to search to the arr: "))

print("Searching", toSearch, "in array:", arr)


def binSearch(arr, toSearch):
    left = 0
    mid = 0
    right = len(arr) - 1

    while (left <= right):
        mid = (left + right)//2
        if arr[mid] < toSearch:
            left = mid + 1
        elif arr[mid] > toSearch:
            right = mid - 1
        else:
            return mid
            
    return None

val = binSearch(arr, toSearch)

if val != None:
    print(toSearch, "found at index", val, "in", arr)
else:
    print(f"{toSearch} not found in any index of {arr}")
