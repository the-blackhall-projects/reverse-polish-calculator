
import os;
import math;

class Stack:

    __data = []

    def length(self):
        return len(self.__data)

    def reset(self):
        self.__data.clear()

    def push(self, item):
            self.__data.append(item)

    def pop(self):
        return self.__data.pop()
    
    def top(self):
        return self.__data[-1]
    
    def peek(self, index):
        return self.__data[-1 - index]
    
    def show(self):
        retVal = ""
        for element in self.__data:
            if is_num(element):
                num = float(element)
                if num == int(num):
                    retVal += " " + str(int(num))
                else:
                    retVal += " " + str(num)
            else:
                retVal += " " + element

        retVal = retVal.strip()

        if len(retVal) == 0:
            retVal = "(empty)"

        return "Stack: " + retVal

            

        

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

def is_function(str):
    return str in {"SIN", "COS", "TAN"}


    
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
                    print("Stack to small for operation - minimum two operands required for", token)
                    return
                elif not is_num(stack.peek(1)) or not is_num(stack.peek(0)):
                    print("Two top-most elements in stack must be numeric for operation", token)
                    return
                
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
            elif is_function(token):
                if stack.length() < 1:
                    print("Stack to small for operation - minimum one parameter required for", token)
                    return
                elif not is_num(stack.peek(0)):
                    print("Top-most element in stack must be numeric for", token)
                    return

                num = float(stack.pop())
                if token == "SIN":
                    stack.push(str(math.sin(num)))
                elif token == "COS":
                    stack.push(str(math.cos(num)))
                elif token == "TAN":
                    stack.push(str(math.tan(num)))
            else:
                print("Token",token,"not recognised.")
    return

os.system('clear')

print("+------------------------------------------+")
print("|  Internet Reverse Polish Calculator V1.0 |")
print("+------------------------------------------+")
print('\nType "quit" to quit.\n')
print('Type "reset" to clear stack.\n')
print('Type "clear" to clear screen.\n')



stack = Stack()
print(stack.show())


# Basic loop for the program
while True:
    line = input("RPN > ")
    if line.upper() == "QUIT":
        break
    # Process line
    process_line(stack, line)
    print(stack.show())



print("Goodbye!")