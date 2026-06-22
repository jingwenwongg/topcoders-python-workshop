try:
    print ("Enter the number of matches")
    n = int(input())

    print("Enter the scores")

    total = 0

    for i in range(n):
        score = int(input())
        total += score
    
    print (f"Batting average: {total / n:.2f}")

except:
    print ("Type Error Exception")