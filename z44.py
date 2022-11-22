def display_array(arr):
    for row in arr:
        for i in row:
            print(i, end = " ")
        print("")

def transpose_matrix(arr):
    rows = len(arr)
    cols = len(arr[0])
    new_arr = []
    for i in range(cols):
        new_arr += [[0]*rows]

    for x in range(len(new_arr)):
        for y in range(len(new_arr[x])):
            new_arr[x][y] = arr[y][x]


    display_array(new_arr)


arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose_matrix(arr)
