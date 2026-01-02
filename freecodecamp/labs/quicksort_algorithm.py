def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[-1]
    less = []
    equal = []
    greater = []

    for num in numbers:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        elif num > pivot:
            greater.append(num)

    sorted_numbers = quick_sort(less) + equal + quick_sort(greater)
    return sorted_numbers

if __name__ == '__main__':
    print(quick_sort([20, 3, 14, 1, 5]))
    print(quick_sort([83, 4, 24, 2]))
    print(quick_sort([4, 42, 16, 23, 15, 8]))
    print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))