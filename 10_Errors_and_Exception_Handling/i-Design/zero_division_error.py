try:
    print("Enter number 1")
    x = int(input())

    print("Enter number 2")
    y = int(input())

    print (x / y)

except ZeroDivisionError:
    print ("Divide By Zero Error")