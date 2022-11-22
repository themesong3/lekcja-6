arr = [
    [1,2,3,4,5],
    [2,0,0,0,0],
    [3,0,0,0,0],
    [4,0,0,0,0],
    [5,0,0,0,0]
]

r = 1
c = 1
while r < len(arr):
    while c < len(arr[0]):
        arr[c][r] = arr[r][0] * arr[0][c]
        c += 1
    r += 1
    c = 1

for row in arr:
        for i in row:
            print(i, end = " ")
        print("")
    