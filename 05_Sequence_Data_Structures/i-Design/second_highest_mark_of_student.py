student_count = int(input())

students = {}

for i in range(student_count):
    data = input().split()

    name = data[0]
    marks = list(map(float, data[1:]))

    students[name] = marks

student_name = input()

if student_name not in students:
    print("Student doesn't exist")
else:
    marks = students[student_name]

    if len(set(marks)) == 1:
        print(f"{student_name} scored same marks in all subjects: {marks[0]:.0f}")
    else:
        marks.sort(reverse=True)
        print(f"Second Highest mark of {student_name}: {marks[1]:.0f}")