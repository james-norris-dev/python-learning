# implement a function that uses the bisection method to find the square root of a number

def square_root_bisection(num, tolerance = 0.01, max_iterations = 50):
    if num < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif num == 0 or num == 1:
        print(f"The square root of {num} is {num}")
        return num
    else:
        mid = 0
        iteration = 0

        if num < 1:
            low = num
            high = 1
        else:
            low = 1
            high = num

        while (high - low) > tolerance and iteration < max_iterations:
            mid = (low + high) / 2
            if mid * mid < num:
                low = mid
            elif mid * mid > num:
                high = mid
            else:
                high = mid
            iteration += 1

        if iteration >= max_iterations:
            print(f"Failed to converge within {max_iterations} iterations")
            return None
        else:
            print(f"The square root of {num} is approximately {mid}")
            return mid