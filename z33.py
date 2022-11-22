def digits(n):
    l = len(str(n))
    return l

arr = [1, 2, 6, 90, 80, 637, 888, 999, 100]
line_top_bottom = ""
line_mid = ""

for i in range(len(arr)-1):
    line_top_bottom += "------"

for i in arr:
    line_mid += "|"
    for j in range(4 - digits(i)):
        line_mid += " "
    line_mid += str(i)
line_mid += "|"

print(line_top_bottom)
print(line_mid)
print(line_top_bottom)
