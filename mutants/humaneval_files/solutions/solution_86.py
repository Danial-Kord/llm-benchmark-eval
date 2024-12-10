
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



def x_add__mutmut_orig(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def x_add__mutmut_1(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[None] for i in range(1, len(lst), 2) if lst[i]%2 == 0])

def x_add__mutmut_2(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(2, len(lst), 2) if lst[i]%2 == 0])

def x_add__mutmut_3(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 3) if lst[i]%2 == 0])

def x_add__mutmut_4(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[None]%2 == 0])

def x_add__mutmut_5(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]/2 == 0])

def x_add__mutmut_6(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%3 == 0])

def x_add__mutmut_7(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 != 0])

def x_add__mutmut_8(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    return sum([lst[i] for i in range(1, len(lst), 2) if lst[i]%2 == 1])

x_add__mutmut_mutants = {
'x_add__mutmut_1': x_add__mutmut_1, 
    'x_add__mutmut_2': x_add__mutmut_2, 
    'x_add__mutmut_3': x_add__mutmut_3, 
    'x_add__mutmut_4': x_add__mutmut_4, 
    'x_add__mutmut_5': x_add__mutmut_5, 
    'x_add__mutmut_6': x_add__mutmut_6, 
    'x_add__mutmut_7': x_add__mutmut_7, 
    'x_add__mutmut_8': x_add__mutmut_8
}

def add(*args, **kwargs):
    result = _mutmut_trampoline(x_add__mutmut_orig, x_add__mutmut_mutants, *args, **kwargs)
    return result 

add.__signature__ = _mutmut_signature(x_add__mutmut_orig)
x_add__mutmut_orig.__name__ = 'x_add'


