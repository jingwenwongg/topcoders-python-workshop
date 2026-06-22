numlist = [2,3,1,5,6,7,1]
print(numlist)

print("Enter n")
n = int(input())

try:
    if n > len(numlist):
        raise IndexError

    print("Sum =", sum(numlist[:n]))

except:
    print("Index Value out of range")
