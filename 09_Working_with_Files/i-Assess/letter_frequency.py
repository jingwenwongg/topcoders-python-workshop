from collections import Counter

file = open("frequencyFile.txt", "r")

text = file.read().lower()

file.close()

freq = Counter(ch for ch in text if ch.isalpha())

for ch in sorted(freq):
    print(f"{ch}: {freq[ch]}")