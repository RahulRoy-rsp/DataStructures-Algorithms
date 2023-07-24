inp = list(map(int, input("Enter numbers separated by space: ").split()))
toSearch = int(input("Enter a number you want to search: "))

print(f"Searching {toSearch} in {inp}")
def linSearch(inp, s):
  for x in range(len(inp)):
    if inp[x] == s:
      return x
  return None

ans = linSearch(inp, toSearch)  
if ans != None:
  print(f"Number {toSearch} found at position {ans} in the list")
else:
  print(f"Number {toSearch} not found in the list")
