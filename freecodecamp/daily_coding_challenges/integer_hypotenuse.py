"""
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle,
determine whether the hypotenuse is an integer.
"""
# def is_integer_hypotenuse(a: int, b: int) -> bool:
#     first_leg = a ** 2
#     second_leg = b ** 2
#
#     combined_legs = first_leg + second_leg
#
#     third_leg = combined_legs ** 0.5
#
#     if third_leg % 1 == 0:
#         return True
#     else:
#         return False

# More Pythonic, return the result of the modulo
# def is_integer_hypotenuse(a: int, b: int) -> bool:
#     first_leg = a ** 2
#     second_leg = b ** 2
#
#     combined_legs = first_leg + second_leg
#
#     third_leg = combined_legs ** 0.5
#
#     return third_leg % 1 == 0

def is_integer_hypotenuse(a: int, b: int) -> bool:
    """
    Check if the hypotenuse of a right triangle is an integer.
    Uses Pythagorean theorem: c ** 2 = a ** 2 + b ** 2

    Progression:
    - Initially broke down: first_leg, second_leg, combined_legs, third_leg
    - Refined to direct formula once logic was clear
    - Checking if hypotenuse % 1 == 0 determines if it's a whole number
    """
    return (((a ** 2) + (b ** 2)) ** 0.5) % 1 == 0

