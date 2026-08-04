
# Map Example

l = [1,8,5,3,6,2,4,7]

square = lambda n : n*n

xList = map(square, l)
print(list(xList))

# Filter Example

def even(n):
    if n%2 == 0:
        return True
    else:
        return False

yList = filter(even, l)
print(list(yList))



# Reduce Example: This is a simple example of how to use the venv module to create a virtual environment in Python.



from functools import reduce


l = [1, 8, 5, 3, 6, 2, 4, 7]

# Define a function to add two numbers
def add(x, y):
    return x + y

# Use reduce to sum all elements in the list
result = reduce(add, l)
print(result)


# Reduce another Example: 

def sum(a, b):
    return a + b
print(reduce(sum, l))  # Output: 36

# Return another function that is the composition of two functions f and g.

from functools import reduce


def sum(a,b):
    return a + b

mul = lambda x, y: x * y

print(reduce(sum, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))
