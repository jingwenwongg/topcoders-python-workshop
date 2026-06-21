print ("Enter the two positive numbers")
num1 = int(input())
num2 = int(input())

while num2 != 0:
    num1, num2 = num2, num1 % num2

print("GCD:", num1, sep="")