#!/usr/bin/env python3
"""
Defining a function to sum elements of a mixed list of integers and floats
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
