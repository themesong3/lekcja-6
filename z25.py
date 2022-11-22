def occurs(n, arr):
    for i in arr:
        if i == n:
            return True
    return False

arr = [1, 2, 3, 4, 5]
my_num = int(input("Give me a number: "))
print(f"Array: {arr}")

if occurs(my_num, arr):
    print("Your number occurs in the array")
else:
    print("Your number DOES NOT occur in the array")