clients = {}

n = int(input("Enter the number of clients"))

for i in range(1, n + 1):
    print(f"Enter the details of the client {i}")

    name = input()
    email = input()
    passport = input()

    clients[passport] = [name, email]

search_passport = input("Enter the passport number of the client to be searched")

if search_passport in clients:
    print("Client Details")

    name = clients[search_passport][0]
    email = clients[search_passport][1]

    print(f"{name}--{email}--{search_passport}")
else:
    print("Client not found")