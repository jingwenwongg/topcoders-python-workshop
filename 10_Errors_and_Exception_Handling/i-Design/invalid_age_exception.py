class CustomError(Exception):
    def __init__(self, message):
        self.message = message

print ("Enter the Name")
name = input()

print ("Enter the age")
age = int(input())

try:
    if age < 18:
        raise CustomError("InvalidAgeRangeException")

    print("Voter name:", name)
    print("VOter age:", age)

except CustomError as e:
    print ("CustomException:", e.message)