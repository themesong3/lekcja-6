def oneInstance(n, arr):
    counter = 0
    for i in arr:
        if i == n:
            counter += 1
    if counter > 1:
        return False
    else:
        return True

arr = [2, 3, 2, 5, 8, 1, 9, 8]
new_arr = []

for i in arr:
    if oneInstance(i, arr):
        new_arr.append(i)

print(new_arr)