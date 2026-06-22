cards = {'R': 10, 'Q': 10, 'P': 7, 'S': 5}

print ("Enter number of time player can flip the card")
n =int(input())

arun = 0
arya = 0

for i in range(n):
    print ("Arun flip the card")
    card = input().strip()
    num = int(input())
    arun += cards[card] * num
    
    print("Arya flip the card")
    card = input().strip()
    num = int(input())
    arya += cards[card] * num
    
print ("Total scores ", arun, arya)

if arun > arya:
    print ("Arun won the game")
elif arya > arun:
    print ("Arya won the game")
else:
    print ("Game tied")