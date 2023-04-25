
import os;

class Stack:

    data = []

    def length(self):
        return len(self.data)

    def reset(self):
        self.data.clear()

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
    
def process_line(stack, line):


    line = line.upper();

    tokens = line.split();
    if len(tokens) == 1 and tokens[0] == "CLEAR":
        os.system('clear')
    elif len(tokens) == 1 and tokens[0] == "RESET":
        stack.reset()
    else:
        for token in tokens:
            if is_num(token):
                stack.push(token)
            elif is_operator(token):
                if stack.length() < 2:
                    print("Stack to small for operation - minimum two elements required")
                    return stack
                elif not is_num(stack.peek(1)) or not is_num(stack.peek(0)):
                    print("Two top-most elements in stack must be numeric for operation")
                    return stack
                
                num2 = float(stack.pop())
                num1 = float(stack.pop())
                if token == '+':
                    stack.push(str(num1 + num2))
                elif token == '-':
                    stack.push(str(num1 - num2))
                elif token == '*':
                    stack.push(str(num1 * num2))
                elif token == '/':
                    stack.push(str(num1 / num2))

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
    stack = Stack()
    line = input("RPN> ")
    if line.upper() == "QUIT":
        break
    # Process line
    stack = process_line(stack, line).data
    print(stack)



print("Goodbye!")