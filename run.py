
import os
import math
import random
import copy

class Stack:

    # Private member variable containing 
    # data for the stack.
    __data = []


    def __init__(self, initStack = []):
         self.__data = initStack


    def getData(self):
        return self.__data

    def length(self):
        return len(self.__data)

    def reset(self):
        self.__data.clear()

    def push(self, item):
            self.__data.append(item)

    def pop(self):
        return self.__data.pop()
   
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
    return str in {"SIN", "COS", "TAN", "ABS", "ATN", "COT", "EXP", "INT", "LOG", "SQR", "SGN", "NEG", "INV"}


def is_no_arg_function(str):
    return str in {"RND", "POP", "SWP", "PI"}

def sign(num):
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def process_no_arg_function(stack, token):
    if token == "RND":
        stack.push(random.random())
    if token == "PI":
        stack.push(math.pi)
    elif token == "POP":
        if stack.length() < 1:
            raise ArithmeticError(token+' requires at least one item in the stack.')
        stack.pop()
    elif token == "SWP":
        if stack.length() < 2:
            raise ArithmeticError(token+" requires at leaat two items in the stack.")
        num2 = stack.pop()
        num1 = stack.pop()
        stack.push(num1)
        stack.push(num2)
    else:
        return False
    
    return True

def process_function(stack, token):

    if stack.length() < 1:
        raise ArithmeticError('Function '+token+' requires one argument.')
        return
    
    num = stack.pop()
    try:
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
            if math.atan(num) == 0:
                raise ZeroDivisionError("COT is not defined for " + str(num)+".")
            stack.push(1/math.tan(num))
        elif token == "EXP":
            stack.push(math.exp(num))
        elif token == "LOG":
            if num <= 0:
                raise ValueError("LOG can't take zero or negative number.")
            stack.push(math.log(num))               
        elif token == "SQR":
            if num < 0:
                raise ValueError("SQR can't take negative number.")
            stack.push(math.sqrt(num))
        elif token == "SGN":
            stack.push(sign(num))
        elif token == "NEG":
            stack.push(-num)
        elif token == "INV":
            stack.push(1/num)
    except (ValueError, ZeroDivisionError) :
        stack.push(num)
        raise
    except OverflowError:
        stack.push(num)
        raise OverflowError("Number exceeded maximum allowed size.")
    else:
        return
        
    


def process_operator(stack, token):

    if stack.length() < 2:
        raise ArithmeticError('Operator '+token+' requires two operands.')

    num2 = stack.pop()
    num1 = stack.pop()
    try:
        if token == '+':
            stack.push(num1 + num2)
        elif token == '-':
            stack.push(num1 - num2)
        elif token == '*':
            stack.push(num1 * num2)
        elif token == '/':
            if num2 == 0:
                raise ZeroDivisionError('Operator /: tried to divide by zero.')
            stack.push(num1 / num2)
        elif token == '^':
            stack.push(num1 ** num2)
        elif token == 'MOD':
            stack.push(num1 % num2)
    except ZeroDivisionError:
        stack.push(num1)
        stack.push(num2)
        raise
    except OverflowError:
        stack.push(num1)
        stack.push(num2)
        raise OverflowError("Number exceeded maximum allowed size.")
        raise 
    else:
        return
    
def process_line(stack, line):

    line = line.upper()

    i = 0

    tokens = line.split()
    if len(tokens) == 1 and tokens[0] == "CLEAR":
        os.system('clear')
    elif len(tokens) == 1 and tokens[0] == "RESET":
        print("Stack reset to zero elements.")
        stack.reset()
    else:
        try:
            for i, token in enumerate(tokens):
                if is_num(token):
                    stack.push(float(token))
                elif is_no_arg_function(token):
                    process_no_arg_function(stack, token)
                elif is_function(token):
                    process_function(stack, token)
                elif is_operator(token):
                    process_operator(stack, token)
                else:
                    raise NameError(token + " not found.")
        except (ZeroDivisionError, ValueError, OverflowError, ArithmeticError, NameError)  as err:
            
            if i < len(tokens) - 1:
                rest_message = "Rest of input line ignored."
            else:
                rest_message = ""

            print(err, rest_message)
    
    return

os.system('clear')

print('''+------------------------------------------+"
|  Internet Reverse Polish Calculator V1.0 |")
+------------------------------------------+")
COMMANDS (to be typed on their own line):
"quit" or "exit" to quit program.  
"reset" to empty the stack.
"clear" to clear screen.''')

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