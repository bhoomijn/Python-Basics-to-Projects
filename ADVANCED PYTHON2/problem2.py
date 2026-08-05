
# Program: Multiplication Table Generator
# Author: Bhoomi
# Language: Python 3

def generate_table(n: int, upto: int = 10) -> str:
    """
    Generate multiplication table for a given number.
    
    Args:
        n (int): The number for which table is generated.
        upto (int): Range limit (default 10).
    
    Returns:
        str: Formatted multiplication table as a string.
    """
    table = [f"{n} x {i} = {n*i}" for i in range(1, upto + 1)]
    return "\n".join(table)

if __name__ == "__main__":
    print(generate_table(7))
