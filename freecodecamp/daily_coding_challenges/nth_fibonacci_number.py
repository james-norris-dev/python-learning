def nth_fibonacci(n):
    """
    Original solution:

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        counter = 3
        past_num = 0
        current_num = 1
        while counter <= n:
            fib_sum = past_num + current_num
            past_num = current_num
            current_num = fib_sum
            counter += 1
     return current_num
    """

    # More Pythonic Solution
    if n == 1:
        return 0
    elif n == 2:
        return 1

    past_num = 0
    current_num = 1

    for _ in range(3, n + 1):
        past_num, current_num = current_num, past_num + current_num

    return current_num