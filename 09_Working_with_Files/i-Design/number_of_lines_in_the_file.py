file = open("input.txt", "r")

count = len(file.readlines())

print ("The file has", count, "lines")

file.close()