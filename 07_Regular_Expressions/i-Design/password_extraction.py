text = input()

num = []
current_num = ""

for char in text:
    if char.isdigit():
        current_num += char
    else:
        if current_num != "":
            num.append(int(current_num))
            current_num = ""

if current_num != "":
    num.append(int(current_num))

if len(num) == 0:
    print ("No Password")
else:
    print(max(num))