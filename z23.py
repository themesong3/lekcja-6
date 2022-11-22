def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                pom = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = pom
    return arr 

arr1 = [4, 3, 2, 1, 1, 1, 5, 4, 3, 2, 8, 10]
arr2 = [4, 3, 6, 7, 2, 1, 3, 5]
arr3 = [6, 7, 4, 3, 6, 5, 7, 8, 90]

print(bubblesort(arr1))
print(bubblesort(arr2))
print(bubblesort(arr3))