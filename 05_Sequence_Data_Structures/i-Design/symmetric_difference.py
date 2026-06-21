set1 = set(map(int, input().split(',')))
set2 = set(map(int, input().split(',')))

result = sorted(set1.symmetric_difference(set2))

if len(result) == 0:
    print ("invalid set")
else:
    print (set(result))