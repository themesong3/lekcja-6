arr = [[-38, 19], [5,40],[-7,11],[29,16]]
minimum = min(min(arr))
maximum = max(max(arr))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == maximum:
            max_row = i
            max_col = j
        if arr[i][j] == minimum:
            min_row = i
            min_col = j

print(f"Minimum: {minimum} row: {min_row+1} col: {min_col+1}")
print(f"Maximum: {maximum} row: {max_row+1} col: {max_col+1}")