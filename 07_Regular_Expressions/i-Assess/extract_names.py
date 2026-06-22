import re

text = input()

names = re.findall(r'(?:[A-Z]\.)*[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', text)

for name in names:
    print(name)