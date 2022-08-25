#!/usr/bin/python3
from sys import argv, exit
import calculator_1
if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a, op, b = argv[1:]
    a = int(a)
    b = int(b)
    if op == '+':
        print("{a} + {b} = {calculator_1.add(a, b)}")
    elif op == '-':
        print("{a} - {b} = {calculator_1.sub(a, b)}")
    elif op == '*':
        print("{a} * {b} = {calculator_1.mul(a, b)}")
    elif op == '/':
        print("{a} / {b} = {calculator_1.div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
