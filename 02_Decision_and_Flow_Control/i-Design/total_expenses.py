cost = int(input())
num = int(input())

total = cost * num

if num < 50:
    discount = 0
elif num <= 100:
    discount = 10
elif num <= 200:
    discount = 20
elif num <= 400:
    discount = 30
elif num <= 500:
    discount = 40
else:
    discount = 50

final = total - (total * discount / 100)

print(f"{final:.2f}")