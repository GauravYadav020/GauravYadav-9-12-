# 1st Face: Summing all numbers in a list using iteration
def sum_all_numbers_iter(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 2nd Face: Summing only even numbers in a list using iteration
def sum_even_numbers_iter(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

# 3rd Face: Cumulative sum up to a target value using iteration
def sum_up_to_target_iter(target):
    total = 0
    for num in range(1, target + 1):
        total += num
    return total

# Test the algorithm with examples
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 10

# Applying the three faces with iteration
print("1st Face (Iteration) - Sum of all numbers:", sum_all_numbers_iter(numbers_list))
print("2nd Face (Iteration) - Sum of even numbers:", sum_even_numbers_iter(numbers_list))
print("3rd Face (Iteration) - Sum up to target value:", sum_up_to_target_iter(target_value))
