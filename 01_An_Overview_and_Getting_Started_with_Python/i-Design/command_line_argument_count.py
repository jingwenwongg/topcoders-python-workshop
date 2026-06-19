import sys

print ("Arguments : ")
for arg in sys.argv[1:]:
    print (arg)

total = len(sys.argv) - 1

print (f"Number of arguments is {total}")