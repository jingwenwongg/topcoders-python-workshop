def summation(n, m):
    if m ==1:
        return n * (n + 1) // 2
    
    return summation(summation(n, m - 1), 1)
    
n = int(input())
m = int(input())

print (summation(n, m))