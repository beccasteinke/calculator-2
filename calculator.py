"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#ask for input; use input to split into a list
#input: + 1 2 -> ["+", "3", "2"]
# + equation[0] 3 equation [1]
while True:
    input_string = input("Enter your equation > ")
    equation = input_string.split(' ')

    if len(equation) < 3:
        num2 = "0"
    elif len(equation) >3:
        num2 = equation[2]

    if equation[0] == "q":
        break

    #add
    if equation[0] == "+":
        result = int(equation[1]) + int(equation[2])

    #subtract
    if equation[0] == "-":
        result = int(equation[1]) - int(equation[2])

    #multiply
    if equation[0] == "*":
        result = int(equation[1]) * int(equation[2])

    #divide
    if equation[0] == "/":
        result = int(equation[1]) / int(equation[2])

    #square
    if equation[0] == "square":
        result = int(num1) ** 2

    #cube
    if equation[0] == "cube":
        result = int(equation[1]) ** 3

    #power
    if equation[0] == "pow":
        result = int(equation[1]) ** int(equation[2])
    
    #mod
    if equation[0] == "mod":
        result = int(equation[1]) % int(equation[2])
   
    print(result)