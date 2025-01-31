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


def mul(a: float, b: float) -> float:
    """Multiplies two numbers

    Args:
    ----
        a (float): a number
        b (float): another number

    Returns:
    -------
        float: the product of the two numbers

    """
    return a * b


def id(a: float) -> float:
    """_summary_

    Args:
    ----
        a (float): _description_

    Returns:
    -------
        float: _description_

    """
    return a


def add(a: float, b: float) -> float:
    """_summary_

    Args:
    ----
        a (float): _description_
        b (float): _description_

    Returns:
    -------
        float: _description_

    """
    return a + b


def neg(a: float) -> float:
    """_summary_

    Args:
    ----
        a (float): _description_

    Returns:
    -------
        float: _description_

    """
    return -a


def lt(a: float, b: float) -> bool:
    """A < b

    Args:
    ----
        a (float): _description_
        b (float): _description_

    Returns:
    -------
        bool: _description_

    """
    return a < b


def eq(a: float, b: float) -> bool:
    """A == b

    Args:
    ----
        a (float): _description_
        b (float): _description_

    Returns:
    -------
        bool: _description_

    """
    return a == b


def max(a: float, b: float) -> float:
    """_summary_

    Args:
    ----
        a (float): _description_
        b (float): _description_

    Returns:
    -------
        float: _description_

    """
    return a if lt(b, a) else b


def is_close(a: float, b: float, tol: float = 1e-2) -> float:
    """$f(x) = |x - y| < 1e-2$

    Args:
    ----
        a (float): _description_
        b (float): _description_
        tol (float, optional): _description_. Defaults to 1e-4.

    Returns:
    -------
        float: _description_

    """
    return abs(a - b) < tol


def sigmoid(x: float) -> float:
    r"""$f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$

    Args:
    ----
        x (float): _description_

    Returns:
    -------
        float: _description_

    """
    return 1 / (1 + exp(-x)) if x >= 0 else exp(x) / (1 + exp(x))


def relu(x: float) -> float:
    """_summary_

    Args:
    ----
        x (float): _description_

    Returns:
    -------
        float: _description_

    """
    return x if x >= 0 else 0


def log(x: float) -> float:
    """_summary_

    Args:
    ----
        x (float): _description_

    Returns:
    -------
        float: _description_

    """
    return math.log(x)


def exp(x: float) -> float:
    """_summary_

    Args:
    ----
        x (float): _description_

    Returns:
    -------
        float: _description_

    """
    return math.e**x


def inv(x: float) -> float:
    """Calculates the reciprocal

    Args:
    ----
        x (float): _description_

    Returns:
    -------
        float: _description_

    """
    return 1 / x


def log_back(x: float, y: float) -> float:
    """Computes the derivative of log times a second arg

    Args:
    ----
        x (float): _description_
        y (float): _description_

    Returns:
    -------
        float: _description_

    """
    return 1 / x * y


def inv_back(x: float, y: float) -> float:
    """Computes the derivative of reciprocal times a second arg

    Args:
    ----
        x (float): _description_
        y (float): _description_

    Returns:
    -------
        float: _description_

    """
    return -1 / x**2 * y


def relu_back(x: float, y: float) -> float:
    """Computes the derivative of ReLU times a second arg

    Args:
    ----
        x (float): _description_
        y (float): _description_

    Returns:
    -------
        float: _description_

    """
    return y if x >= 0 else 0


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
    """Higher-order function that applies a given function to each element of an iterable

    Args:
    ----
        fn (Callable[[float], float]): _description_

    Returns:
    -------
        Callable[[Iterable[float]], Iterable[float]]: _description_

    """

    def apply(ls: Iterable[float]) -> Iterable[float]:
        return [fn(x) for x in ls]

    return apply


def zipWith(
    fn: Callable[[float, float], float],
) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """Higher-order function that combines elements from two iterables using a given function

    Args:
    ----
        fn (Callable[[float,float], float]): _description_

    Returns:
    -------
        Callable[[Iterable[float], Iterable[float]], Iterable[float]]: _description_

    """

    def apply(l1: Iterable[float], l2: Iterable[float]) -> Iterable[float]:
        return [fn(el1, l2[idx]) for idx, el1 in enumerate(l1)]

    return apply


def reduce(fn: Callable[[float, float], float]) -> Callable[[Iterable[float]], float]:
    """Higher-order function that reduces an iterable to a single value using a given function

    Args:
    ----
        fn (Callable[[float], float]): _description_

    Returns:
    -------
        Callable[[Iterable[float]], float]: _description_

    """

    def apply(ls: Iterable[float]) -> float:
        if not ls:
            return 0  # a bit adhoc IMO
        res = ls[0]
        for el in ls[1:]:
            res = fn(res, el)
        return res

    return apply


def negList(ls: Iterable[float]) -> Iterable[float]:
    """Negate all elements in a list using map

    Args:
    ----
        ls (Iterable[float]): _description_

    Returns:
    -------
        Iterable[float]: _description_

    """
    return map(neg)(ls)


def addLists(ls1: Iterable[float], ls2: Iterable[float]) -> Iterable[float]:
    """Add corresponding elements from two lists using zipWith

    Args:
    ----
        ls1 (Iterable[float]): _description_
        ls2 (Iterable[float]): _description_

    Returns:
    -------
        Iterable[float]: _description_

    """
    return zipWith(add)(ls1, ls2)


def sum(ls: Iterable[float]) -> float:
    """Sum all elements in a list using reduce

    Args:
    ----
        ls (Iterable[float]): _description_

    Returns:
    -------
        float: _description_

    """
    return reduce(add)(ls)


def prod(ls: Iterable[float]) -> float:
    """Calculate the product of all elements in a list using reduce

    Args:
    ----
        ls (Iterable[float]): _description_

    Returns:
    -------
        float: _description_

    """
    return reduce(mul)(ls)
