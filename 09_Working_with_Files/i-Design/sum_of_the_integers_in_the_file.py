file = open("sample.txt", "r")

total = 0

for line in file:
    total += int(line)

print("The sum of the integers in the file sample.txt is:", total)

file.close()