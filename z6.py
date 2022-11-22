arr = [2, 3, 7, 5, 4]
print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[len(arr)-1])
print(arr[-2])
print(arr[-1] + arr[-2])
middle = len(arr) // 2
print(arr[middle])
for i in arr:
    print(i, end=" ")
print("")
for i in range(middle+1):
    print(arr[i], end=" ")