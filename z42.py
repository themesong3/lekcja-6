import random

def reverse(arr):
    for row in arr:
        pom = row[0]
        row[0] = row[-1]
        row[-1] = pom
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