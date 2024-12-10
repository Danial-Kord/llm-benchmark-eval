
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



def x_even_odd_count__mutmut_orig(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_1(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 1
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_2(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = None
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_3(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 1
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_4(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = None
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_5(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(None)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_6(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(None)%2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_7(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)/2==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_8(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%3==0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_9(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2!=0:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_10(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==1:
            even_count +=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_11(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count -=1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_12(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count =1
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_13(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=2
        else:
            odd_count +=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_14(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count -=1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_15(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count =1
    return (even_count, odd_count)

def x_even_odd_count__mutmut_16(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_count = 0
    odd_count = 0
    for i in str(abs(num)):
        if int(i)%2==0:
            even_count +=1
        else:
            odd_count +=2
    return (even_count, odd_count)

x_even_odd_count__mutmut_mutants = {
'x_even_odd_count__mutmut_1': x_even_odd_count__mutmut_1, 
    'x_even_odd_count__mutmut_2': x_even_odd_count__mutmut_2, 
    'x_even_odd_count__mutmut_3': x_even_odd_count__mutmut_3, 
    'x_even_odd_count__mutmut_4': x_even_odd_count__mutmut_4, 
    'x_even_odd_count__mutmut_5': x_even_odd_count__mutmut_5, 
    'x_even_odd_count__mutmut_6': x_even_odd_count__mutmut_6, 
    'x_even_odd_count__mutmut_7': x_even_odd_count__mutmut_7, 
    'x_even_odd_count__mutmut_8': x_even_odd_count__mutmut_8, 
    'x_even_odd_count__mutmut_9': x_even_odd_count__mutmut_9, 
    'x_even_odd_count__mutmut_10': x_even_odd_count__mutmut_10, 
    'x_even_odd_count__mutmut_11': x_even_odd_count__mutmut_11, 
    'x_even_odd_count__mutmut_12': x_even_odd_count__mutmut_12, 
    'x_even_odd_count__mutmut_13': x_even_odd_count__mutmut_13, 
    'x_even_odd_count__mutmut_14': x_even_odd_count__mutmut_14, 
    'x_even_odd_count__mutmut_15': x_even_odd_count__mutmut_15, 
    'x_even_odd_count__mutmut_16': x_even_odd_count__mutmut_16
}

def even_odd_count(*args, **kwargs):
    result = _mutmut_trampoline(x_even_odd_count__mutmut_orig, x_even_odd_count__mutmut_mutants, *args, **kwargs)
    return result 

even_odd_count.__signature__ = _mutmut_signature(x_even_odd_count__mutmut_orig)
x_even_odd_count__mutmut_orig.__name__ = 'x_even_odd_count'


