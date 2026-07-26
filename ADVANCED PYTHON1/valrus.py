
n: int = 5
name: str = "harry"

def sum(a: int, b: int) -> int:
    return a + b

# Example walrus operator usage
while (user_input := input("Enter a number (or 'q' to quit): ")) != "q":
    print(f"You entered: {user_input}")
