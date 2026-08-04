
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
