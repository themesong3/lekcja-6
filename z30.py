def minmax(arr):
    arr2 = []
    arr2.append(min(arr))
    arr2.append(max(arr))
    return arr2

arr = [1,2,3,4,56,10]
print(minmax(arr))