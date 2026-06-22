file = open("averageLength.txt", "r")

text = file.read()

words = text.split()

total_length = 0

for word in words:
    total_length += len(word)

average = total_length // len(words)

print(average)

file.close()