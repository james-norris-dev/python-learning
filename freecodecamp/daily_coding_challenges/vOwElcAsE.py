"""
vOwElcAsE
Given a string, return a new string where all vowels are converted to
uppercase and all other alphabetical characters are converted to lowercase.
 * Vowels are "a", "e", "i", "o", and "u" in any case.
 * Non-alphabetical characters should remain unchanged.
"""
def vowel_case(s):
    word = s.lower()
    result = [letter.upper() if letter in 'aeiou' else letter for letter in word]
    return ''.join(result)