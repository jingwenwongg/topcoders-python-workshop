n = int(input("Enter total Number of sheets:"))

attendance_sheets = []
register_num = []

for i in range(n):
    sheet = tuple(map(int, input().split()))
    attendance_sheets.append(sheet)

    for number in sheet:
        register_num.append(number)

print("Attendance Sheets with Register Number:", tuple(attendance_sheets))

final_sheet = tuple(sorted(set(register_num)))

print("Final sheet:", final_sheet)