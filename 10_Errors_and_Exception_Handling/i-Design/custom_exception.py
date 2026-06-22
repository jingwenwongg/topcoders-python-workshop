class NotEligibleException(Exception):
    pass

class Student:
    def __init__(self, marks):
        self.marks = marks

    def check_marks(self):
        if self.marks >= 90:
            return True
        else:
            raise NotEligibleException

print("Enter marks of student")
marks = int(input())

s = Student(marks)

try:
    if s.check_marks():
        print("Eligible")
except NotEligibleException:
    print ("Inside Except Block : Not Eligible")