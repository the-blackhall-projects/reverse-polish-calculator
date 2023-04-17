# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

def process_line(line):
    return line.upper()

# Basic loop for the program
while True:
    line = input("] ")
    if line.upper() == "BYE":
        break
    # Process line
    print(process_line(line))



print("Goodbye!")


