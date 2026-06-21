def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


n = int(input())
t = int(input())

for i in range(t):
    total = 0

    for number in range(2, n + 1):
        if is_prime(number):
            total += number

    n = total

print("Sum:" + str(n))