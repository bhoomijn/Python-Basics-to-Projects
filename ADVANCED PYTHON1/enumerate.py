# Demonstrating manual index and enumerate in Python

l = [4, 8, 99, 0]

# Method 1: Manual index increment
index = 0
for item in l:
    print(f"how{index}")
    index += 1

# Method 2: Using enumerate (cleaner)
for index, item in enumerate(l):
    print(f"the{index} is {item}")

