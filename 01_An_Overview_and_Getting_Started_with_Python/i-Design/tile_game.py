side = int(input("Enter the side in cm of a square tile"))
num = int(input("Enter the number of square tiles available"))

tiles_per_side = int(num ** 0.5)
large_square_side = tiles_per_side * side
largest_area = large_square_side * large_square_side

print (f"Area of the largest possible square is {largest_area}sqcm")