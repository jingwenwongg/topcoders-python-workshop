basic_salary = int(input())

if basic_salary < 15000:
    hra = 0.15 * basic_salary
    da = 0.90 * basic_salary
else:
    hra = 5000
    da = 0.98 * basic_salary

gross_salary = basic_salary + hra + da

print (f"{gross_salary:.2f}")