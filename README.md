# Python List Average Calculation with Error Handling

This repository demonstrates a common error in Python when calculating the average of numbers in a list and provides a solution to handle potential `TypeError` exceptions.

The `bug.py` file contains code that raises a `TypeError` when trying to calculate the average of a list containing both numbers and non-numeric elements. The `bugSolution.py` file provides a corrected version that handles this error gracefully.

## Bug Description:

The `calculate_average` function attempts to calculate the average of a list of numbers. However, if the list contains elements that are not numbers (e.g., strings), the `sum()` function will raise a `TypeError`. This is because `sum()` expects all elements in the list to be numbers.

## Solution:

The solution includes error handling to check if the elements are numeric before calculating the sum. It iterates through the list and checks the data type of each element to prevent type errors during calculations.