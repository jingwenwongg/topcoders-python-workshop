n = int(input())

term = 21
diff = 4

for i in range(n):
    print (term, end=" ")
    term += diff
    diff *= 2