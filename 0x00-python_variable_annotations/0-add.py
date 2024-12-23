#!/usr/bin/env python3

""" Type annotation """

def add(a: float, b: float) -> float:
    """
    Add two floats and return the result.

    Args:
        a (float): The first float to add.
        b (float): The second float to add.

    Returns:
        float: The sum of the two floats.
    """
    result = float(a) + float(b)
    return result
