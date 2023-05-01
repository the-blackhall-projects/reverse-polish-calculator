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

More recently, FORTH, a stack based language developed in 1970, uses RPN for arithmetic and Hewlett-Packard, to this day, allows the use of RPN in its calculators.  



## Using the program

When you start up the program you are presented with the following information:

``` 
+-------------------------------------------+
|  Internet Reverse Polish Calculator V 1.0 |
+-------------------------------------------+

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

**Commands** have already been discussed.  They are not part of RPN and therefore must be typed on their own line. 

**Numbers** can be positive or negative and can be entered in scientific notation.  When a number is encountered in the input line it is added to the stack. 
```
Stack: (empty)
RPN > 1 -1.2 3e-3
Stack: 1 -1.2 0.003
RPN > 
```
In the example above, starting from an empty stack, the numbers 1, -1.2 and 3e-3 are entered after the prompt.  The program then displays the stack and a new
prompt is printed on the following line.

**Operators** consist of the standard arithemtic binary operators.  Unlike conventional notation, operators appear after their operands in the command line.  When an operator is encountered, two numbers are popped from the stack.  The operation is peformed upon them, and the result then pushed to the stack.

Below is a table of available operators.

| Operator      | Description |
| ----------- | ----------- |
| +      | Addition       |
| -   | Subtraction        |
| \*   | Multipliacation   |
|\\   | Division        |
|^   | Exponentiation     |
|MOD   | Modulus     |

All of these require at least two numbers on the stack upon which to operate.

Example:

To compute 6 × (5 + 4) we would type: 5 4 + 6 *.

```
Stack: (empty)
RPN > 5 4 + 6 *
Stack: 54
RPN > 
```
And we see the answer is 54.

**Functions** come in several types. 
- Trigonometric
- Log and Exponential
- Stack manipulation
- Other functions

Most functions take one argument.  When a single argument is encountered
in the input line, a number is popped off the stack, the function is 
evaluated and the result pushed back onto the stack.

| Trigonometric      | Description |
| ----------- | ----------- |
| SIN      | Sine       |
| COS   | Cosine        |
| TAN   | Tangent   |
| ATN   | Arctangent        |
| COT   | Cotangent        |

| Log and Exponential      | Description |
| ----------- | ----------- |
| LOG      | Natural logarithm       |
| EXP   | Exponent to base e        |

| Stack manipulation      | Description |
| ----------- | ----------- |
| DUP      | Duplicate top item |
| DROP   | Drop top item       |
| SWP   | Swap top two items       |

| Other functions      | Description |
| ----------- | ----------- |
| SQR   | Square root   |
| ABS   | Absolute value   |
| INT      | Integer portion of num |
| SGN   | Sign of a number 1, -1 or 0 |
| NEG   | Negate: multiply by -1   |
| INV   | Invert: 1 / num   |

As an example, consider $\sin($\pi$ / 2)$





