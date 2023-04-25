# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os;

class Stack:

    data = []

    def reset(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
    
    def top(self):
        return self.data[-1]
    
    def peek(self, index):
        return self.data[-1 - index]
        

def is_num(str):
    #If you expect None to be passed:
    retVal = True
    
    try:
        float(str)
    except ValueError:
        retVal = False

    return retVal

def is_operator(str):
    return str in {'+', '-', '*', '/', '^'}
    
def process_line(line):

    stack = Stack()

    line = line.upper();

    tokens = line.split();
    if len(tokens) == 1 and tokens[0] == "CLEAR":
        os.system('clear')
        return []
    elif len(tokens) == 1 and tokens[0] == "RESET":
        stack.reset()
    else:
        for token in tokens:
            if is_num(token):
                stack.push(token)
            elif is_operator(token):
                if token == '+':
                    stack.push( float(stack.pop()) + float(stack.pop()))
                if token == '-':
                    stack.push( -float(stack.pop()) + float(stack.pop()))


    

    return stack

os.system('clear')

print("+------------------------------------------+")
print("|  Internet Reverse Polish Calculator V1.0 |")
print("+------------------------------------------+")
print('\nType "quit" to quit.\n')
print('Type "reset" to clear stack.\n')
print('Type "clear" to clear screen.\n')




# Basic loop for the program
while True:
    line = input("] ")
    if line.upper() == "QUIT":
        break
    # Process line


    print(process_line(line).data)



print("Goodbye!")


