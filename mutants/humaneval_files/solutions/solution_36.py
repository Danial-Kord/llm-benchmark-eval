
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




def x_max_element__mutmut_orig(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = e
    return m


def x_max_element__mutmut_1(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[1]
    for e in l:
        if e > m:
            m = e
    return m


def x_max_element__mutmut_2(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[None]
    for e in l:
        if e > m:
            m = e
    return m


def x_max_element__mutmut_3(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = None
    for e in l:
        if e > m:
            m = e
    return m


def x_max_element__mutmut_4(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e >= m:
            m = e
    return m


def x_max_element__mutmut_5(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    m = l[0]
    for e in l:
        if e > m:
            m = None
    return m

x_max_element__mutmut_mutants = {
'x_max_element__mutmut_1': x_max_element__mutmut_1, 
    'x_max_element__mutmut_2': x_max_element__mutmut_2, 
    'x_max_element__mutmut_3': x_max_element__mutmut_3, 
    'x_max_element__mutmut_4': x_max_element__mutmut_4, 
    'x_max_element__mutmut_5': x_max_element__mutmut_5
}

def max_element(*args, **kwargs):
    result = _mutmut_trampoline(x_max_element__mutmut_orig, x_max_element__mutmut_mutants, *args, **kwargs)
    return result 

max_element.__signature__ = _mutmut_signature(x_max_element__mutmut_orig)
x_max_element__mutmut_orig.__name__ = 'x_max_element'


