try:
    print("Enter number 1")
    val1 = input()
    
    print("Enter number 2")
    val2 = input()
    
    if val2 == '0' or val2 == 'O' or val2 == 'o':
        result = int(val1) / 0
    else:
        result = int(val1) / int(val2)
        
    print(result)

except ZeroDivisionError:
    print("Divide By Zero Error")
    
except ValueError:
    print("Invalid Value")