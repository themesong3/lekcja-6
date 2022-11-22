def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] > arr[j+1]:
                pom = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = pom
    return arr

def median(arr):
    arr = bubblesort(arr)
    length = len(arr)
    if length % 2 != 0:
        median = arr[len(arr)//2]
    else:
        val1 = arr[len(arr)//2]
        val2 = arr[(len(arr)//2)-1]
        median = (val1 + val2) /2
    return median

arr1 = [1,0,9,4,6,9]
arr2 = [6,8,3,1,0,5,7]


print(bubblesort(arr1))
print(median(arr1))

print(bubblesort(arr2))
print(median(arr2))