"""
Sorted Array?
Given an array of numbers, determine if the numbers are sorted in ascending order,
descending order, or neither.

If the given array is:
* In ascending order (lowest to highest), return "Ascending".
* In descending order (highest to lowest), return "Descending".
* Not sorted in ascending or descending order, return "Not sorted".
"""
def is_sorted(arr):
    expected_pattern = ""
    for i in range(len(arr) - 1):
        if expected_pattern == "":
            if arr[i] > arr[i + 1]:
                expected_pattern = "Descending"
            elif arr[i] < arr[i + 1]:
                expected_pattern = "Ascending"
            else:
                continue
        else:
            if expected_pattern == "Descending":
                if arr[i] >= arr[i + 1]:
                    continue
                else:
                    return "Not sorted"
            elif expected_pattern == "Ascending":
                if arr[i] <= arr[i + 1]:
                    continue
                else:
                    return "Not sorted"
            else:
                return "Not sorted"

    if expected_pattern == "":
        return "Not sorted"
    return expected_pattern