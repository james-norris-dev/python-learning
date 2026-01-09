"""
Circular Prime
Given an integer, determine if it is a circular prime.
* A circular prime is an integer where all rotations of
its digits are themselves prime.
*For example, 197 is a circular prime because all rotations
of its digits: 197, 971, and 719, are prime numbers.
"""
# def is_circular_prime(n):
#     def is_prime(num):
#         if num <= 1:
#             return False
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#         return True
#
#     current = str(n)
#     for j in range(len(str(n))):
#         if not is_prime(int(current)):
#             return False
#         current = current[1:] + current[0]
#     return True
# More Pythonic
def is_circular_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))

    def get_rotations(num_str):
        return [num_str[i:] + num_str[:i] for i in range(len(num_str))]

    rotations = get_rotations(str(n))
    return all(is_prime(int(rotation)) for rotation in rotations)