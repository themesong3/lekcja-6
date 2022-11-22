def display_array(arr):
    for row in arr:
        for i in row:
            print(i, end = " ")
        print("")

def identity_matrix(n):
    arr = []
    for i in range(n):
        arr += [[0]*n]
    
    for i in range(n):
        arr[i][i] = 1
    display_array(arr)

identity_matrix(3)
