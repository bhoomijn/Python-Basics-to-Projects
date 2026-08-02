
# Demonstrating writing multiplication table to a file

n = int(input("Enter a number: "))
table = [n * i for i in range(1, 11)]

with open("1.txt", "a") as f:   # file extension ko sahi rakho (.txt)
    f.write(str(table) + "\n")
