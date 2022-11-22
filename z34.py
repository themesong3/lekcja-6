def isSubset(arr1, arr2):
    a1 = set(arr1)
    a2 = set(arr2)
    for i in a1:
        if i not in a2:
            return False
    return True



arr1 = [1, 2, 7, 10]
arr2 = [4,7,8,3,2,8,9,0,1,5,7]

print(isSubset(arr1, arr2))