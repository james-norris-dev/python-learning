"""
Circular Prime
Given an integer, determine if it is a circular prime.
* A circular prime is an integer where all rotations of
its digits are themselves prime.
*For example, 197 is a circular prime because all rotations
of its digits: 197, 971, and 719, are prime numbers.
"""
def is_circular_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    current = str(n)
    for j in range(len(str(n))):
        if not is_prime(int(current)):
            return False
        current = current[1:] + current[0]
    return True

if __name__ == '__main__':
    is_circular_prime(100025687741)