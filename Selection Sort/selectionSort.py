inp = list(map(int, input("Enter numbers separated by space: ").split()))
print("Entered Array before Sorting is:", inp)

def selection_sort(nums):
    for i in range(len(nums)):
        smallest = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
            
        nums[i], nums[smallest] = nums[smallest], nums[i]
    
    return nums
  
ans = selection_sort(inp)
print("Entered Array after Sorting is:", ans)
