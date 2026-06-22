n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0
prev = 0

for i in range(n):
    available = A[i] - prev
    
    if B[i] <= available:
        count += 1
        
    prev = A[i]
    
print(count)