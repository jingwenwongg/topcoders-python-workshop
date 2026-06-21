def multiply(a, b=10):
    print("The result is", a * b)

a = int(input())
b = int(input())

multiply(a)
multiply(a, b)
multiply(a, b=9)