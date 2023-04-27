
import os
import math
import random

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
   
    def show(self):
        retVal = ""
        for num in self.__data:
            if num == int(num):
                retVal += " " + str(int(num))
            else:
                retVal += " " + str(num)

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
    return str in {'+', '-', '*', '/', '^', 'MOD'}

def is_function(str):
    return str in {"SIN", "COS", "TAN", "ABS", "ATN", "COT", "EXP", "INT", "LOG", "SQR", "SGN"}


def is_no_arg_function(str):
    return str in {"RND"}

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def process_no_arg_function(token):
    if token == "RND":
        stack.push(random.random())
    else:
        return False
    
    return True

def process_function(token, num):
    if token == "SIN":
        stack.push(math.sin(num))
    elif token == "COS":
        stack.push(math.cos(num))
    elif token == "TAN":
        stack.push(math.tan(num))
    elif token == "ABS":
        stack.push(abs(num))
    elif token == "INT":
        stack.push(int(num))
    elif token == "ATN":
        stack.push(math.atan(num))
    elif token == "COT":
        stack.push(1/math.atan(num))
    elif token == "EXP":
        stack.push(math.exp(num))
    elif token == "LOG":
        stack.push(math.log(num))               
    elif token == "SQR":
        stack.push(math.sqrt(num))
    elif token == "SGN":
        stack.push(sign(num))
    else:
        return False
    
    return True


def process_operator(token, num1, num2):
    if token == '+':
        stack.push(num1 + num2)
    elif token == '-':
        stack.push(num1 - num2)
    elif token == '*':
        stack.push(num1 * num2)
    elif token == '/':
        stack.push(num1 / num2)
    elif token == '^':
        stack.push(num1 ** num2)
    elif token == 'MOD':
        stack.push(num1 % num2)
    else:
        return False
    
    return True
    
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
                stack.push(float(token))
            elif process_no_arg_function(token):
                break
            else:
                if stack.length() < 1:
                    print("Stack to short. One argument required for", token)
                    break

                num2 = stack.pop()
                if process_function(token, num2):
                    break
                else:
                    if stack.length() < 1:
                        print("Stack to short. Two operands required for", token)
                        break

                    num1 = stack.pop()
                    if process_operator(token, num1, num2):
                        break
                    else:
                        print("Token not recognized:", token)
    return

os.system('clear')

print("+------------------------------------------+")
print("|  Internet Reverse Polish Calculator V1.0 |")
print("+------------------------------------------+")
print('\nType "quit" or "exit" to quit.\n')
print('Type "reset" to clear stack.\n')
print('Type "clear" to clear screen.\n')



stack = Stack()
print(stack.show())


# Basic loop for the program
while True:
    line = input("RPN > ")
    if line.upper() in {"QUIT", "EXIT"}:
        break
    # Process line
    process_line(stack, line)
    print(stack.show())



print("Goodbye!")