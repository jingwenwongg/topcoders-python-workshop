name = input()

length = len(name)

if length % 2 == 0:
    palindrome = name[:length // 2] + name[:length // 2][::-1]
else:
    palindrome = name[:length // 2 + 1] + name[:length // 2][::-1]

print(palindrome)