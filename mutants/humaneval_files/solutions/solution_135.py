
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



def x_check_if_last_char_is_a_letter__mutmut_orig(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_1(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split('XX XX')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_2(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[+1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_3(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-2]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_4(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[None]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_5(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = None
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_6(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return False if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_7(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) != 1 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_8(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 2 and (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_9(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (98 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_10(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 < ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_11(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) < 122) else False

def x_check_if_last_char_is_a_letter__mutmut_12(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 123) else False

def x_check_if_last_char_is_a_letter__mutmut_13(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 or (97 <= ord(check.lower()) <= 122) else False

def x_check_if_last_char_is_a_letter__mutmut_14(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''
 
    check = txt.split(' ')[-1]
    return True if len(check) == 1 and (97 <= ord(check.lower()) <= 122) else True

x_check_if_last_char_is_a_letter__mutmut_mutants = {
'x_check_if_last_char_is_a_letter__mutmut_1': x_check_if_last_char_is_a_letter__mutmut_1, 
    'x_check_if_last_char_is_a_letter__mutmut_2': x_check_if_last_char_is_a_letter__mutmut_2, 
    'x_check_if_last_char_is_a_letter__mutmut_3': x_check_if_last_char_is_a_letter__mutmut_3, 
    'x_check_if_last_char_is_a_letter__mutmut_4': x_check_if_last_char_is_a_letter__mutmut_4, 
    'x_check_if_last_char_is_a_letter__mutmut_5': x_check_if_last_char_is_a_letter__mutmut_5, 
    'x_check_if_last_char_is_a_letter__mutmut_6': x_check_if_last_char_is_a_letter__mutmut_6, 
    'x_check_if_last_char_is_a_letter__mutmut_7': x_check_if_last_char_is_a_letter__mutmut_7, 
    'x_check_if_last_char_is_a_letter__mutmut_8': x_check_if_last_char_is_a_letter__mutmut_8, 
    'x_check_if_last_char_is_a_letter__mutmut_9': x_check_if_last_char_is_a_letter__mutmut_9, 
    'x_check_if_last_char_is_a_letter__mutmut_10': x_check_if_last_char_is_a_letter__mutmut_10, 
    'x_check_if_last_char_is_a_letter__mutmut_11': x_check_if_last_char_is_a_letter__mutmut_11, 
    'x_check_if_last_char_is_a_letter__mutmut_12': x_check_if_last_char_is_a_letter__mutmut_12, 
    'x_check_if_last_char_is_a_letter__mutmut_13': x_check_if_last_char_is_a_letter__mutmut_13, 
    'x_check_if_last_char_is_a_letter__mutmut_14': x_check_if_last_char_is_a_letter__mutmut_14
}

def check_if_last_char_is_a_letter(*args, **kwargs):
    result = _mutmut_trampoline(x_check_if_last_char_is_a_letter__mutmut_orig, x_check_if_last_char_is_a_letter__mutmut_mutants, *args, **kwargs)
    return result 

check_if_last_char_is_a_letter.__signature__ = _mutmut_signature(x_check_if_last_char_is_a_letter__mutmut_orig)
x_check_if_last_char_is_a_letter__mutmut_orig.__name__ = 'x_check_if_last_char_is_a_letter'


