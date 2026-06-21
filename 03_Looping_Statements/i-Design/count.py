num_count = int(input())

even = 0
odd = 0

for i in range(num_count):
    num = int(input())

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print (even, odd)