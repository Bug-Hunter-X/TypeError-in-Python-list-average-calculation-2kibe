def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    total = sum(numeric_numbers)
    count = len(numeric_numbers)
    if count == 0:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return total / count

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 0

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 30.0

my_list = [10, 20, 'a', 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: 30.0

my_list = ['a', 'b', 'c']
average = calculate_average(my_list)
print(f"The average is: {average}") # Output: 0