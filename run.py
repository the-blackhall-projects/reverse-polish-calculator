# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os;

def process_line(line):
    line = line.upper();

    tokens = line.split();
    if len(tokens) == 1 and tokens[0] == "CLEAR":
        tokens = []
        os.system('clear')

    return tokens

os.system('clear')

print("+------------------------------------------+")
print("|  Internet Reverse Polish Calculator V1.0 |")
print("+------------------------------------------+")
print("\nType quit to quit.\n")



# Basic loop for the program
while True:
    line = input("] ")
    if line.upper() == "QUIT":
        break
    # Process line


    print(process_line(line))



print("Goodbye!")


