def even_odd(arr):
    odd = []
    even = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    new_arr = even + odd
    return new_arr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(even_odd(arr))