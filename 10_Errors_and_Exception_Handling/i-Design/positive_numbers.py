while True:
    try:
        print ("Enter a positive integer")
        n = int(input())

        if n <= 0:
            raise ValueError

        print(f"Good! You entered {n}")
        break

    except ValueError:
        print("You entered a negative number. Retry!")   