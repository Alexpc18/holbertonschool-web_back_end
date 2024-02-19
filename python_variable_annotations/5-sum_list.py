#!/usr/bin/env python3
"""
This script defines a type-annotated function 'sum_list'
that takes an 'imput_list' list of floats as arguments and
returns a sum as a float
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Parameters:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list)
