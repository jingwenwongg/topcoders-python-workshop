class CustomError(Exception):
    pass

print("Enter the username")
username = input()

print("Enter the password")
password = input()

try:
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)

    if not (has_lower and has_upper and has_digit):
        raise CustomError

    print("Employee Username:", username)
    print("Password:", password)

except CustomError:
    print("CustomException: Invalid Password Exception")