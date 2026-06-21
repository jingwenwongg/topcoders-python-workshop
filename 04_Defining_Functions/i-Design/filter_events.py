n = int(input("Enter size of list"))

if n > 0:
    num = []

    print ("Enter the elements in list")
    for i in range(n):
        num.append(int(input()))

    result = list(filter(lambda x: x % 13 == 0, num))

    for num in result:
        print (num, end=" ")

else:
    print ("Invalid input")