#!/usr/bin/env python3
"""sum_mixed_list module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the list of floats and integers"""
    return sum(mxd_lst)
