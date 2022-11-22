import random

def rand_elem(arr):
    re = random.randint(0, len(arr))
    return arr[re]
arr = [1, 2, 3, 4, 5, 6]
print(rand_elem(arr))