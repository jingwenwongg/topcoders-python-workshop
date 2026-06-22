phone_num = input()

if phone_num.startswith("+91-") and len(phone_num) == 14 and phone_num[4:].isdigit():
    print("Not a Spam Call")
else:
    print("Spam Call")