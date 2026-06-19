salary = float(input("Enter the total salary paid"))

weekend = int((salary - 800) / 130)
weekday = weekend + 10

print (f"Number of weekday hours is {weekday}")
print (f"Number of weekend hours is {weekend}")