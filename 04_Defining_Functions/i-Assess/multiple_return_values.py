def multiVarFunc():
    department = input("Enter department name:")
    total_students = int(input("Enter the number of total students:"))
    total_faculties = int(input("Enter the number of total faculties:"))

    return department, total_students, total_faculties

department, total_students, total_faculties = multiVarFunc()

print("Details:")
print("Department:" + department)
print("Total students:" + str(total_students))
print("Total faculties:" + str(total_faculties))