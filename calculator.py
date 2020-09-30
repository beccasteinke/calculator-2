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

    if equation[0] == "q":
        break

    #add
    if equation[0] == "+":
        result = equation[1] + equation[2]
        print(result)

    #subtract
    if equation[0] == "-":
        result = equation[1] - equation[2]
        print(result)
    #multiply
    if equation[0] == "*":
        result = equation[1] * equation[2]
        print(result)
    #divide
    if equation[0] == "/":
        result = equation[1] / equation[2]
        print(result)
    #square
    if equation[0] == "square":
        result = equation[1] ** 2
        print(result)
    #cube
    if equation[0] == "cube":
        result = equation[1] ** 3
        print(result)
    #power
    if equation[0] == "pow":
        result = equation[1] ** equation[2]
        print(result)
    #mod
    if equation[0] == "mod"
        result = equation[1] % equation[2]
        print(result)