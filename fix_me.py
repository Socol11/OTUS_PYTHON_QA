"""This module calculates averages"""


def calculate_average(nums):
    """Calculates average"""
    total = sum(nums)
    count = len(nums)
    average = total / count
    return average


numbers = [10, 15, 20]
result = calculate_average(numbers)
print("The average is:", result)
