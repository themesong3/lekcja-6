def create_2d_arr(x,y):
    arr = []
    for i in range(x):
        sub_arr = [0] * y
        arr.append(sub_arr)
    return arr

print(create_2d_arr(3, 5))