arr = [1, 2, 3, 4, 5]

arr[0] -= 1
print(arr)

arr[-1] += 4
print(arr)

middle = len(arr) // 2
arr[middle] *= 2
print(arr)

for i in range(len(arr)):
    arr[i] += 3
print(arr)