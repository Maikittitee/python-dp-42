arr1 = [2, 8, 9, 48, 8, 22, -12, 2]
arr2 = set(filter(lambda x: x != None, [c + 2 if c > 5 else None for c in arr1]))

print(arr1)
print(arr2)