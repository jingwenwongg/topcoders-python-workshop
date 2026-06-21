def greet(name, message = "Welcome to Python Programming"):
    print (f"Hello {name}, {message}")

print("""
Menu
1. Name and Message
2. Name
""")

choice = int(input())
name = input("Enter the name")

if choice == 1:
    message = input("Enter the message")
    greet(name, message)
elif choice == 2:
    greet(name)