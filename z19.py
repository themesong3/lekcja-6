arr = [15, 8, 31, 47, 2, 19]
arr = sorted(arr)
print(arr)
arr_even = False
if len(arr) % 2 == 0:
    arr_even = True

median_pos = len(arr) // 2

if arr_even:
    median = (arr[median_pos] + arr[median_pos -1])/2
else:
    median = arr[median_pos]

print(median)