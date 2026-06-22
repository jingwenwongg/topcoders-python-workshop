input_file = open("input.txt", "r")

text = input_file.read()

input_file.close()

output_file = open("output.txt", "w")

output_file.write(text[::-1])

output_file.close()