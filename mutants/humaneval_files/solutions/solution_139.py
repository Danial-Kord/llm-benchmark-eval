
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



def x_is_equal_to_sum_even__mutmut_orig(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 8

def x_is_equal_to_sum_even__mutmut_1(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n/2 == 0 and n >= 8

def x_is_equal_to_sum_even__mutmut_2(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%3 == 0 and n >= 8

def x_is_equal_to_sum_even__mutmut_3(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 != 0 and n >= 8

def x_is_equal_to_sum_even__mutmut_4(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 1 and n >= 8

def x_is_equal_to_sum_even__mutmut_5(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n > 8

def x_is_equal_to_sum_even__mutmut_6(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 and n >= 9

def x_is_equal_to_sum_even__mutmut_7(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n%2 == 0 or n >= 8

x_is_equal_to_sum_even__mutmut_mutants = {
'x_is_equal_to_sum_even__mutmut_1': x_is_equal_to_sum_even__mutmut_1, 
    'x_is_equal_to_sum_even__mutmut_2': x_is_equal_to_sum_even__mutmut_2, 
    'x_is_equal_to_sum_even__mutmut_3': x_is_equal_to_sum_even__mutmut_3, 
    'x_is_equal_to_sum_even__mutmut_4': x_is_equal_to_sum_even__mutmut_4, 
    'x_is_equal_to_sum_even__mutmut_5': x_is_equal_to_sum_even__mutmut_5, 
    'x_is_equal_to_sum_even__mutmut_6': x_is_equal_to_sum_even__mutmut_6, 
    'x_is_equal_to_sum_even__mutmut_7': x_is_equal_to_sum_even__mutmut_7
}

def is_equal_to_sum_even(*args, **kwargs):
    result = _mutmut_trampoline(x_is_equal_to_sum_even__mutmut_orig, x_is_equal_to_sum_even__mutmut_mutants, *args, **kwargs)
    return result 

is_equal_to_sum_even.__signature__ = _mutmut_signature(x_is_equal_to_sum_even__mutmut_orig)
x_is_equal_to_sum_even__mutmut_orig.__name__ = 'x_is_equal_to_sum_even'


