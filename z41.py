import random

def reverse(arr):
    last_row = arr.pop(len(arr)-1)
    first_row = arr.pop(0)
    arr.append(first_row)
    arr.insert(0, last_row)
    return arr
    

arr = [[], [], []]
for row in arr:
    for i in range(6):
        row.append(random.randint(0, 10))

print("BEFORE")
for row in arr:
    for i in row:
        print(i, end = " ")
    print("")

arr = reverse(arr)

print("AFTER")
for row in arr:
    for i in row:
        print(i, end = " ")
    print("")
