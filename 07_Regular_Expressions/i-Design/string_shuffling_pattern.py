word1 = input()
word2 = input()

result = ""

i = 0
j = len(word2) - 1

while i < len(word1) and j >= 0:
    result += word1[i]
    result += word2[j]
    i += 1
    j -= 1

result += word1[i:]
result += word2[:j + 1]

print (result)