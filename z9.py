arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
lengths = []
for i in arr:
    lengths.append(len(i))
longest_n = max(lengths)

for i in range(len(lengths)):
    if longest_n == lengths[i]:
        longest_name = arr[i]
print(longest_name)