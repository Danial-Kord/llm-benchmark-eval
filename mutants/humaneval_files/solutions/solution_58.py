
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




def x_monotonic__mutmut_orig(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


def x_monotonic__mutmut_1(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l != sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


def x_monotonic__mutmut_2(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(None) or l == sorted(l, reverse=True):
        return True
    return False


def x_monotonic__mutmut_3(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l != sorted(l, reverse=True):
        return True
    return False


def x_monotonic__mutmut_4(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(None, reverse=True):
        return True
    return False


def x_monotonic__mutmut_5(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=False):
        return True
    return False


def x_monotonic__mutmut_6(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted( reverse=True):
        return True
    return False


def x_monotonic__mutmut_7(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l,):
        return True
    return False


def x_monotonic__mutmut_8(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) and l == sorted(l, reverse=True):
        return True
    return False


def x_monotonic__mutmut_9(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return False
    return False


def x_monotonic__mutmut_10(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return True

x_monotonic__mutmut_mutants = {
'x_monotonic__mutmut_1': x_monotonic__mutmut_1, 
    'x_monotonic__mutmut_2': x_monotonic__mutmut_2, 
    'x_monotonic__mutmut_3': x_monotonic__mutmut_3, 
    'x_monotonic__mutmut_4': x_monotonic__mutmut_4, 
    'x_monotonic__mutmut_5': x_monotonic__mutmut_5, 
    'x_monotonic__mutmut_6': x_monotonic__mutmut_6, 
    'x_monotonic__mutmut_7': x_monotonic__mutmut_7, 
    'x_monotonic__mutmut_8': x_monotonic__mutmut_8, 
    'x_monotonic__mutmut_9': x_monotonic__mutmut_9, 
    'x_monotonic__mutmut_10': x_monotonic__mutmut_10
}

def monotonic(*args, **kwargs):
    result = _mutmut_trampoline(x_monotonic__mutmut_orig, x_monotonic__mutmut_mutants, *args, **kwargs)
    return result 

monotonic.__signature__ = _mutmut_signature(x_monotonic__mutmut_orig)
x_monotonic__mutmut_orig.__name__ = 'x_monotonic'


