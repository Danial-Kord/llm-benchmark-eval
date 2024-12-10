
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



def x_generate_integers__mutmut_orig(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_1(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(3, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_2(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(None, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_3(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, None))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_4(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min( b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_5(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a,))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_6(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = None
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_7(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(9, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_8(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(None, b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_9(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, None))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_10(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max( b))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_11(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a,))

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_12(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = None

    return [i for i in range(lower, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_13(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(None, upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_14(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper-1) if i % 2 == 0]

def x_generate_integers__mutmut_15(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+2) if i % 2 == 0]

def x_generate_integers__mutmut_16(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range( upper+1) if i % 2 == 0]

def x_generate_integers__mutmut_17(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i / 2 == 0]

def x_generate_integers__mutmut_18(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 3 == 0]

def x_generate_integers__mutmut_19(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 != 0]

def x_generate_integers__mutmut_20(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    lower = max(2, min(a, b))
    upper = min(8, max(a, b))

    return [i for i in range(lower, upper+1) if i % 2 == 1]

x_generate_integers__mutmut_mutants = {
'x_generate_integers__mutmut_1': x_generate_integers__mutmut_1, 
    'x_generate_integers__mutmut_2': x_generate_integers__mutmut_2, 
    'x_generate_integers__mutmut_3': x_generate_integers__mutmut_3, 
    'x_generate_integers__mutmut_4': x_generate_integers__mutmut_4, 
    'x_generate_integers__mutmut_5': x_generate_integers__mutmut_5, 
    'x_generate_integers__mutmut_6': x_generate_integers__mutmut_6, 
    'x_generate_integers__mutmut_7': x_generate_integers__mutmut_7, 
    'x_generate_integers__mutmut_8': x_generate_integers__mutmut_8, 
    'x_generate_integers__mutmut_9': x_generate_integers__mutmut_9, 
    'x_generate_integers__mutmut_10': x_generate_integers__mutmut_10, 
    'x_generate_integers__mutmut_11': x_generate_integers__mutmut_11, 
    'x_generate_integers__mutmut_12': x_generate_integers__mutmut_12, 
    'x_generate_integers__mutmut_13': x_generate_integers__mutmut_13, 
    'x_generate_integers__mutmut_14': x_generate_integers__mutmut_14, 
    'x_generate_integers__mutmut_15': x_generate_integers__mutmut_15, 
    'x_generate_integers__mutmut_16': x_generate_integers__mutmut_16, 
    'x_generate_integers__mutmut_17': x_generate_integers__mutmut_17, 
    'x_generate_integers__mutmut_18': x_generate_integers__mutmut_18, 
    'x_generate_integers__mutmut_19': x_generate_integers__mutmut_19, 
    'x_generate_integers__mutmut_20': x_generate_integers__mutmut_20
}

def generate_integers(*args, **kwargs):
    result = _mutmut_trampoline(x_generate_integers__mutmut_orig, x_generate_integers__mutmut_mutants, *args, **kwargs)
    return result 

generate_integers.__signature__ = _mutmut_signature(x_generate_integers__mutmut_orig)
x_generate_integers__mutmut_orig.__name__ = 'x_generate_integers'


