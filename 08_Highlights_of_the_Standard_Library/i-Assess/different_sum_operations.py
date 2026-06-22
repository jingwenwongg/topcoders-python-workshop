from math import floor, ceil

numbers = list(map(float, input().split()))

total = sum(numbers)

print(float(floor(total) - ceil(total)))
print(float(ceil(total) - round(total)))
print(float(floor(total) - round(total)))