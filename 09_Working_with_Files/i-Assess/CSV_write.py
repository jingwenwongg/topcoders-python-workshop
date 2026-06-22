n = int(input())

file = open("salaryData.csv", "w")

for i in range(n):
    name = input()
    salary = input()
    file.write(name + "," + salary + "\n")

file.close()

file = open("salaryData.csv", "r")

for line in file:
    print(line.strip())

file.close()