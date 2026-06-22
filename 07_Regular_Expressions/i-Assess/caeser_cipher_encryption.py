import re

text = input()
n = int(input())

valid = True

for char in text:
    if ord(char) + n > 127:
        valid = False
        break

if valid:
    result = re.sub(r'.', lambda x: chr(ord(x.group()) + n), text)
    print(result)
else:
    print("invalid")