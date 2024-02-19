#!/usr/bin/env python3
"""
This function takes a string 'k' and an integer or float 'v' as arguments
and returns a tuple containing the string 'k' and the square of 'v'.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int or float to a tuple.

    Parameters:
        k (str): The string value.
        v (Union[int, float]): The int or float value.

    Returns:
        Tuple[str, Union[int, float]]: A tuple containing the string k and
        the square of the int or float v.
        """
    return k, float(v ** 2)
