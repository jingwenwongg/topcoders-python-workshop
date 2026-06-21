text = input()
character = input()

parts = text.split(character)

print("Strings after splitting")

for word in parts:
    print(word.capitalize())