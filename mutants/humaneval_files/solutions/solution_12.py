
from inspect import signature as _mutmut_signature

def _mutmut_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = mutants[mutant_name](*args, **kwargs)
    return result


from inspect import signature as _mutmut_signature

def _mutmut_yield_from_trampoline(orig, mutants, *args, **kwargs):
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = yield from orig(*args, **kwargs)
        return result  # for the yield case
    mutant_name = mutant_under_test.rpartition('.')[-1]
    result = yield from mutants[mutant_name](*args, **kwargs)
    return result


from typing import List


def x_string_xor__mutmut_orig(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


def x_string_xor__mutmut_1(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i != j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


def x_string_xor__mutmut_2(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return 'XX0XX'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, b))


def x_string_xor__mutmut_3(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return 'XX1XX'

    return ''.join(xor(x, y) for x, y in zip(a, b))


def x_string_xor__mutmut_4(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return 'XXXX'.join(xor(x, y) for x, y in zip(a, b))


def x_string_xor__mutmut_5(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(None, y) for x, y in zip(a, b))


def x_string_xor__mutmut_6(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, None) for x, y in zip(a, b))


def x_string_xor__mutmut_7(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor( y) for x, y in zip(a, b))


def x_string_xor__mutmut_8(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x,) for x, y in zip(a, b))


def x_string_xor__mutmut_9(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(None, b))


def x_string_xor__mutmut_10(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a, None))


def x_string_xor__mutmut_11(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip( b))


def x_string_xor__mutmut_12(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    def xor(i, j):
        if i == j:
            return '0'
        else:
            return '1'

    return ''.join(xor(x, y) for x, y in zip(a,))

x_string_xor__mutmut_mutants = {
'x_string_xor__mutmut_1': x_string_xor__mutmut_1, 
    'x_string_xor__mutmut_2': x_string_xor__mutmut_2, 
    'x_string_xor__mutmut_3': x_string_xor__mutmut_3, 
    'x_string_xor__mutmut_4': x_string_xor__mutmut_4, 
    'x_string_xor__mutmut_5': x_string_xor__mutmut_5, 
    'x_string_xor__mutmut_6': x_string_xor__mutmut_6, 
    'x_string_xor__mutmut_7': x_string_xor__mutmut_7, 
    'x_string_xor__mutmut_8': x_string_xor__mutmut_8, 
    'x_string_xor__mutmut_9': x_string_xor__mutmut_9, 
    'x_string_xor__mutmut_10': x_string_xor__mutmut_10, 
    'x_string_xor__mutmut_11': x_string_xor__mutmut_11, 
    'x_string_xor__mutmut_12': x_string_xor__mutmut_12
}

def string_xor(*args, **kwargs):
    result = _mutmut_trampoline(x_string_xor__mutmut_orig, x_string_xor__mutmut_mutants, *args, **kwargs)
    return result 

string_xor.__signature__ = _mutmut_signature(x_string_xor__mutmut_orig)
x_string_xor__mutmut_orig.__name__ = 'x_string_xor'


