file = open("SalariesDataSet.csv", "r")

for line in file:
    print(line.strip().replace(",", ";"))

file.close()