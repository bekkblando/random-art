import random
import math as m
import numpy as np
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    i = random.random()
    w = random.randint(1, 30)
    s = random.randint(1, 5)
    choice = random.randint(1, 3)

    def expr(x, y):
        for item in range(3):
            x = x * i
            y = y * i
            x += m.factorial(s)

            op1 = (lambda x, y: x*i*y/m.sin(299792458)/3.14345353)(y, x)
            op2 = (lambda x, y: (x*w/3.14) % s + i)(x, y)
            op3 = (lambda x, y: (m.cos(y**2) * m.gamma(x)))(x, y)
            if choice == 1:
                op = op1
                ops = op2
            if choice == 2:
                op = op2
                ops = op3
            if choice == 3:
                op = op3
                ops = op1
            u = (lambda x, y: (x*2) * (y*2))(op, ops)
            ans = u
        return ans

    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
