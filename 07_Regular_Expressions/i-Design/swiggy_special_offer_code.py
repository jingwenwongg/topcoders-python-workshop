text = input()

if all(vowel in text for vowel in "aeiou"):
    print("Accepted")
else:
    print("Not Accepted")