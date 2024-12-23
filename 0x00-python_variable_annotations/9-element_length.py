from typing import List, Tuple, Sequence

def element_length(lst: Sequence[str]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
