def addition(n1,n2):
    return n1 + n2
def subtraction(n1,n2):
    return n1 - n2
def multiplication(n1,n2):
    return n1 * n2
def division(n1,n2):
    return n1 / n2
def modulus(n1,n2):
    return n1 % n2

print ("""
Select the operation
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus
""")

choice = int(input("Enter the choice(1/2/3/4/5):"))

if choice >= 1 and choice <= 5:
    n1 = int(input("Enter the first number"))
    n2 = int(input("Enter the second number"))

    if choice == 1:
        print (f"{n1} + {n2} = {addition(n1, n2)}")
    elif choice == 2:
        print (f"{n1} - {n2} = {subtraction(n1, n2)}")
    elif choice == 3:
        print (f"{n1} * {n2} = {multiplication(n1, n2)}")
    elif choice == 4:
        print (f"{n1} / {n2} = {division(n1, n2)}")
    elif choice == 5:
        print (f"{n1} % {n2} = {modulus(n1, n2)}")
else:
    print ("Invalid Input")