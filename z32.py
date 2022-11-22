def list_to_string(arr):
    word = ""
    for i in range(len(arr)-1):
         word += str(arr[i])
         word += ", "
    word += str(arr[-1])
    return word


arr = [1, 2, 3, 4, 5, 6]
print(list_to_string(arr))