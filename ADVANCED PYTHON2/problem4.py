
# Program: Find Maximum Value in a List
# Author: Bhoomi
# Language: Python 3

def find_maximum(numbers: list) -> int:
    """
    Return the maximum value from a list of integers.
    
    Args:
        numbers (list): List of integers.
    
    Returns:
        int: Maximum value in the list.
    """
    return max(numbers)

if __name__ == "__main__":
    numbers = [88, 89, 545, 77]
    maximum = find_maximum(numbers)
    print(f"The maximum value in the list is: {maximum}")
