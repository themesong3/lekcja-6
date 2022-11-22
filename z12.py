arr = [[2,5,4],[9,0,3]]

print(arr)

rows = len(arr)
cols = len(arr[0])
print(f"rows: {rows}  cols: {cols}")

print(arr[0][1])

print(arr[-1][-1])

for i in arr[1]:
    print(i, end = " ")
print("")

for i in arr[0]:
    print(i, end = " ")
print("")

for row in arr:
    print(row[-1])
    print("")