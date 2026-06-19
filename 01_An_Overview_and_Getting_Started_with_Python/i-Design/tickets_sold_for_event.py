x = int(input("Enter the value of X"))
y = int(input("Enter the value of Y"))

children = (y - 5 * x) // 13
adult = children + x
senior = 2 * children

print (f"Number of children tickets sold : {children}")
print (f"Number of adult tickets sold : {adult}")
print (f"Number of senior tickets sold : {senior}")