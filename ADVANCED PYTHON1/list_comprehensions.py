
# Demonstrating squares of list items in Python

l = [4, 8, 7, 9, 9, 0]

# Method 1: Using for loop
squaredlist = []
for item in l:
    squaredlist.append(item * item)

print(squaredlist)

# Method 2: Using list comprehension (cleaner)
squaredlist = [i * i for i in l]
print(squaredlist)
