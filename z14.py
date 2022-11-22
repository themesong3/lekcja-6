arr = [[True,False],[True,True],[False,False]]

for row in arr:
    for i in range(len(row)):
        if row[i] == True:
            row[i] = False
        else:
            row[i] = True

print(arr)