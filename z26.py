def second_largest(arr):
    largest = max(arr)
    dif_min = largest - arr[0]
    for i in arr:
        if i != largest:
            dif = largest - i
            if dif < dif_min:
                sec_largest = i
                dif_min = dif
    return sec_largest



arr = [5, 7, 9, 8, 10]
print(second_largest(arr))