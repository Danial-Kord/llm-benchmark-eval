
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



def x_special_factorial__mutmut_orig(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_1(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 2
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_2(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = None
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_3(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 2
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_4(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = None
    for i in range(1, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_5(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(2, n+1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_6(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n-1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_7(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+2):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_8(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i /= i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_9(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i = i
        special_fact *= fact_i
    return special_fact

def x_special_factorial__mutmut_10(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact /= fact_i
    return special_fact

def x_special_factorial__mutmut_11(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n+1):
        fact_i *= i
        special_fact = fact_i
    return special_fact

x_special_factorial__mutmut_mutants = {
'x_special_factorial__mutmut_1': x_special_factorial__mutmut_1, 
    'x_special_factorial__mutmut_2': x_special_factorial__mutmut_2, 
    'x_special_factorial__mutmut_3': x_special_factorial__mutmut_3, 
    'x_special_factorial__mutmut_4': x_special_factorial__mutmut_4, 
    'x_special_factorial__mutmut_5': x_special_factorial__mutmut_5, 
    'x_special_factorial__mutmut_6': x_special_factorial__mutmut_6, 
    'x_special_factorial__mutmut_7': x_special_factorial__mutmut_7, 
    'x_special_factorial__mutmut_8': x_special_factorial__mutmut_8, 
    'x_special_factorial__mutmut_9': x_special_factorial__mutmut_9, 
    'x_special_factorial__mutmut_10': x_special_factorial__mutmut_10, 
    'x_special_factorial__mutmut_11': x_special_factorial__mutmut_11
}

def special_factorial(*args, **kwargs):
    result = _mutmut_trampoline(x_special_factorial__mutmut_orig, x_special_factorial__mutmut_mutants, *args, **kwargs)
    return result 

special_factorial.__signature__ = _mutmut_signature(x_special_factorial__mutmut_orig)
x_special_factorial__mutmut_orig.__name__ = 'x_special_factorial'


