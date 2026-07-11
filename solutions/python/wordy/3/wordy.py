"""Translate natural language math queries into executable arithmetic operations.

Parse text-based mathematical questions, map them to Python operators,
and compute the resulting integer values while enforcing syntax validation.
"""
import operator
from typing import Dict, List, Callable


Operation = Callable[[int, int], int]

TRANSLATIONS: Dict[str, Operation] = {
    "plus": operator.add,
    "minus": operator.sub,
    "multiply_by": operator.mul,
    "divide_by": operator.floordiv,
}


def _parse_text(question: str) -> List[str]:
    """Parse and tokenize the natural language question.
    """
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    content = (
        question.removeprefix("What is ")
        .removesuffix("?")
        .replace("multiplied by", "multiply_by")
        .replace("divided by", "divide_by")
    )
    
    cache = content.split()    
    try:
        int(cache[0])
    except ValueError as exc:
        raise ValueError("syntax error") from exc
        
    return cache
    

def answer(question: str) -> int:
    """Calculate the result of a mathematical question."""
    parts = _parse_text(question)
    result = int(parts[0])

    for index in range(1, len(parts)):
        if index % 2 == 0:
            try:
                number = int(parts[index])
                op_func = TRANSLATIONS[parts[index - 1]]
                result = op_func(result, number)
            except ValueError as exc:
                raise ValueError("syntax error") from exc

        else:
            try:
                op_word = parts[index]
                _ = TRANSLATIONS[op_word]
                if index == len(parts) - 1:
                    raise ValueError("syntax error")
            except KeyError as exc:
                if op_word.lstrip("-").isdecimal():
                    raise ValueError("syntax error") from exc
                raise ValueError("unknown operation") from exc

    return result
