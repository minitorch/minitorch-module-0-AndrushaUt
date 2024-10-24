"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


def is_close(num1: float, num2: float) -> bool:
    return abs(num1 - num2) < 1e-2 


def mul(num1: float, num2: float) -> float:
    return num1 * num2


def max(num1: float, num2: float) -> float:
    return num1 if num1 > num2 else num2


def add(num1: float, num2: float) -> float:
    return num1 + num2


def neg(num1: float) -> float:
    return -num1


def id(num: float) -> float:
    return num


def inv(num: float) -> float:
    return 1.0 / num


def relu(num: float) -> float:
    return num if num > 0 else 0.0


def relu_back(num1: float, num2: float) -> float:
    return num2 if num1 > 0 else 0.0


def lt(num1: float, num2: float) -> float:
    return float(num1 < num2)


def eq(num1: float, num2: float) -> float:
    return float(num1 == num2)
# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
