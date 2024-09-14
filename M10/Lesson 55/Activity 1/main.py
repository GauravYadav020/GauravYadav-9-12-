# 1st Face: Summing all numbers in a list
def sum_all_numbers(numbers):
    return sum(numbers)

# 2nd Face: Summing only even numbers in a list
def sum_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# 3rd Face: Cumulative sum up to a target value
def sum_up_to_target(target):
    return sum(range(1, target + 1))

# Test the algorithm with examples
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 10

# Applying the three faces
print("1st Face - Sum of all numbers:", sum_all_numbers(numbers_list))
print("2nd Face - Sum of even numbers:", sum_even_numbers(numbers_list))
print("3rd Face - Sum up to target value:", sum_up_to_target(target_value))
