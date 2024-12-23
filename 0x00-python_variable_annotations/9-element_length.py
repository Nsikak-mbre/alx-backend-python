#!/usr/bin/env python3
"""Type-annotated function element_length that takes a list of strings"""
from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    """Type-annotated function element_length that takes a list of strings"""
    return [(i, len(i)) for i in lst]
