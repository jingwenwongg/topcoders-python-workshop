def daysInYear(year, leap = False):

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        leap = True

    if leap:
        print (f"{year} is a leap year")
    else:
        print (f"{year} is not a leap year")
    
year = int(input())
daysInYear(year)