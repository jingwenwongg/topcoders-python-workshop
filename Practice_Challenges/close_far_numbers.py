def close_far(a, b, c):
    return ((abs(a-b) <= 2 and abs(a-c) >= 3 and abs(b-c) >= 3) or
            (abs(a-c) <= 2 and abs(a-b) >=3 and abs(b-c) >= 3) or
            (abs(b-c) <= 2 and abs(a-b) >= 3 and abs(a-c) >= 3))
            
a = int(input())
b = int(input())
c = int(input())

print (close_far(a, b, c))