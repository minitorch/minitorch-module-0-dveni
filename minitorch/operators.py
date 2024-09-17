"""Collection of the core mathematical operators used throughout the code base."""

import math
from typing import Callable, Iterable


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


def lte(x: float, y: float) -> bool:
    """Check if x is less or equal than y"""
    return x <= y


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


def map(fn: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """Map a function over a list"""

    def apply(ls: Iterable[float]) -> Iterable[float]:
        return [fn(el) for el in ls]

    return apply


def reduce(fn: Callable[[float, float], float]) -> Callable[[Iterable[float]], float]:
    """Reduce a list with a function"""

    def apply(ls: Iterable[float]) -> float:
        if not ls:
            return 0
        ls = iter(ls)
        value = next(ls)
        for el in ls:
            value = fn(value, el)
        return value

    return apply


def zipWith(
    fn: Callable[[float, float], float],
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """Zip two lists with a function"""

    def apply(l1: Iterable[float], l2: Iterable[float]) -> Iterable[float]:
        return [fn(x, y) for x, y in zip(l1, l2)]

    return apply


def negList(l: list) -> Iterable[float]:
    """Negate a list"""
    return map(neg)(l)


def addLists(l1: list, l2: list) -> Iterable[float]:
    """Add two lists together"""
    return zipWith(add)(l1, l2)


def sum(l: Iterable[float]) -> float:
    """Sum lists"""
    return reduce(add)(l)


def prod(l: list) -> float:
    """Take the product of lists"""
    return reduce(mul)(l)
