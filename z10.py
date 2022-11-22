arr = [4,7,1,3,6,7,8,9,7,8,9]
odd = 0
even = 0
for i in arr:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"odd: {odd}, even:{even}")