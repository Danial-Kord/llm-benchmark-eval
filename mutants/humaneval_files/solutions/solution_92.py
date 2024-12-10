
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



def x_is_bored__mutmut_orig(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_1(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'XX[.?!]\s*XX', S)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', None)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_3(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*',)
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_4(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = None
    return sum(sentence[0:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_5(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[1:2] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_6(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:3] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_7(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[None] == 'I ' for sentence in sentences)

def x_is_bored__mutmut_8(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] != 'I ' for sentence in sentences)

def x_is_bored__mutmut_9(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]\s*', S)
    return sum(sentence[0:2] == 'XXI XX' for sentence in sentences)

x_is_bored__mutmut_mutants = {
'x_is_bored__mutmut_1': x_is_bored__mutmut_1, 
    'x_is_bored__mutmut_2': x_is_bored__mutmut_2, 
    'x_is_bored__mutmut_3': x_is_bored__mutmut_3, 
    'x_is_bored__mutmut_4': x_is_bored__mutmut_4, 
    'x_is_bored__mutmut_5': x_is_bored__mutmut_5, 
    'x_is_bored__mutmut_6': x_is_bored__mutmut_6, 
    'x_is_bored__mutmut_7': x_is_bored__mutmut_7, 
    'x_is_bored__mutmut_8': x_is_bored__mutmut_8, 
    'x_is_bored__mutmut_9': x_is_bored__mutmut_9
}

def is_bored(*args, **kwargs):
    result = _mutmut_trampoline(x_is_bored__mutmut_orig, x_is_bored__mutmut_mutants, *args, **kwargs)
    return result 

is_bored.__signature__ = _mutmut_signature(x_is_bored__mutmut_orig)
x_is_bored__mutmut_orig.__name__ = 'x_is_bored'


