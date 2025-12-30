"""
Sum the String

Given a string containing digits and other characters,
return the sum of all numbers in the string.

* Treat consecutive digits as a single number. For example, "13" counts as 13, not 1 + 3.
* Ignore any non-digit characters.
"""

def string_sum(s):
    current_sum = 0
    current_num = ""

    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if current_num != "":
                current_sum += int(current_num)
                current_num = ""
    if current_num != "":
        current_sum += int(current_num)
    return current_sum