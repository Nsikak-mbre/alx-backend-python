from typing import Iterable, Sequence, Tuple

def element_length(lst: Iterable[Sequence]) -> Iterable[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
