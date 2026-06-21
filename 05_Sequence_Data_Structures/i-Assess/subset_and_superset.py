set1 = set(map(int, input().split(',')))
set2 = set(map(int, input().split(',')))

print(set1.issubset(set2))
print(set2.issubset(set1))
print(set1.issuperset(set2))
print(set2.issuperset(set1))