"""Collection of the core mathematical operators used throughout the code base."""

import math


# ## Task 0.1

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


def mul(x: float, y: float) -> float:
    """Multiply two numbers"""
    return x * y


def id(x: float) -> float:
    """Identity function"""
    return x


def add(x: float, y: float) -> float:
    """Add two numbers"""
    return x + y


def neg(x: float) -> float:
    """Negate a number"""
    return -x


def lt(x: float, y: float) -> bool:
    """Check if x is less than y"""
    return x < y


def eq(x: float, y: float) -> bool:
    """Check if x is equal to y"""
    return x == y


def max(x: float, y: float) -> float:
    """Return the max of two numbers"""
    return x if x > y else y


def is_close(x: float, y: float) -> bool:
    """Check if x is close to y"""
    return abs(x - y) < 1e-2


def sigmoid(x: float) -> float:
    """Sigmoid function"""
    if x >= 0:
        return 1.0 / (1.0 + exp(neg(x)))
    else:
        return exp(x) / (1.0 + exp(x))


def relu(x: float) -> float:
    """ReLU function"""
    return max(0, x)


def log(x: float) -> float:
    """Log function"""
    return math.log(x)


def exp(x: float) -> float:
    """Exponential function"""
    return math.exp(x)


def inv(x: float) -> float:
    """Inverse function"""
    return 1 / x


def log_back(x: float, z: float) -> float:
    """Log back function"""
    return 1 / x * z


def inv_back(x: float, z: float) -> float:
    """Inverse back function"""
    return -1 / (x**2) * z


def relu_back(x: float, z: float) -> float:
    """ReLU back function"""
    return 0 if x <= 0 else z


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


def negList(l: list) -> list:
    """Negate a list"""
    ...


def addLists(l1: list, l2: list) -> list:
    """Add two lists together"""
    ...


def sum(l: list) -> float:
    """Sum lists"""
    ...


def prod(l: list) -> float:
    """Take the product of lists"""
    ...
