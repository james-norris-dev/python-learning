def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        if min_index != i:
            numbers[min_index], numbers[i] = numbers[i], numbers[min_index]
    return numbers

