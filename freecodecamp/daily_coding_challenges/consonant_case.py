"""
Consonant Case
Given a string representing a variable name, convert it to consonant case using the following rules:
* All consonants should be converted to uppercase.
* All vowels (a, e, i, o, u in any case) should be converted to lowercase.
* All hyphens (-) should be converted to underscores (_).
"""
def to_consonant_case(s: str) -> str:
    lowercase_word = s.lower()

    if "-" in lowercase_word:
        lowercase_word = lowercase_word.replace("-", "_")

    uppercase_word = ""
    for letter in lowercase_word:
        if letter not in "aeiou1234567890":
            uppercase_word += letter.upper()
        else:
            uppercase_word += letter

    return uppercase_word