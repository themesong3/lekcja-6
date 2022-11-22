arr = [1,2, 3, 4, 5, 6]
my_num = int(input("Give me a number: "))
counter = 0
for i in arr:
    if i > my_num:
        counter += 1
print(f"There are {counter} numbers greater that {my_num} in array {arr}")
