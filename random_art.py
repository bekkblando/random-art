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
        for item in range(1):
            x = x * i
            # x = x/w
            y = y * i
            x += m.factorial(s)

            op1 = (lambda x, y: x*i*y)(y, x)
            op2 = (lambda x, y: (x*w)%s + i)(x, y)
            op3 = (lambda x, y: ((m.acos(y**2) *m.gamma(x))))(x, y)
            if choice == 1:
                op = op1
                ops = op2
            if choice == 2:
                op = op2
                ops = op3
            if choice == 3:
                op = op3
                ops = op1
            # print(len(range((lambda x, y: (x**4) * (y**2))(random.choice(choices), random.choice(choices)))))
            u = (lambda x, y: (x*2) * (y*2))(op, ops)
            ans = u
        return ans

        # return x * (1/m.sqrt(1 - ((y)/299792458**2)))
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)
