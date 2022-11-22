arr = [[0,0,0],[0,0,0],[0,0,0]]

for row in range(len(arr)):
    numOfRow = row
    for i in range(len(arr[row])):
            if numOfRow == i:
                arr[row][i] = 1

print(arr)