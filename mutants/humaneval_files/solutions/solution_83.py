
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



def x_prime_length__mutmut_orig(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_1(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = None
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_2(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l != 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_3(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 1 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_4(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l != 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_5(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 2:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_6(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 and l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_7(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return True
    for i in range(2, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_8(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(3, l):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_9(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, None):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_10(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2,):
        if l % i == 0:
            return False
    return True

def x_prime_length__mutmut_11(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l / i == 0:
            return False
    return True

def x_prime_length__mutmut_12(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i != 0:
            return False
    return True

def x_prime_length__mutmut_13(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 1:
            return False
    return True

def x_prime_length__mutmut_14(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return True
    return True

def x_prime_length__mutmut_15(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    l = len(string)
    if l == 0 or l == 1:
        return False
    for i in range(2, l):
        if l % i == 0:
            return False
    return False

x_prime_length__mutmut_mutants = {
'x_prime_length__mutmut_1': x_prime_length__mutmut_1, 
    'x_prime_length__mutmut_2': x_prime_length__mutmut_2, 
    'x_prime_length__mutmut_3': x_prime_length__mutmut_3, 
    'x_prime_length__mutmut_4': x_prime_length__mutmut_4, 
    'x_prime_length__mutmut_5': x_prime_length__mutmut_5, 
    'x_prime_length__mutmut_6': x_prime_length__mutmut_6, 
    'x_prime_length__mutmut_7': x_prime_length__mutmut_7, 
    'x_prime_length__mutmut_8': x_prime_length__mutmut_8, 
    'x_prime_length__mutmut_9': x_prime_length__mutmut_9, 
    'x_prime_length__mutmut_10': x_prime_length__mutmut_10, 
    'x_prime_length__mutmut_11': x_prime_length__mutmut_11, 
    'x_prime_length__mutmut_12': x_prime_length__mutmut_12, 
    'x_prime_length__mutmut_13': x_prime_length__mutmut_13, 
    'x_prime_length__mutmut_14': x_prime_length__mutmut_14, 
    'x_prime_length__mutmut_15': x_prime_length__mutmut_15
}

def prime_length(*args, **kwargs):
    result = _mutmut_trampoline(x_prime_length__mutmut_orig, x_prime_length__mutmut_mutants, *args, **kwargs)
    return result 

prime_length.__signature__ = _mutmut_signature(x_prime_length__mutmut_orig)
x_prime_length__mutmut_orig.__name__ = 'x_prime_length'


