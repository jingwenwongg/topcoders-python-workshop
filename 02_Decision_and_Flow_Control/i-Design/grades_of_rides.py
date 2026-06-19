hurl, spin, speed = map(int, input().split())

condition1 = hurl > 50
condition2 = spin > 60
condition3 = speed > 100

if condition1 and condition2 and condition3:
    print (10)
elif condition1 and condition2:
    print (9)
elif condition2 and condition3:
    print (8)
elif condition1 and condition3:
    print (7)
elif condition1 or condition2 or condition3:
    print (6)
else:
    print (5)