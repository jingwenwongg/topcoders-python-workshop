n = int(input())

mid = n // 2

for i in range(n):
    for j in range(n):
        if i == mid and j == mid:
            print("*", end="")
        else:
            print("~", end="")
    print()