a = int(input())
b = int(input())

for number in range(a, b + 1):

    if number < 2:
        continue

    is_prime = True

    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")