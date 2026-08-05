
# Program: Check divisibility by 5
# Author: Bhoomi
# Language: Python 3

def check_divisible_by_5(numbers: list) -> None:
    """
    Print numbers from the list that are divisible by 5.
    
    Args:
        numbers (list): List of integers.
    """
    for num in numbers:
        if num % 5 == 0:
            print(f"The {num} is divisible by 5")

if __name__ == "__main__":
    numbers = [67, 5, 25, 30, 9, 33]
    check_divisible_by_5(numbers)
