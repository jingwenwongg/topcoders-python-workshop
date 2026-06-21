n = int(input())

balls = []

for i in range(n):
    balls.append(int(input()))

search_ball = int(input())

if search_ball in balls:
    print  ("Got It!")
else:
    print ("Sorry!")