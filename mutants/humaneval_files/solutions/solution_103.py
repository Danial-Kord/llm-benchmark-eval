
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



def x_choose_num__mutmut_orig(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_1(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x >= y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_2(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return +1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_3(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -2
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_4(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y / 2 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_5(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 3 == 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_6(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 != 0:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_7(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 1:
        return y
    if x == y:
        return -1
    return y - 1

def x_choose_num__mutmut_8(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x != y:
        return -1
    return y - 1

def x_choose_num__mutmut_9(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return +1
    return y - 1

def x_choose_num__mutmut_10(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -2
    return y - 1

def x_choose_num__mutmut_11(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y + 1

def x_choose_num__mutmut_12(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if x == y:
        return -1
    return y - 2

x_choose_num__mutmut_mutants = {
'x_choose_num__mutmut_1': x_choose_num__mutmut_1, 
    'x_choose_num__mutmut_2': x_choose_num__mutmut_2, 
    'x_choose_num__mutmut_3': x_choose_num__mutmut_3, 
    'x_choose_num__mutmut_4': x_choose_num__mutmut_4, 
    'x_choose_num__mutmut_5': x_choose_num__mutmut_5, 
    'x_choose_num__mutmut_6': x_choose_num__mutmut_6, 
    'x_choose_num__mutmut_7': x_choose_num__mutmut_7, 
    'x_choose_num__mutmut_8': x_choose_num__mutmut_8, 
    'x_choose_num__mutmut_9': x_choose_num__mutmut_9, 
    'x_choose_num__mutmut_10': x_choose_num__mutmut_10, 
    'x_choose_num__mutmut_11': x_choose_num__mutmut_11, 
    'x_choose_num__mutmut_12': x_choose_num__mutmut_12
}

def choose_num(*args, **kwargs):
    result = _mutmut_trampoline(x_choose_num__mutmut_orig, x_choose_num__mutmut_mutants, *args, **kwargs)
    return result 

choose_num.__signature__ = _mutmut_signature(x_choose_num__mutmut_orig)
x_choose_num__mutmut_orig.__name__ = 'x_choose_num'


