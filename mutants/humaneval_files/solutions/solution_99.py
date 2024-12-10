
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



def x_count_upper__mutmut_orig(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_1(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 1
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_2(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = None
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_3(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(1,len(s),2):
        if s[i] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_4(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),3):
        if s[i] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_5(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[None] in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_6(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] not in "AEIOU":
            count += 1
    return count

def x_count_upper__mutmut_7(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "XXAEIOUXX":
            count += 1
    return count

def x_count_upper__mutmut_8(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count -= 1
    return count

def x_count_upper__mutmut_9(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count = 1
    return count

def x_count_upper__mutmut_10(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0,len(s),2):
        if s[i] in "AEIOU":
            count += 2
    return count

x_count_upper__mutmut_mutants = {
'x_count_upper__mutmut_1': x_count_upper__mutmut_1, 
    'x_count_upper__mutmut_2': x_count_upper__mutmut_2, 
    'x_count_upper__mutmut_3': x_count_upper__mutmut_3, 
    'x_count_upper__mutmut_4': x_count_upper__mutmut_4, 
    'x_count_upper__mutmut_5': x_count_upper__mutmut_5, 
    'x_count_upper__mutmut_6': x_count_upper__mutmut_6, 
    'x_count_upper__mutmut_7': x_count_upper__mutmut_7, 
    'x_count_upper__mutmut_8': x_count_upper__mutmut_8, 
    'x_count_upper__mutmut_9': x_count_upper__mutmut_9, 
    'x_count_upper__mutmut_10': x_count_upper__mutmut_10
}

def count_upper(*args, **kwargs):
    result = _mutmut_trampoline(x_count_upper__mutmut_orig, x_count_upper__mutmut_mutants, *args, **kwargs)
    return result 

count_upper.__signature__ = _mutmut_signature(x_count_upper__mutmut_orig)
x_count_upper__mutmut_orig.__name__ = 'x_count_upper'


