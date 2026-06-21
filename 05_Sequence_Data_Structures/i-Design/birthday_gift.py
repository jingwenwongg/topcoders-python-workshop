num = int(input())

total_books = 0

for i in range(num):
    students = int(input())
    total_books += students

price = int(input())
total_cost = total_books * price

print(f"Total number of books required : {total_books}")
print(f"Total cost: {total_cost}")