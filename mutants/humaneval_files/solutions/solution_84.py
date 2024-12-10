
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



def x_starts_one_ends__mutmut_orig(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n - 2))

def x_starts_one_ends__mutmut_1(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n != 1: return 1
    return 18 * (10 ** (n - 2))

def x_starts_one_ends__mutmut_2(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 2: return 1
    return 18 * (10 ** (n - 2))

def x_starts_one_ends__mutmut_3(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 2
    return 18 * (10 ** (n - 2))

def x_starts_one_ends__mutmut_4(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 19 * (10 ** (n - 2))

def x_starts_one_ends__mutmut_5(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 / (10 ** (n - 2))

def x_starts_one_ends__mutmut_6(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (11 ** (n - 2))

def x_starts_one_ends__mutmut_7(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 * (n - 2))

def x_starts_one_ends__mutmut_8(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n + 2))

def x_starts_one_ends__mutmut_9(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n == 1: return 1
    return 18 * (10 ** (n - 3))

x_starts_one_ends__mutmut_mutants = {
'x_starts_one_ends__mutmut_1': x_starts_one_ends__mutmut_1, 
    'x_starts_one_ends__mutmut_2': x_starts_one_ends__mutmut_2, 
    'x_starts_one_ends__mutmut_3': x_starts_one_ends__mutmut_3, 
    'x_starts_one_ends__mutmut_4': x_starts_one_ends__mutmut_4, 
    'x_starts_one_ends__mutmut_5': x_starts_one_ends__mutmut_5, 
    'x_starts_one_ends__mutmut_6': x_starts_one_ends__mutmut_6, 
    'x_starts_one_ends__mutmut_7': x_starts_one_ends__mutmut_7, 
    'x_starts_one_ends__mutmut_8': x_starts_one_ends__mutmut_8, 
    'x_starts_one_ends__mutmut_9': x_starts_one_ends__mutmut_9
}

def starts_one_ends(*args, **kwargs):
    result = _mutmut_trampoline(x_starts_one_ends__mutmut_orig, x_starts_one_ends__mutmut_mutants, *args, **kwargs)
    return result 

starts_one_ends.__signature__ = _mutmut_signature(x_starts_one_ends__mutmut_orig)
x_starts_one_ends__mutmut_orig.__name__ = 'x_starts_one_ends'


