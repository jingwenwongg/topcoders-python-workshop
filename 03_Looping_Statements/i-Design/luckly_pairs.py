richie, riya, turns = map(int, input().split())

for turn in range(1, turns + 1):
    if turn % 2 != 0:
        richie = richie * 2
    else:
        riya = riya * 2

sum = richie + riya
print (sum)