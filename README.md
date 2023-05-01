# Online Reverse Polish Notation (RPN) Calculator

Live site: https://reverse-polish-calculator.herokuapp.com/

Github repository:
https://github.com/the-blackhall-projects/reverse-polish-calculator

PyDoc Documentation:
https://the-blackhall-projects.github.io/reverse-polish-calculator/



## What is Reverse Polish Notation?

This program implements a Reverse Rolish Notation (RPN) calculator.  Reverse Polish is an alternative to the more common infix notation involving parentheses. Wheras with normal infix notation, the operator is placed between the operands, with RPN the operator comes after the operands.  As such, it is an example of postfix notation.

So, for example, instead of writing:

(2 + 4) * 5 

in normal infix notation, in RPN we would write:

2 4 + 5 *

In this example, 2 and 4 are pushed onto the stack.  The '+' operator
is invoked replacing the 2 and 4 with the sum 6.  Then a 5 is pushed onto
the stack and the multiplaction operator '*' is invoked giving the final result of 30.  

RPN has a long history and is a variant of Polish Notation (PN) which was invented by the Polish logician, Jan Łukasiewicz to express mathematical logic without parentheses.  While PN puts the operator in front of the operands, RPN puts the operator after and hence is a postfix notation.

RPN was used in some early digital computers such as Konrad Zuse's Z3, English Electric's KDF9 and the Burroughs B5000.  The early computer language GEORGE used RPN to express arithmetic and ran on English Electric's DEUCE machine.

Another more recent programming language to use RPN is FORTH, a stack based language developed in 1970. 



## Using the program

When you start up the program you are presented with the following information:

``` 
+-------------------------------------------+"
|  Internet Reverse Polish Calculator V 1.0 |"
+-------------------------------------------+"

COMMANDS (to be typed on their own line):

"quit" or "exit" to quit program.
"reset" to empty the stack.
"clear" to clear screen.

Stack: (empty)
RPN > 
```
After the main banner we have a list of commands which must be entered alone
on their own line to work.  The result of these commands should be obvious from the opening text.

Following this we have a display of the data stack.  As we can see, upon starting the program, the stack is empty.
Finallly, on the next line, we have the "RPN >" prompt after which the user 
can type expressions in Reverse Polish Notation (RPN).

RPN is a sequences of tokens separated by spaces.  The tokens can be of three
types:

1. Commands
1. Numbers
1. Operators
1. Functions

**Commands** have already been discussed and are not part of RPN. 

**Numbers** can be positive or negative and can be entered in scientific notation.  When a number is encountered in the input line it is added to the stack. 
```
Stack: (empty)
RPN > 1 -1.2 3e-3
Stack: 1 -1.2 0.003
RPN > 
```
In the example above, starting from an empty stack, the numbers 1, -1.2 and 3e-3 are entered after the prompt.  The program then displays the stack and a new
prompt is printed on the following line.



