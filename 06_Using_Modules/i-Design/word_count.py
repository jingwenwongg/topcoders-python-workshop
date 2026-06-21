sentence = input("Enter the String").lower()

words = sentence.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word in sorted(word_count):
    print (word + "-" + str(word_count[word]))