num = int(input())

if num < 10:
    print ("Invalid Input")
else:
    last_digit = num % 10

    first_digit = num
    while first_digit >= 10:
        first_digit = first_digit // 10
    
    difference = abs(first_digit - last_digit)

    print (difference)