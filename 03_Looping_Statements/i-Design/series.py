n = int(input())

odd = 30
even = 35

for i in range(1, n + 1):
    if i % 2 != 0:
        print (odd, end=" ")
        odd = odd + (8 * ((i + 1) // 2))
    else:
        print (even, end=" ")
        even = even + (6 * (i // 2))