def convert_array(arr):
    new_arr = []
    for row in arr:
        for i in row:
            new_arr.append(i)
    return new_arr
arr = [[1, 2], [3, 4]]
print(convert_array(arr))