"""
Given two positive integers representing the lengths for the two legs (the two short sides) of a right triangle,
determine whether the hypotenuse is an integer.
"""
def is_integer_hypotenuse(a: int, b: int) -> bool:
    first_leg = a ** 2
    second_leg = b ** 2

    combined_legs = first_leg + second_leg

    third_leg = combined_legs ** 0.5

    if third_leg % 1 == 0:
        return True
    else:
        return False