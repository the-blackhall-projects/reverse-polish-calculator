
import os
import math
import random


class Stack:
    """
    Implement a stack object using a list as the data.
    """
    __data = []

    def __init__(self, init_stack = []):
         """
         Constructor.  Create the object.

         Parameters
         ----------
         init_stack : list. Optional
            Alist supplied to constitute
            initial stack.  Defaults to the empty list
         """
         self.__data = init_stack
    
    def length(self):
        """
        Get length of stack.

        Returns
        -------
        int : the number of items in the stack.
        """

        return len(self.__data)

    def reset(self):
        """
            Clear the list of all items.
        """
        self.__data.clear()

    def push(self, item):
        """
        Pushes an item ont the stack.

        Parameters
        ----------
        item: float
            The item to be pushed onto the stack.

        """
        self.__data.append(item)

    def pop(self):
        """
        Pup an item from the stack.

        Returns
        -------
        float: the item popped from the stack.
        """
        return self.__data.pop()
   
    def show(self):
        """
        Return a string representing the stack for use
        in the program output.  Prefix output with "Stack:"
        and have "(empty)" if stack is empty.

        Returns
        -------
            string : a printable representation of the stack.

        """
        ret_val = ""
        for num in self.__data:
            if num == int(num):
                ret_val += " " + str(int(num))
            else:
                ret_val += " " + str(num)

        retVal = ret_val.strip()

        if len(ret_val) == 0:
            ret_val = "(empty)"

        return "Stack: " + ret_val


def is_num(strng):
    """
    Test if string passed represents a valid number.

    Parameters
    ----------
    strng : string
        The string containing the number to be tested.

    Returns
    -------
        boolean : True if the passed string represents 
        a valid number.
    """
    ret_val = True
    
    try:
        float(strng)
    except ValueError:
        ret_val = False

    return ret_val

def is_operator(strng):
    """
    Test if passed string represents an arithmetic operator.

    Parameters
    ----------
    strng : string
        String to be tested

    Returns
    -------
    boolean : True if string represents a valid operator

    """
    return strng in {'+', '-', '*', '/', '^', 'MOD'}

def is_function(strng):
    """
    Test if passed string represents a function

    Parameters
    ----------
    strng : string
        String to be tested

    Returns
    -------
    boolean : True if string represents a valid function
    """
    return strng in {"SIN", "COS", "TAN", "ABS", "ATN", "COT", "EXP", "INT", "LOG", "SQR", "SGN", "NEG", "INV"}


def is_no_arg_function(strng):
    """
    Test if passed string represents a function that takes no argument

    Parameters
    ----------
    strng : string
        String to be tested

    Returns
    -------
    boolean : True if string represents a valid function that takes no argument
    """
    return strng in {"RND", "POP", "SWP", "PI"}

def sign(num):
    """
    Return the sign of a number

    Parameters
    ----------
    float : num
    The number who's sign is to be determined

    Returns
    -------
    float : the sign of the number.  -1 if negative,
        1 if positive and 0 if zero.
    
    """
    if num < 0:
        return -1
    elif num > 0:
        return 1
    else:
        return 0

def process_no_arg_function(stack, token):
    """
    Process no argument function. Push the calculated value
    onto the stack or carry out required operation.

    Parameters
    ----------
    stack : object
    The stack on which to perform operation

    token : string
    A string representing the function.

    Note
    ----
    Some of these operations require some elements in the stack,
    however these elements are not used as arguments to the functions.
    """
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
        stack.push(num2)
        stack.push(num1)
    return

def process_function(stack, token):
    """
    Process standard function and push the calculated value
    onto the stack.

    Parameters
    ----------
    stack : object
    The stack on which to perform operation

    token : string
    A string representing the function
    """
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
        elif token == "COT": # Cotangent
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
    except OverflowError as err:
        stack.push(num)
        raise OverflowError("Number exceeded maximum allowed size.") from err
    
    return

def process_operator(stack, token):
    """
    Process the suppied operator and push the calculated value
    onto the stack.

    Parameters
    ----------
    stack : object
    The stack on which to perform operation

    token : string
    A string representing the operator
    """
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
         
    return
    
def process_line(stack, line):
    """
    Process a line entered by the user.

    Parameters
    ----------
    stack : object
    The stack on which to perform operation

    line : string
    A string entered by the user.
    """
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





def main():
    """
    Main loop of the program.  Set up stack.  Read line from user.
    Process line.  Display new stack as output.
    """
    os.system('clear')

    print('''+-------------------------------------------+"
|  Internet Reverse Polish Calculator V 1.0 |"
+-------------------------------------------+"

COMMANDS (to be typed on their own line):

"quit" or "exit" to quit program.  
"reset" to empty the stack.
"clear" to clear screen.
''')

    stack = Stack()
    print(stack.show())


    # Basic loop for the program
    while True:
        line = input("RPN > ")
        if line.upper() in {"QUIT", "EXIT"}:
            break
        # Process line
        process_line(stack, line)
        # Display the stack
        print(stack.show())

    print("Goodbye!")

if __name__ == "__main__":
    main()