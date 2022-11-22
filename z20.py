def star(n):
    for i in n:
        stars = ""
        for j in range(i):
            stars += "*"
        print(f"{i}: {stars}")


arr = [12, 6, 4, 9, 10]
star(arr)